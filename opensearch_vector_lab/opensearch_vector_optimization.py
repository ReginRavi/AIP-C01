#!/usr/bin/env python3
"""
OpenSearch Vector Search Optimization & Benchmark Reference Implementation
AWS Certified Generative AI Engineer - Practical Lab

Demonstrates:
1. OpenSearch k-NN index creation with Lucene HNSW algorithm settings (M, ef_construction).
2. Dynamic tuning of index.knn.algo_param.ef_search to improve Recall@K and control latency.
3. OpenSearch _reindex API payload generation for shard rebalancing & load distribution.
4. Synthetic vector search benchmark testing latency vs recall trade-offs.
"""

import json
import math
import random
import time
from typing import Dict, List, Tuple

class OpenSearchVectorClusterSimulator:
    """
    Simulates an Amazon OpenSearch Service k-NN Vector Search Cluster
    with HNSW index parameter tuning and shard load balancing.
    """

    def __init__(self, num_nodes: int = 4, num_shards: int = 4, corpus_millions: float = 35.0):
        self.num_nodes = num_nodes
        self.num_shards = num_shards
        self.corpus_millions = corpus_millions

        # HNSW Index Parameters (Default untuned state)
        self.m = 16
        self.ef_construction = 100
        self.ef_search = 16
        self.routing_strategy = "imbalanced"

    def get_index_mapping_payload(self, dimension: int = 768) -> Dict:
        """
        Returns the OpenSearch REST API payload for creating a k-NN index
        with custom HNSW parameters.
        """
        return {
            "settings": {
                "index": {
                    "knn": True,
                    "knn.algo_param.ef_search": self.ef_search,
                    "number_of_shards": self.num_shards,
                    "number_of_replicas": 1
                }
            },
            "mappings": {
                "properties": {
                    "article_id": {"type": "keyword"},
                    "article_title": {"type": "text"},
                    "article_vector": {
                        "type": "knn_vector",
                        "dimension": dimension,
                        "method": {
                            "name": "hnsw",
                            "space_type": "cosinesimil",
                            "engine": "lucene",
                            "parameters": {
                                "m": self.m,
                                "ef_construction": self.ef_construction
                            }
                        }
                    }
                }
            }
        }

    def get_reindex_payload(self, source_index: str = "articles_v1", target_index: str = "articles_v2_rebalanced") -> Dict:
        """
        Returns the OpenSearch REST API payload for re-indexing into an index with
        balanced primary shards and optimized hash distribution.
        """
        return {
            "source": {
                "index": source_index
            },
            "dest": {
                "index": target_index
            },
            "script": {
                "source": "ctx._routing = ctx._id",  # Distribute documents uniformly using document ID hash
                "lang": "painless"
            }
        }

    def tune_hnsw_parameters(self, m: int = 32, ef_construction: int = 250, ef_search: int = 128):
        """Solution 1: Tune HNSW parameters for high recall & latency control."""
        self.m = m
        self.ef_construction = ef_construction
        self.ef_search = ef_search
        print(f"[Tuning Applied] HNSW M={m}, efConstruction={ef_construction}, efSearch={ef_search}")

    def rebalance_shards(self, new_shard_count: int = 8):
        """Solution 2: Resize and rebalance shards evenly across cluster nodes."""
        self.num_shards = new_shard_count
        self.routing_strategy = "rebalanced"
        print(f"[Rebalance Executed] Primary Shards scaled to {new_shard_count}. Uniform routing active.")

    def run_vector_search_benchmark(self, qps: int = 1200, top_k: int = 10) -> Dict:
        """
        Simulates vector search execution under real traffic load and returns key metrics.
        """
        # Calculate shard distribution
        if self.routing_strategy == "imbalanced":
            hot_shard_qps = qps * 0.70  # Shard 0 handles 70% of total query traffic
            other_shard_qps = (qps * 0.30) / max(1, self.num_shards - 1)
            shard_qps_list = [hot_shard_qps] + [other_shard_qps] * (self.num_shards - 1)
        else:
            shard_qps_list = [qps / self.num_shards] * self.num_shards

        # Compute Max Node CPU %
        shards_per_node = math.ceil(self.num_shards / self.num_nodes)
        max_node_qps = max(
            sum(shard_qps_list[n * shards_per_node: (n + 1) * shards_per_node])
            for n in range(self.num_nodes)
        )
        node_capacity = 350.0  # Safe QPS baseline per node
        hot_node_cpu = min(99.0, (max_node_qps / node_capacity) * 100 + (self.corpus_millions / 50.0) * 12.0)

        # Compute HNSW Search Base Latency
        base_latency_ms = (self.ef_search * 0.45) + (self.m * 0.20) + 12.0
        
        # Queueing Latency Spike if Hot Node CPU > 75%
        queueing_delay_ms = 0.0
        if hot_node_cpu > 75.0:
            queueing_delay_ms = math.pow((hot_node_cpu - 75.0) / 5.0, 2) * 6.0

        p99_latency_ms = round(base_latency_ms + queueing_delay_ms, 2)
        p50_latency_ms = round((base_latency_ms * 0.5) + (queueing_delay_ms * 0.2), 2)

        # Compute Recall @ K (%) using HNSW approximation model
        recall = 100.0 / (1.0 + math.exp(-(self.ef_search - 32) / 18.0))
        if self.m < 16:
            recall *= 0.90
        recall_at_k = min(99.5, max(35.0, round(recall, 1)))

        return {
            "qps_requested": qps,
            "hot_node_cpu_pct": round(hot_node_cpu, 1),
            "p50_latency_ms": p50_latency_ms,
            "p99_latency_ms": p99_latency_ms,
            "recall_at_k_pct": recall_at_k,
            "queueing_delay_ms": round(queueing_delay_ms, 2),
            "routing_strategy": self.routing_strategy,
            "ef_search": self.ef_search,
            "m": self.m,
            "shards": self.num_shards
        }

