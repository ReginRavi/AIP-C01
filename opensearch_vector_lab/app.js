/* OpenSearch Vector Search Optimization Simulator & Benchmark Engine */

document.addEventListener('DOMContentLoaded', () => {
  // Global State
  const state = {
    preset: 'default',
    traffic: 1200,     // QPS
    corpus: 35,        // Millions
    dim: 768,          // Vector dimension
    m: 16,             // HNSW M
    efConst: 100,      // efConstruction
    efSearch: 16,      // efSearch (Default untuned)
    nodes: 4,          // Node count
    shards: 4,         // Primary Shards
    routing: 'imbalanced', // 'imbalanced' or 'rebalanced'
    queryText: 'Generative AI LLM applications in financial stock market forecasting'
  };

  // Preset Configurations
  const presets = {
    default: {
      m: 16,
      efConst: 100,
      efSearch: 16,
      nodes: 4,
      shards: 4,
      routing: 'imbalanced',
      traffic: 1200
    },
    hnsw: {
      m: 32,
      efConst: 250,
      efSearch: 128,
      nodes: 4,
      shards: 4,
      routing: 'imbalanced',
      traffic: 1200
    },
    shards: {
      m: 16,
      efConst: 100,
      efSearch: 16,
      nodes: 4,
      shards: 8,
      routing: 'rebalanced',
      traffic: 1200
    },
    optimized: {
      m: 32,
      efConst: 250,
      efSearch: 128,
      nodes: 4,
      shards: 8,
      routing: 'rebalanced',
      traffic: 1200
    }
  };

  // DOM Elements
  const btnPresets = document.querySelectorAll('.btn-preset');
  const sliderTraffic = document.getElementById('sliderTraffic');
  const valTraffic = document.getElementById('valTraffic');
  const sliderCorpus = document.getElementById('sliderCorpus');
  const valCorpus = document.getElementById('valCorpus');
  const selectDim = document.getElementById('selectDim');

  const sliderM = document.getElementById('sliderM');
  const valM = document.getElementById('valM');
  const sliderEfConst = document.getElementById('sliderEfConst');
  const valEfConst = document.getElementById('valEfConst');
  const sliderEfSearch = document.getElementById('sliderEfSearch');
  const valEfSearch = document.getElementById('valEfSearch');

  const selectNodes = document.getElementById('selectNodes');
  const valNodes = document.getElementById('valNodes');
  const selectShards = document.getElementById('selectShards');
  const valShards = document.getElementById('valShards');
  const selectRouting = document.getElementById('selectRouting');
  const btnReindex = document.getElementById('btnReindex');

  const clusterNodesContainer = document.getElementById('clusterNodesContainer');
  const hnswCanvas = document.getElementById('hnswCanvas');
  const ctx = hnswCanvas.getContext('2d');

  const inputQuery = document.getElementById('inputQuery');
  const btnRunQuery = document.getElementById('btnRunQuery');
  const listCurrentArticles = document.getElementById('listCurrentArticles');
  const listTargetArticles = document.getElementById('listTargetArticles');

  const codeSnippet = document.getElementById('codeSnippet');
  const btnCopyCode = document.getElementById('btnCopyCode');

  // Chart.js instance
  let latencyRecallChart = null;

  // Initialize Chart.js
  function initChart() {
    const ctxChart = document.getElementById('chartLatencyRecall').getContext('2d');
    latencyRecallChart = new Chart(ctxChart, {
      type: 'line',
      data: {
        labels: ['0s', '5s', '10s', '15s', '20s', '25s', '30s'],
        datasets: [
          {
            label: 'P99 Latency (ms)',
            data: [420, 450, 480, 465, 470, 490, 465],
            borderColor: '#ef4444',
            backgroundColor: 'rgba(239, 68, 68, 0.1)',
            yAxisID: 'yLatency',
            tension: 0.3,
            fill: true
          },
          {
            label: 'Recall @ 10 (%)',
            data: [58, 59, 57, 58.4, 60, 57.5, 58.4],
            borderColor: '#34d399',
            backgroundColor: 'rgba(52, 211, 153, 0.1)',
            yAxisID: 'yRecall',
            tension: 0.3,
            fill: false
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          x: {
            grid: { color: 'rgba(51, 65, 85, 0.3)' },
            ticks: { color: '#94a3b8' }
          },
          yLatency: {
            type: 'linear',
            position: 'left',
            title: { display: true, text: 'Latency (ms)', color: '#ef4444' },
            grid: { color: 'rgba(51, 65, 85, 0.3)' },
            ticks: { color: '#ef4444' }
          },
          yRecall: {
            type: 'linear',
            position: 'right',
            title: { display: true, text: 'Recall %', color: '#34d399' },
            grid: { drawOnChartArea: false },
            ticks: { color: '#34d399' },
            min: 0,
            max: 100
          }
        },
        plugins: {
          legend: { labels: { color: '#f8fafc' } }
        }
      }
    });
  }

  // Simulation Calculations
  function calculateMetrics() {
    // 1. Shard Load Distribution & Hot Shards
    let shardLoads = [];
    const numShards = state.shards;
    const numNodes = state.nodes;

    if (state.routing === 'imbalanced') {
      // Hot shard imbalance: Shard 0 gets 65-75% of query load
      const hotLoad = 0.70;
      const totalLoad = state.traffic;
      shardLoads[0] = Math.round(totalLoad * hotLoad);
      const remaining = totalLoad * (1 - hotLoad);
      for (let i = 1; i < numShards; i++) {
        shardLoads[i] = Math.round(remaining / (numShards - 1));
      }
    } else {
      // Even distribution across all shards
      const loadPerShard = Math.round(state.traffic / numShards);
      for (let i = 0; i < numShards; i++) {
        shardLoads[i] = loadPerShard;
      }
    }

    // Node CPU calculation based on max shard assigned
    let nodeCPUs = [];
    const shardsPerNode = Math.ceil(numShards / numNodes);
    for (let n = 0; n < numNodes; n++) {
      let nodeQps = 0;
      for (let s = n * shardsPerNode; s < (n + 1) * shardsPerNode && s < numShards; s++) {
        nodeQps += shardLoads[s] || 0;
      }
      // Compute capacity baseline (each node handles ~400 QPS comfortably)
      const baseCap = 350;
      let cpu = Math.min(99, Math.round((nodeQps / baseCap) * 100 + (state.corpus / 50) * 12));
      nodeCPUs[n] = Math.max(12, cpu);
    }

    const hotShardCpu = Math.max(...nodeCPUs);

    // 2. Latency calculation
    // Base HNSW traversal latency depends on efSearch and M
    const baseHnswLatency = (state.efSearch * 0.45) + (state.m * 0.2); // ms
    // Queueing delay spike if hot shard CPU > 75%
    let queueingDelay = 0;
    if (hotShardCpu > 75) {
      queueingDelay = Math.pow((hotShardCpu - 75) / 5, 2) * 6; // exponential latency spike
    }
    const p99Latency = Math.round(baseHnswLatency + queueingDelay + 12);
    const p50Latency = Math.round((baseHnswLatency * 0.5) + (queueingDelay * 0.2) + 5);

    // 3. Recall @ 10 calculation
    // Sigmoid curve based on efSearch & M
    // efSearch = 16 -> ~58% recall
    // efSearch = 64 -> ~88% recall
    // efSearch = 128 -> ~97.5% recall
    let recallVal = 100 / (1 + Math.exp(-(state.efSearch - 32) / 18));
    if (state.m < 16) recallVal *= 0.9;
    if (state.dim > 1000) recallVal *= 0.94; // higher dimension curse of dimensionality penalty if untuned
    const recallAt10 = Math.min(99.5, Math.max(35, parseFloat(recallVal.toFixed(1))));

    // 4. Throughput calculation
    const maxClusterQps = numNodes * 450;
    let successfulQps = state.traffic;
    let throttledPct = 0;
    if (hotShardCpu >= 95) {
      throttledPct = Math.round(((hotShardCpu - 80) / 20) * 45);
      successfulQps = Math.round(state.traffic * (1 - throttledPct / 100));
    }

    return {
      shardLoads,
      nodeCPUs,
      hotShardCpu,
      p99Latency,
      p50Latency,
      recallAt10,
      successfulQps,
      throttledPct,
      queueingDelay: Math.round(queueingDelay),
      baseHnswLatency: Math.round(baseHnswLatency)
    };
  }

  // Update UI Elements
  function updateUI() {
    const metrics = calculateMetrics();

    // 1. Update KPI Values
    document.getElementById('kpiValLatency').innerText = `${metrics.p99Latency} ms`;
    const kpiStatusLatency = document.getElementById('kpiStatusLatency');
    if (metrics.p99Latency > 200) {
      kpiStatusLatency.className = 'kpi-status status-critical';
      kpiStatusLatency.innerHTML = '<i class="fa-solid fa-triangle-exclamation"></i> High Latency Spike';
    } else if (metrics.p99Latency > 80) {
      kpiStatusLatency.className = 'kpi-status status-warning';
      kpiStatusLatency.innerHTML = '<i class="fa-solid fa-circle-exclamation"></i> Elevated Latency';
    } else {
      kpiStatusLatency.className = 'kpi-status status-good';
      kpiStatusLatency.innerHTML = '<i class="fa-solid fa-circle-check"></i> Target Sub-50ms';
    }

    document.getElementById('kpiValRecall').innerText = `${metrics.recallAt10}%`;
    const kpiStatusRecall = document.getElementById('kpiStatusRecall');
    if (metrics.recallAt10 < 75) {
      kpiStatusRecall.className = 'kpi-status status-warning';
      kpiStatusRecall.innerHTML = '<i class="fa-solid fa-circle-exclamation"></i> Irrelevant Matches Returned';
    } else {
      kpiStatusRecall.className = 'kpi-status status-good';
      kpiStatusRecall.innerHTML = '<i class="fa-solid fa-circle-check"></i> High Relevance & Precision';
    }

    document.getElementById('kpiValHotShard').innerText = `${metrics.hotShardCpu}%`;
    const kpiStatusHotShard = document.getElementById('kpiStatusHotShard');
    if (metrics.hotShardCpu > 80) {
      kpiStatusHotShard.className = 'kpi-status status-critical';
      kpiStatusHotShard.innerHTML = `<i class="fa-solid fa-temperature-arrow-up"></i> Overloaded Node 1`;
    } else {
      kpiStatusHotShard.className = 'kpi-status status-good';
      kpiStatusHotShard.innerHTML = `<i class="fa-solid fa-snowflake"></i> Balanced Load Across Cluster`;
    }

    document.getElementById('kpiValThroughput').innerText = `${metrics.successfulQps} / ${state.traffic}`;
    const kpiStatusThroughput = document.getElementById('kpiStatusThroughput');
    if (metrics.throttledPct > 0) {
      kpiStatusThroughput.className = 'kpi-status status-warning';
      kpiStatusThroughput.innerText = `Throttling ${metrics.throttledPct}%`;
    } else {
      kpiStatusThroughput.className = 'kpi-status status-good';
      kpiStatusThroughput.innerText = '0% Drop Rate';
    }

    // 2. Update Cluster Node Heatmap
    renderClusterHeatmap(metrics);

    // 3. Update Trace Analytics Waterfall
    renderTraceWaterfall(metrics);

    // 4. Update HNSW Visualizer Canvas
    drawHnswGraph();

    // 5. Update Recommendations Article List
    renderRecommendations(metrics);

    // 6. Update Code Snippet
    updateCodeSnippet();

    // 7. Update Chart
    updateChart(metrics);
  }

  function renderClusterHeatmap(metrics) {
    clusterNodesContainer.innerHTML = '';

    const numNodes = state.nodes;
    const numShards = state.shards;
    const shardsPerNode = Math.ceil(numShards / numNodes);

    for (let n = 0; n < numNodes; n++) {
      const nodeCpu = metrics.nodeCPUs[n];
      const isHotNode = nodeCpu > 80;

      const nodeCard = document.createElement('div');
      nodeCard.className = `node-card ${isHotNode ? 'hot-border' : ''}`;
      
      let shardsHtml = '';
      for (let s = n * shardsPerNode; s < (n + 1) * shardsPerNode && s < numShards; s++) {
        const shardLoad = metrics.shardLoads[s] || 0;
        const shardPct = Math.min(100, Math.round((shardLoad / (state.traffic / numShards * 1.5)) * 100));
        
        let colorClass = 'bg-green';
        if (shardPct > 80 || (state.routing === 'imbalanced' && s === 0)) colorClass = 'bg-red';
        else if (shardPct > 50) colorClass = 'bg-yellow';

        const isHotShard = (state.routing === 'imbalanced' && s === 0 && metrics.hotShardCpu > 80);

        shardsHtml += `
          <div class="shard-pill ${isHotShard ? 'hot' : ''}">
            <div class="shard-title">
              <span>Primary Shard ${s}</span>
              <span>${shardLoad} QPS</span>
            </div>
            <div class="shard-load-bar">
              <div class="shard-load-fill ${colorClass}" style="width: ${Math.max(10, shardPct)}%;"></div>
            </div>
          </div>
        `;
      }

      nodeCard.innerHTML = `
        <div class="node-header">
          <span class="node-name"><i class="fa-solid fa-server"></i> Node opensearch-0${n + 1}</span>
          <span class="badge ${nodeCpu > 80 ? 'badge-aws' : ''}">${nodeCpu}% CPU</span>
        </div>
        <div class="node-metrics">
          <span>RAM: ${(8 + (state.corpus / 50) * 12).toFixed(1)} GB / 32 GB</span>
          <span>Vector RAM: ${(state.m * 0.4 + state.corpus * 0.3).toFixed(1)} GB</span>
        </div>
        <div class="shards-grid">
          ${shardsHtml}
        </div>
      `;

      clusterNodesContainer.appendChild(nodeCard);
    }
  }

  function renderTraceWaterfall(metrics) {
    document.getElementById('timeShardQueue').innerText = `${metrics.queueingDelay + 4} ms`;
    document.getElementById('timeHnswTraversal').innerText = `${metrics.baseHnswLatency} ms`;

    const totalTime = metrics.p99Latency;
    const shardQueuePct = Math.round(((metrics.queueingDelay + 4) / totalTime) * 100);
    const hnswPct = Math.round((metrics.baseHnswLatency / totalTime) * 100);

    const traceHotShardSpan = document.getElementById('traceHotShardSpan');
    const traceHnswSpan = document.getElementById('traceHnswSpan');

    traceHotShardSpan.querySelector('.trace-bar').style.width = `${Math.max(5, shardQueuePct)}%`;
    traceHnswSpan.querySelector('.trace-bar').style.width = `${Math.max(5, hnswPct)}%`;

    if (metrics.queueingDelay > 100) {
      traceHotShardSpan.querySelector('.trace-bar').style.background = '#ef4444';
    } else {
      traceHotShardSpan.querySelector('.trace-bar').style.background = '#10b981';
    }
  }

  // Draw HNSW Spatial Graph on HTML5 Canvas
  function drawHnswGraph() {
    const width = hnswCanvas.width = hnswCanvas.parentElement.clientWidth || 900;
    const height = hnswCanvas.height = 320;
    ctx.clearRect(0, 0, width, height);

    // Draw background grid lines
    ctx.strokeStyle = 'rgba(51, 65, 85, 0.2)';
    ctx.lineWidth = 1;
    for (let x = 0; x < width; x += 40) {
      ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, height); ctx.stroke();
    }
    for (let y = 0; y < height; y += 40) {
      ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(width, y); ctx.stroke();
    }

    // Generate graph nodes for 3 layers: Layer 2 (Entry), Layer 1 (Highway), Layer 0 (Base Dense)
    const entryX = 80, entryY = 60;
    const targetX = width - 100, targetY = height - 70;

    // Draw Layer boundaries
    ctx.font = '12px JetBrains Mono';
    ctx.fillStyle = '#64748b';
    ctx.fillText('HNSW Layer 2 (Entry Point)', 20, 40);
    ctx.fillText('HNSW Layer 1 (Skip Highway)', 20, 150);
    ctx.fillText('HNSW Layer 0 (Dense Vector Corpus)', 20, 280);

    // Draw Query Target Vector
    ctx.beginPath();
    ctx.arc(targetX, targetY, 14, 0, Math.PI * 2);
    ctx.fillStyle = 'rgba(245, 158, 11, 0.2)';
    ctx.fill();
    ctx.strokeStyle = '#f59e0b';
    ctx.lineWidth = 2;
    ctx.stroke();

    ctx.fillStyle = '#f59e0b';
    ctx.font = '11px Inter';
    ctx.fillText('Query Vector (Target Article)', targetX - 55, targetY + 30);

    // Traversal Path Nodes depending on efSearch
    const numCandidates = Math.min(state.efSearch, 64);
    document.getElementById('hnswHopsText').innerText = `Hops Evaluated: ${Math.round(numCandidates * 0.4)}`;
    document.getElementById('hnswCandidatesText').innerText = `Candidate Queue (efSearch): ${state.efSearch}`;

    // Draw nodes across layers
    let pointsLayer0 = [];
    const countL0 = 35;
    for (let i = 0; i < countL0; i++) {
      const px = 180 + (i / countL0) * (width - 320) + (Math.sin(i * 3) * 20);
      const py = 240 + (Math.cos(i * 2) * 25);
      pointsLayer0.push({ x: px, y: py, id: i });
    }

    // Connect L0 edges based on M
    ctx.strokeStyle = 'rgba(59, 130, 246, 0.15)';
    ctx.lineWidth = 1;
    for (let i = 0; i < pointsLayer0.length; i++) {
      for (let k = 1; k <= Math.min(4, state.m / 4); k++) {
        const neighbor = pointsLayer0[(i + k) % pointsLayer0.length];
        ctx.beginPath();
        ctx.moveTo(pointsLayer0[i].x, pointsLayer0[i].y);
        ctx.lineTo(neighbor.x, neighbor.y);
        ctx.stroke();
      }
    }

    // Draw L0 Nodes
    pointsLayer0.forEach((p, idx) => {
      ctx.beginPath();
      ctx.arc(p.x, p.y, 4, 0, Math.PI * 2);
      ctx.fillStyle = (idx < numCandidates * 0.5) ? '#60a5fa' : '#334155';
      ctx.fill();
    });

    // Draw Traversal Beam path from Entry (L2) -> L1 -> L0 Target
    ctx.beginPath();
    ctx.moveTo(entryX, entryY);
    ctx.lineTo(250, 140);
    ctx.lineTo(500, 240);
    ctx.lineTo(targetX - 20, targetY - 10);
    ctx.strokeStyle = (state.efSearch >= 64) ? '#34d399' : '#ef4444';
    ctx.lineWidth = 3;
    ctx.setLineDash([5, 5]);
    ctx.stroke();
    ctx.setLineDash([]);

    // Entry Point Dot
    ctx.beginPath();
    ctx.arc(entryX, entryY, 8, 0, Math.PI * 2);
    ctx.fillStyle = '#3b82f6';
    ctx.fill();
    ctx.fillStyle = '#fff';
    ctx.font = '10px Inter';
    ctx.fillText('Entry Node', entryX - 25, entryY - 14);
  }

  // Render Before vs After Article Recommendations
  function renderRecommendations(metrics) {
    const isTuned = state.efSearch >= 64 && state.routing === 'rebalanced';
    document.getElementById('recLatencyCurrent').innerText = `${metrics.p99Latency}ms`;
    
    // Articles dataset
    const highRelevanceArticles = [
      { title: 'Transformer Architectures for High-Frequency Stock Market Predictions', score: 0.94 },
      { title: 'Generative AI and Large Language Models in Algorithmic Portfolio Optimization', score: 0.91 },
      { title: 'Real-Time Vector Similarity Search in Financial Sentiment Analysis', score: 0.88 },
      { title: 'LLM Sentiment Extraction for S&P 500 Equity Volatility Forecasting', score: 0.86 }
    ];

    const lowRelevanceArticles = [
      { title: 'Introductory Python Guide for Beginners: Variables & Loops', score: 0.48 },
      { title: 'HTML5 Semantic Formatting and CSS Layout Best Practices', score: 0.42 },
      { title: 'Overview of Renewable Solar Energy Trends 2026', score: 0.38 },
      { title: 'Global Football Championship Scores & Match Summaries', score: 0.31 }
    ];

    // Current Articles (Untuned vs Tuned)
    listCurrentArticles.innerHTML = '';
    const currentList = (state.efSearch < 32) ? lowRelevanceArticles : highRelevanceArticles;
    
    currentList.forEach(art => {
      const isRel = art.score > 0.70;
      const item = document.createElement('div');
      item.className = `article-item ${isRel ? 'relevant' : 'irrelevant'}`;
      item.innerHTML = `
        <div class="article-title">${art.title}</div>
        <div class="article-score ${isRel ? 'score-high' : 'score-low'}">Cosine Sim: ${art.score}</div>
      `;
      listCurrentArticles.appendChild(item);
    });

    // Target Tuned Output (Always Ground Truth High Quality)
    listTargetArticles.innerHTML = '';
    highRelevanceArticles.forEach(art => {
      const item = document.createElement('div');
      item.className = 'article-item relevant';
      item.innerHTML = `
        <div class="article-title">${art.title}</div>
        <div class="article-score score-high">Cosine Sim: ${art.score}</div>
      `;
      listTargetArticles.appendChild(item);
    });
  }

  function updateCodeSnippet() {
    codeSnippet.innerText = `{
  "settings": {
    "index": {
      "knn": true,
      "knn.algo_param.ef_search": ${state.efSearch},
      "number_of_shards": ${state.shards},
      "number_of_replicas": 1
    }
  },
  "mappings": {
    "properties": {
      "article_vector": {
        "type": "knn_vector",
        "dimension": ${state.dim},
        "method": {
          "name": "hnsw",
          "space_type": "cosinesimil",
          "engine": "lucene",
          "parameters": {
            "m": ${state.m},
            "ef_construction": ${state.efConst}
          }
        }
      }
    }
  }
}`;
  }

  function updateChart(metrics) {
    if (!latencyRecallChart) return;
    const now = new Date().toLocaleTimeString();
    
    // Push new point
    if (latencyRecallChart.data.labels.length > 8) {
      latencyRecallChart.data.labels.shift();
      latencyRecallChart.data.datasets[0].data.shift();
      latencyRecallChart.data.datasets[1].data.shift();
    }
    
    latencyRecallChart.data.labels.push(now);
    latencyRecallChart.data.datasets[0].data.push(metrics.p99Latency);
    latencyRecallChart.data.datasets[1].data.push(metrics.recallAt10);
    latencyRecallChart.update();
  }

  // Event Handlers
  btnPresets.forEach(btn => {
    btn.addEventListener('click', (e) => {
      btnPresets.forEach(b => b.classList.remove('active'));
      const target = e.currentTarget;
      target.classList.add('active');
      const pKey = target.getAttribute('data-preset');
      const p = presets[pKey];

      state.m = p.m;
      state.efConst = p.efConst;
      state.efSearch = p.efSearch;
      state.nodes = p.nodes;
      state.shards = p.shards;
      state.routing = p.routing;
      state.traffic = p.traffic;

      // Sync slider UI controls
      sliderTraffic.value = state.traffic;
      valTraffic.innerText = `${state.traffic} QPS`;
      sliderM.value = state.m;
      valM.innerText = state.m;
      sliderEfConst.value = state.efConst;
      valEfConst.innerText = state.efConst;
      sliderEfSearch.value = state.efSearch;
      valEfSearch.innerText = state.efSearch;
      selectNodes.value = state.nodes;
      valNodes.innerText = `${state.nodes} Nodes`;
      selectShards.value = state.shards;
      valShards.innerText = `${state.shards} Shards`;
      selectRouting.value = state.routing;

      updateUI();
    });
  });

  // Slider Listeners
  sliderTraffic.addEventListener('input', (e) => {
    state.traffic = parseInt(e.target.value);
    valTraffic.innerText = `${state.traffic} QPS`;
    updateUI();
  });

  sliderCorpus.addEventListener('input', (e) => {
    state.corpus = parseInt(e.target.value);
    valCorpus.innerText = `${state.corpus} Million`;
    updateUI();
  });

  selectDim.addEventListener('change', (e) => {
    state.dim = parseInt(e.target.value);
    updateUI();
  });

  sliderM.addEventListener('input', (e) => {
    state.m = parseInt(e.target.value);
    valM.innerText = state.m;
    updateUI();
  });

  sliderEfConst.addEventListener('input', (e) => {
    state.efConst = parseInt(e.target.value);
    valEfConst.innerText = state.efConst;
    updateUI();
  });

  sliderEfSearch.addEventListener('input', (e) => {
    state.efSearch = parseInt(e.target.value);
    valEfSearch.innerText = state.efSearch;
    updateUI();
  });

  selectNodes.addEventListener('input', (e) => {
    state.nodes = parseInt(e.target.value);
    valNodes.innerText = `${state.nodes} Nodes`;
    updateUI();
  });

  selectShards.addEventListener('input', (e) => {
    state.shards = parseInt(e.target.value);
    valShards.innerText = `${state.shards} Shards`;
    updateUI();
  });

  selectRouting.addEventListener('change', (e) => {
    state.routing = e.target.value;
    updateUI();
  });

  btnReindex.addEventListener('click', () => {
    state.routing = 'rebalanced';
    state.shards = 8;
    selectRouting.value = 'rebalanced';
    selectShards.value = 8;
    valShards.innerText = '8 Shards';
    updateUI();
  });

  btnRunQuery.addEventListener('click', () => {
    state.queryText = inputQuery.value;
    updateUI();
  });

  btnCopyCode.addEventListener('click', () => {
    navigator.clipboard.writeText(codeSnippet.innerText);
    btnCopyCode.innerHTML = '<i class="fa-solid fa-check"></i> Copied!';
    setTimeout(() => {
      btnCopyCode.innerHTML = '<i class="fa-solid fa-copy"></i> Copy JSON';
    }, 2000);
  });

  // Initial Load
  initChart();
  updateUI();
  window.addEventListener('resize', drawHnswGraph);
});
