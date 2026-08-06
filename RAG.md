RAG is a framework that enhances the LLM responses using the external knowledge.
During ingestion the documents are chunked , converted in to embeddings and stored in a vector database. when a user ask a question, the query is converted in to a embeddings and a similarity search retrieves the most relevant chunks.
These chucks are added to the prompt as context, and the LLM generated a grounded response based on both user query and retrieved information. This reduces hallucination and enable answers from up to date private enterprise data

The end-to-end process of RAG is typically broken down into two main phases: **Data Ingestion (Offline Processing)** and **Inference / Query Processing (Online Execution)**.


### Phase 1: Data Ingestion (Offline Pipeline)

Before a user ever asks a question, your internal documents, knowledge bases, or databases must be prepared and indexed.

1. **Document Loading:** Raw source data (such as PDFs, text files, FAQs, or databases) is ingested from storage repositories like Amazon S3.
    
2. **Chunking (Text Splitting):** Large documents are broken down into smaller, manageable segments (chunks) so that embeddings capture precise contextual meanings rather than broad, diluted concepts.
    
3. **Embedding Generation:** Each chunk is passed through an embedding model (such as Amazon Titan Embeddings) which transforms the text into numerical vectors (high-dimensional arrays).
    
4. **Vector Database Storage:** The generated vectors, along with their original text chunks and metadata, are stored in a vector database (e.g., Amazon OpenSearch Service, Amazon Aurora with `pgvector`, or Pinecone).
    

### Phase 2: Inference & Execution (Online Pipeline)

When a user submits a query, the live RAG pipeline executes the following stages in real-time:

1. **User Query Input:** The user submits a natural language query or prompt to the application.
    
2. **Query Vectorization:** The user's query is converted into a vector embedding using the same embedding model used during ingestion.
    
3. **Similarity Search (Retrieval):** The query vector is sent to the vector database to perform a similarity search (such as Approximate Nearest Neighbors / ANN using HNSW) against the indexed document vectors.
    
4. **Context Assembly:** The vector database returns the top-$K$ most relevant text chunks (context) that match the user's intent.
    
5. **Prompt Augmentation:** The application combines the original user prompt with the retrieved external documents into an enhanced prompt template. This provides the LLM with grounded facts:
    
    - _Example Template:_ `"Using the context provided below, answer the user's question: [Retrieved Chunks] -> [User Query]"`
        
6. **LLM Generation:** The augmented prompt is sent to the Foundation Model (e.g., Anthropic Claude via Amazon Bedrock), which synthesizes the final, accurate response based specifically on the retrieved context, significantly minimizing hallucinations.

Types of Chunking 

In Retrieval-Augmented Generation (RAG), **chunking** is the process of breaking down large documents into smaller text segments so that embedding models can accurately capture their semantic meaning. Choosing the right chunking strategy depends on your document layout, target model context windows, and retrieval requirements.

### 1. Fixed-Size Chunking

- **How it works:** Splits text into uniform segments based on a fixed character or token count (e.g., 500 characters), often with a specified overlap (e.g., 50 characters) to avoid cutting context abruptly across boundaries.

- **When to use:**
    - Quick prototyping or baseline testing when speed is preferred over high precision.
    - Flat, unstructured text files without distinct structural headers or logical divisions.
    - Uniformly structured datasets (such as logs or simple text dumps).

### 2. Sentence / Recursive Chunking

- **How it works:** Recursively splits text using a hierarchy of natural boundaries (e.g., paragraphs, then sentences, then words) until the resulting chunk meets the target token limit.
    
- **When to use:**

    - General-purpose RAG applications involving prose, articles, blogs, or user documentation.
    
    - Maintaining complete linguistic sentences to prevent cutoff mid-thought while keeping chunks reasonably sized.
    

### 3. Document-Based / Structural Chunking

- **How it works:** Uses format-specific metadata or structural indicators (such as Markdown headers `#`, HTML tags `<div>`, or PDF layout elements) to divide text into logical sections.

- **When to use:**
    - Structured or semi-structured documents like technical documentation, API specifications, user manuals, or Markdown files.
    - Use cases where preserving the section title or hierarchy along with the content is critical for accuracy.


### 4. Semantic Chunking

- **How it works:** Monitors the semantic distance between consecutive sentences using an embedding model. A new chunk boundary is created only when the cosine similarity drops significantly, signaling a change in topic.

- **When to use:**
    - Complex, multi-topic documents (e.g., research papers, financial filings, legal contracts) where topic shifts do not follow strict paragraph rules.
    - Scenarios where maintaining high search precision and thematic consistency within each chunk is paramount.


### 5. Parent-Child / Hierarchical Chunking

- **How it works:** Creates two levels of chunks: small "child" chunks (e.g., 100–200 tokens) for fine-grained similarity matching during vector search, and larger "parent" chunks (e.g., 1,000 tokens) that are retrieved and passed to the LLM to provide full context.
    
- **When to use:**
    
    - Documents where precise retrieval requires small units, but meaningful generation by the LLM requires surrounding context.
        
    - Mitigating the trade-off between search precision and prompt context completeness.
        

### Summary Selection Matrix

|**Strategy**|**Speed / Complexity**|**Context Preservation**|**Best Use Case**|
|---|---|---|---|
|**Fixed-Size**|Fast / Low|Low|Quick prototypes, unstructured raw text dumps|
|**Recursive**|Moderate / Low|Medium-High|Articles, blogs, general text|
|**Structural**|Moderate / Medium|High|Markdown docs, technical manuals, HTML pages|
|**Semantic**|Slow / High|Very High|Research papers, legal/financial documents|
|**Parent-Child**|Moderate / Medium|High|High-precision vector search needing rich LLM context|