def print_benchmark_report(title: str, results: Dict):
    print(f"\n==================================================")
    print(f" {title}")
    print(f"==================================================")
    print(f" Cluster Routing:        {results['routing_strategy'].upper()}")
    print(f" Primary Shards:         {results['shards']}")
    print(f" HNSW Parameters:        M={results['m']}, efSearch={results['ef_search']}")
    print(f" Requested QPS:          {results['qps_requested']} QPS")
    print(f" Hot Node CPU Load:      {results['hot_node_cpu_pct']}%")
    print(f" P50 Latency:            {results['p50_latency_ms']} ms")
    print(f" P99 Latency:            {results['p99_latency_ms']} ms (Queue delay: {results['queueing_delay_ms']} ms)")
    print(f" Recommendation Recall:  {results['recall_at_k_pct']}%")
    
    if results['p99_latency_ms'] > 200:
        print(" STATUS: [CRITICAL] Severe Latency Spike & Hot Shard Bottleneck")
    elif results['recall_at_k_pct'] < 75:
        print(" STATUS: [WARNING] Irrelevant or Weakly Related Articles Returned")
    else:
        print(" STATUS: [OPTIMAL] Low Latency & High Recommendation Quality")

def main():
    print("Initializing OpenSearch Vector Search Simulator (35 Million Vectors)...")
    cluster = OpenSearchVectorClusterSimulator(num_nodes=4, num_shards=4, corpus_millions=35.0)

    # Step 1: Run Unoptimized Default State
    res_default = cluster.run_vector_search_benchmark(qps=1200)
    print_benchmark_report("TEST 1: UNOPTIMIZED DEFAULT STATE (Hot Shards + Untuned HNSW)", res_default)

    # Step 2: Apply Solution 1 - HNSW Parameter Tuning
    cluster.tune_hnsw_parameters(m=32, ef_construction=250, ef_search=128)
    res_hnsw = cluster.run_vector_search_benchmark(qps=1200)
    print_benchmark_report("TEST 2: SOLUTION 1 APPLIED (HNSW M=32, efSearch=128)", res_hnsw)

    # Step 3: Apply Solution 2 - Shard Resizing & Rebalancing
    cluster.rebalance_shards(new_shard_count=8)
    res_rebalanced = cluster.run_vector_search_benchmark(qps=1200)
    print_benchmark_report("TEST 3: FULLY OPTIMIZED (HNSW Tuned + 8 Balanced Shards)", res_rebalanced)

    # Generate and display OpenSearch REST API payload snippet
    print("\n--------------------------------------------------")
    print(" OpenSearch k-NN Index Creation REST API Payload")
    print("--------------------------------------------------")
    print(json.dumps(cluster.get_index_mapping_payload(dimension=768), indent=2))

if __name__ == "__main__":
    main()
