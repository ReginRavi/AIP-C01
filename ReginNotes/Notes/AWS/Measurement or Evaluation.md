
Evaluating Retrieval-Augmented Generation (RAG) systems requires assessing two distinct components that operate sequentially: **the Retriever** (vector store and search algorithm) and **the Generator** (the Foundation Model).

For the **AWS Certified Generative AI Developer - Professional (AIP-C01)** exam and production systems, RAG evaluation is broken down into specific metric frameworks, diagnostic use cases, and AWS Bedrock platform capabilities.

### 1. The Core Metrics Framework

RAG evaluation metrics fall into two primary paradigms: **Referenceless Metrics** (evaluating without a ground-truth answer) and **Reference-Based Metrics** (comparing against a labeled golden dataset).

```
                            [ RAG SYSTEM EVALUATION ]
                                       |
           +---------------------------+---------------------------+
           |                                                       |
   [RETRIEVER METRICS]                                    [GENERATOR METRICS]
   (Evaluates Search & Chunks)                             (Evaluates Output Quality)
           |                                                       |
   • Context Relevancy                                     • Faithfulness / Groundedness
   • Context Recall (Reference)                            • Answer Relevancy
   • Context Precision (Reference)                         • Answer Correctness (Reference)
```

#### A. The RAG Triad (Referenceless Metrics)

The **RAG Triad** is the industry-standard referenceless framework. It allows continuous evaluation on live user queries without requiring human-labeled ground truth.

1. **Context Relevancy (Retriever Metric):**

    - **What it measures:** The proportion of retrieved context chunks that are directly relevant to the user query.

    - **Formula Idea:** $\frac{\text{Number of Relevant Sentences in Context}}{\text{Total Sentences in Retrieved Chunks}}$

2. **Faithfulness / Groundedness (Generator Metric):**
    
    - **What it measures:** Whether all claims in the generated answer can be mathematically or logically inferred **solely** from the retrieved context.

    - **Target:** Hallucination detection.

    - **Formula Idea:** $\frac{\text{Number of Verified Output Statements}}{\text{Total Output Statements}}$
 
3. **Answer Relevancy (Generator / Prompt Metric):**
    
    - **What it measures:** How directly the generated answer addresses the original user prompt, regardless of whether the answer is factually correct.

    - **Target:** Instruction following and prompt adherence.


#### B. Reference-Based Metrics (Requires Golden Datasets)

When you have a benchmark dataset containing human-verified answers (`expected_output`), you can measure deeper retrieval characteristics:

- **Context Recall:** Measures if the retriever brought back _all_ facts needed to answer the query (comparing retrieved chunks against `expected_output`).

- **Context Precision:** Measures if the most relevant chunks were ranked higher in the search results than noise chunks.

- **Answer Correctness:** Measures exact/semantic overlap between generated output and `expected_output` (using metrics like ROUGE, BLEU, BERTScore, or LLM-as-a-Judge).

### 2. Practical Use Cases & Root-Cause Diagnostics

In practice and on the exam, evaluation metrics act as a diagnostic tree to identify system bottlenecks.

|**Evaluation Finding**|**Root Cause**|**Recommended System Fix**|
|---|---|---|
|**Low Context Relevancy**|The retriever returns noisy or unrelated text chunks.|• Increase $k$-NN cutoff or tune vector thresholds.<br><br>  <br><br>• Implement hybrid search (BM25 + vector embeddings).<br><br>  <br><br>• Optimize text chunk size or switch embedding models.|
|**Low Context Recall**|Chunks are missing critical facts needed to fully answer.|• Increase `top-k` retrieved documents.<br><br>  <br><br>• Switch to Parent-Child/Hierarchical chunking.<br><br>  <br><br>• Use Query Rewriting/Expansion.|
|**Low Faithfulness** (High Hallucination)|The LLM generates facts outside the provided context.|• Strengthen system prompts (_"Answer using ONLY the context provided..."_).<br><br>  <br><br>• Reduce model temperature ($\approx 0.0$).<br><br>  <br><br>• Switch to a stronger reasoning model (e.g., Nova Pro, Claude Sonnet).|
|**Low Answer Relevancy**|The answer is grounded in context but strays from user intent.|• Improve prompt template structure or provide few-shot examples.<br><br>  <br><br>• Add explicit formatting guidelines.|

### 3. AWS Bedrock Model Evaluations (AIP-C01 Focus)

Amazon Bedrock provides native evaluation mechanisms for RAG systems and Foundation Models.

```
                            [ BEDROCK EVALUATION TYPES ]
                                         |
         +-------------------------------+-------------------------------+
         |                               |                               |
[AUTOMATIC (PROGRAMMATIC)]      [LLM-AS-A-JUDGE]              [HUMAN EVALUATION]
• Deterministic metrics         • Automated LLM judge         • Amazon A2I / Workforce
• ROUGE, BLEU, BERTScore        • Faithfulness, Correctness,   • Subjective quality,
• Fast, cheap                   • Refusal, Harmfulness          • Brand voice alignment
```

1. **Automatic / Programmatic Evaluations:**
    
    - Uses predefined deterministic algorithms against reference datasets.

    - **ROUGE-1 / ROUGE-L:** Measures n-gram recall (best for **Summarization**).

    - **BLEU:** Measures n-gram precision (best for **Translation**).

    - **BERTScore:** Uses contextual embeddings for semantic similarity.
  
2. **LLM-as-a-Judge (Bedrock Managed):**
    
    - Uses an automated LLM to score RAG outputs and Knowledge Bases.

    - Native metrics include **Faithfulness**, **Correctness**, **Completeness**, and Responsible AI dimensions (**Harmfulness**, **Answer Refusal**).

    - Supports **BYOI (Bring Your Own Inference)** to evaluate non-Bedrock RAG pipelines.

3. **Human Evaluations:**
    
    - Used for subjective dimensions like tone, style, and brand voice.

    - Uses **Amazon A2I (Augmented AI)**, internal workforce, or AWS-managed expert teams.


### 4. AIP-C01 Exam Tricks & Scenario Traps

- **Trap 1: "Which metric to fix hallucinations?"**
    
    - _Rule:_ Hallucination is always tied to **Faithfulness** (or Groundedness). If an application outputs plausible but false statements, Faithfulness is low, pointing to a generator/LLM issue.

- **Trap 2: ROUGE vs. BLEU**
    
    - _Rule:_ **ROUGE** = Summarization (Recall-oriented). **BLEU** = Translation (Precision-oriented). If an exam question asks for automated evaluation of a document summarizer against ground truth, pick ROUGE.

- **Trap 3: Ground Truth Availability**
    
    - _Rule:_ If the scenario states **"No ground truth answers exist for live user queries,"** select **RAG Triad metrics** (Context Relevancy, Faithfulness, Answer Relevancy). If **"A labeled evaluation set exists,"** select reference-based metrics (Context Recall, Precision).

- **Trap 4: Human-in-the-Loop for Subjective Voice**
    
    - _Rule:_ Automated metrics (BLEU, ROUGE) cannot reliably score subjective constraints like "adherence to corporate brand tone." Select **Amazon Bedrock Human Evaluation** (or Amazon A2I) for subjective human feedback.

- **Trap 5: Bedrock Knowledge Base Evaluations**
    
    - _Rule:_ You can evaluate Knowledge Base storage/retriever parameters _separately_ from the end-to-end Retrieve & Generate pipeline using Bedrock Evaluation jobs. Pick **RAG Retrieval Evaluation** when testing chunking/top-$k$ changes, and **RAG Retrieve & Generate Evaluation** when testing prompt/LLM changes.

________________

### 1. SageMaker Model Evaluation Capabilities

Amazon SageMaker evaluates both **traditional machine learning models** and **Foundation Models (FMs / LLMs)** through **Amazon SageMaker Clarify**. For Generative AI, evaluation can be executed via the SageMaker Studio UI, SageMaker Processing Jobs, or the open-source **`fmeval`** (Foundation Model Evaluation) Python SDK.

#### Core Capabilities

- **Evaluate Models Anywhere:** Evaluates models hosted on SageMaker Endpoints, SageMaker JumpStart, Hugging Face, or external endpoints hosted outside AWS.
    
- **Automatic & Human Evaluation:** Supports algorithmic benchmark runs using built-in or custom prompt datasets, as well as human review teams.
    
- **MLOps Pipeline Integration:** Embeds directly into **SageMaker Pipelines** for automated regression testing and evaluation gates during model fine-tuning.
    

### 2. Evaluation Metrics Categories

SageMaker Clarify divides metrics into **Foundation Model (LLM) Metrics** and **Classical Machine Learning / Bias Metrics**.

|Category|Metric / Dimension|What It Measures|Target Task / Scenario|
|---|---|---|---|
|**FM Evaluation**|**Accuracy & Factual Knowledge**|Compares model response against target answers using exact match, ROUGE, BLEU, or BERTScore.|Q&A, Document Summarization, Translation.|
|**FM Evaluation**|**Toxicity & Stereotyping**|Detects toxic, abusive, profanity-laden, or biased content in generated text.|Customer service, public-facing chatbots.|
|**FM Evaluation**|**Semantic Robustness**|Measures changes in model performance when minor perturbations (typos, case changes) are introduced into prompts.|Real-world noisy user inputs.|
|**Explainability**|**SHAP (Shapley Additive exPlanations)**|Calculates feature attribution scores to quantify the impact of each input feature on a prediction.|Tabular ML models, Credit scoring, Fraud detection.|
|**Fairness / Bias**|**Disparate Impact & Statistical Parity**|Compares outcome probabilities across protected demographic groups.|Regulatory compliance, hiring models, loan approvals.|

### 3. SageMaker Evaluation vs. Bedrock Evaluation (AIP-C01 Core Distinction)

Knowing when to choose **SageMaker Clarify** over **Amazon Bedrock Model Evaluation** is a major decision point in the AIP-C01 exam.

|Dimension|SageMaker Clarify FM Evaluation|Amazon Bedrock Model Evaluation|
|---|---|---|
|**Model Hosting**|Any model (SageMaker Endpoints, SageMaker JumpStart, Hugging Face, external servers).|Models hosted natively within Amazon Bedrock (Claude, Nova, Llama on Bedrock).|
|**Custom Model Weights**|Evaluates fine-tuned custom weights deployed on dedicated EC2 / Inferentia instances.|Evaluates Bedrock base models or Bedrock custom fine-tuned models.|
|**Human Evaluation Engine**|Integrated with **SageMaker Ground Truth** (Private workforce or AWS managed workforce).|Integrated with **Amazon A2I (Augmented AI)** or managed workforce.|
|**MLOps & Automation**|Native step inside **SageMaker Pipelines** for automated CI/CD model deployment gates.|Event-driven or scheduled via AWS Lambda / EventBridge calling Bedrock evaluation APIs.|
|**Open-Source Code**|Uses the open-source **`fmeval`** Python SDK for local or hybrid evaluation.|Managed API / Console execution.|

### 4. Primary Use Cases

- **Pre-Deployment Model Selection:** Evaluating multiple open-source models (e.g., Llama 3, Mistral) from SageMaker JumpStart on a custom domain dataset before committing to fine-tuning.

- **Automated Fine-Tuning Gatekeeper:** Running SageMaker Clarify inside a SageMaker Pipeline to evaluate a fine-tuned model against a baseline; if toxicity increases or factual accuracy drops, the pipeline halts deployment.

- **Regulatory Compliance & Fairness Auditing:** Generating comprehensive PDF audit reports detailing model bias, feature importance, and disparate impact for financial or healthcare regulators.


### 5. AIP-C01 Exam Tricks & Scenario Traps

- **Trap 1: Evaluating Open-Weights or Self-Hosted Models**

    - _Rule:_ If an exam question asks to evaluate a model hosted on a **SageMaker Endpoint**, **Hugging Face Hub**, or **on-premises**, **Bedrock Evaluation is wrong**. Select **SageMaker Clarify** or the **`fmeval`** library.

- **Trap 2: MLOps Integration (CI/CD Pipelines)**

    - _Rule:_ If the scenario involves an automated training pipeline built on **SageMaker Pipelines** that requires evaluation before registering a model in the SageMaker Model Registry, choose **SageMaker Clarify**.

- **Trap 3: Feature Importance & Explainability**

    - _Rule:_ Bedrock Model Evaluation does _not_ offer SHAP feature attribution. If a question mentions _"understanding feature importance for tabular models or input tokens"_, select **SageMaker Clarify**.

- **Trap 4: Human-in-the-Loop Workforce Services**

    - _Rule:_ Pay attention to the human workforce service paired with the evaluation tool. **SageMaker Clarify FM Evaluation uses SageMaker Ground Truth**, whereas **Bedrock Evaluation uses Amazon A2I (Augmented AI)**.

- **Trap 5: Perturbation & Semantic Robustness**

    - _Rule:_ If a scenario tests how robust a model is against typos, spelling errors, or slight wording changes, look for **Semantic Robustness in SageMaker Clarify**.


Would you like to walk through a sample AIP-C01 scenario question comparing SageMaker Clarify and Amazon Bedrock evaluation workflows?

[SageMaker Clarify Foundation Model Evaluation](https://www.youtube.com/watch?v=9X2oDkOBYyA) This video provides an overview of how Amazon SageMaker Clarify evaluates foundation models for accuracy, bias, and toxicity, directly reinforcing the AIP-C01 evaluation concepts discussed above.

[](https://www.youtube.com/watch?v=9X2oDkOBYyA)

[

![](https://www.gstatic.com/images/branding/productlogos/youtube/v9/192px.svg)

AWS re:Invent 2023 - Accelerate foundation model evaluation with Amazon SageMaker Clarify (AIM367)

AWS Events · 4.8K views

](https://www.youtube.com/watch?v=9X2oDkOBYyA)[Open in AWS re:Invent 2023 - Accelerate foundation model evaluation with Amazon SageMaker Clarify (AIM367)](https://www.youtube.com/watch?v=9X2oDkOBYyA)

![](https://i.ytimg.com/vi/9X2oDkOBYyA/maxresdefault.jpg)

![](https://www.gstatic.com/images/branding/productlogos/youtube/v9/192px.svg)
Perplexity - predict text /fluency of the translation 
Accuracy - Classification of text

BERT score - embedding based - metric , evaluate the meaning of the generated text rather than just two exact word matches.

BLEU Score - Measures n-gram(Word/phrase) overlap
* Primarily used for Machine translation . Sensitive to word differences
* Less effective in capturing meaning 

F1 Score
* Commonly used for classification and some QA tasks
* Measures precision and recall
* 