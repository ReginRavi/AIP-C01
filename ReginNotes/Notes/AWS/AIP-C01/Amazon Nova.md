**Amazon Nova** is AWS's proprietary family of next-generation foundation models built in-house and served natively through **Amazon Bedrock**.

### Core Purpose

The primary purpose of Amazon Nova is to provide enterprise-grade **multimodal intelligence** (text, vision, video, and audio) at **industry-leading price-performance**. Rather than relying solely on third-party FMs (such as Anthropic Claude or Meta Llama), AWS built Nova to give developers low-latency, scalable, and highly customizable models deeply optimized for AWS infrastructure and native generative AI workflows.

### Categories & Types of Amazon Nova Models

Amazon Nova models are grouped into three functional categories: **Understanding Models** (text & visual input to text), **Creative Content Models** (text/image input to media), and **Speech Models**.

#### 1. Multimodal Understanding Models

|Model|Modality|Context Window|Key Purpose & Best Use Cases|
|---|---|---|---|
|**Nova Micro**|Text-only|128K tokens|**Ultra-low latency & lowest cost.** Ideal for fast text translation, classification, summarization, and simple coding tasks.|
|**Nova Lite**|Multimodal (Text, Image, Video) → Text|300K tokens|**Fast, affordable multimodal processing.** Ideal for visual Q&A, document extraction, real-time chatbots, and analyzing video clips up to 30 minutes.|
|**Nova Pro**|Multimodal (Text, Image, Video) → Text|300K tokens|**High reasoning & agentic capability.** Optimized for complex function/tool calling, large codebase analysis, RAG pipelines, and financial document synthesis.|
|**Nova Premier**|Multimodal (Text, Image, Video) → Text|Max context|**Flagship frontier reasoning.** Designed for the most complex multi-step reasoning tasks and for serving as a "teacher model" to distill smaller custom models.|

#### 2. Creative Content Generation Models

- **Amazon Nova Canvas:** Image generation model designed to create high-quality studio images from text or reference images, with support for visual styling, background replacement, and color matching.

- **Amazon Nova Reel:** Video generation model that produces short, high-definition cinematic video clips from text prompts or static reference images for creative, marketing, and media applications.

#### 3. Speech / Voice Models

- **Amazon Nova Sonic:** Low-latency, bi-directional speech model built for interactive, human-like voice applications (speech-in to speech/text-out).

### Key Enterprise Features

- **Model Distillation & Customization:** You can fine-tune Nova models on proprietary enterprise data or use **Nova Pro** as a teacher model to train lightweight custom **Nova Micro** or **Lite** variants.
- **Native RAG & Function Calling:** Built to excel at structured function calling (Berkeley Function Calling Leaderboard benchmarks) and Retrieval-Augmented Generation (RAG).
- **Seamless Bedrock Integration:** Accessible via standard Bedrock `InvokeModel` and `Converse` APIs with cross-region inference support.

Are you preparing for the AWS AIP-C01 exam or deciding between Amazon Nova and third-party models (like Claude or Llama) for a specific architecture?

### Multimodal Understanding Models

- **Amazon Nova Micro (Text-Only)**

    - **Primary Use Case:** High-volume, latency-sensitive, text-only tasks where cost must be minimized.

    - **Enterprise Scenarios:** High-throughput text classification, real-time sentiment analysis, uniform product description generation for e-commerce catalogs, fast language translation, and lightweight email/ticket summarization.

- **Amazon Nova Lite / Nova 2 Lite (Multimodal: Text, Image, Video)**
    
    - **Primary Use Case:** Everyday multimodal processing requiring speed, low cost, and visual reasoning.

    - **Enterprise Scenarios:** Automated document/receipt data extraction, visual Q&A on charts/graphs, analyzing up to 30-minute video clips for key moments, customer service chatbots, and general business automation.

- **Amazon Nova Pro / Nova 2 Pro (Advanced Reasoning)**
    
    - **Primary Use Case:** Complex, production-grade enterprise tasks demanding high reasoning, tool/function calling, and multi-step logic.

    - **Enterprise Scenarios:** Complex RAG pipelines over heterogeneous documents, deep financial analysis, agentic coding and large codebase reviews (up to 15,000 lines), and long-range workflow orchestration.

- **Amazon Nova Premier (Frontier Intelligence & Distillation)**
    
    - **Primary Use Case:** Top-tier reasoning over massive context windows (1M tokens) and model distillation.

    - **Enterprise Scenarios:** Legal contract auditing across massive document sets, multi-step strategic planning, and acting as a **Teacher Model** to distill smaller, domain-specific Nova Micro/Lite models at lower costs.

### Creative Content Generation Models

- **Amazon Nova Canvas (Text/Image $\rightarrow$ Studio Image)**
    
    - **Primary Use Case:** Generating studio-quality visual assets at scale with built-in content moderation and watermarking.

    - **Enterprise Scenarios:** E-commerce product visualization, marketing/advertising campaign generation, automated background removal/replacement, and brand-aligned image creation.

- **Amazon Nova Reel (Text/Image $\rightarrow$ Video)**
    
    - **Primary Use Case:** Generating short, high-definition promotional videos and animated visual media.

    - **Enterprise Scenarios:** Social media video marketing clips, dynamic product advertisement videos, corporate training animations, and video content prototyping.

### Speech & Interactive Voice Models

- **Amazon Nova Sonic / Nova 2 Sonic (Speech-to-Speech)**
    
    - **Primary Use Case:** Low-latency, human-like voice conversations that perceive tone, inflection, and speech pacing.

    - **Enterprise Scenarios:** Interactive IVR call center voice agents, real-time voice assistants with seamless topic-switching, and multilingual conversational AI applications.

### Agentic & Specialist Services

- **Amazon Nova Act**
    
    - **Primary Use Case:** Automated browser-based computer use and UI interaction.

    - **Enterprise Scenarios:** Automating repetitive web UI tasks (e.g., filling CRM fields, submitting health insurance claims, end-to-end web software QA testing) with ~90% workflow reliability.

- **Amazon Nova Multimodal Embeddings**
    
    - **Primary Use Case:** Creating unified vector embeddings across text, images, video, and audio.

    - **Enterprise Scenarios:** Cross-modal vector search (e.g., searching video archives using natural language queries or finding similar products using image inputs in RAG vector databases).


### 💡 AIP-C01 Exam Decision Matrix

| **Exam Keyword / Requirement**                                       | **Target Amazon Nova Model / Feature** |
| -------------------------------------------------------------------- | -------------------------------------- |
| _"Lowest cost, text-only, fast translation or classification"_       | **Nova Micro**                         |
| _"Fast multimodal document/video extraction at 75% lower cost"_      | **Nova Lite**                          |
| _"Complex function calling, agentic coding, RAG workhorse"_          | **Nova Pro**                           |
| _"Massive 1M token context, teacher model for Bedrock distillation"_ | **Nova Premier**                       |
| _"Studio images with watermarking and brand controls"_               | **Nova Canvas**                        |
| _"Short HD video clip generation from text prompts"_                 | **Nova Reel**                          |
| _"Real-time conversational voice assistant detecting tone/pacing"_   | **Nova Sonic**                         |
| _"Automating web UI tasks, browser scraping, or CRM updates"_        | Nova Act                               |
### Exam Traps & Common Scenarios (AIP-C01)

- **Exam Trap 1: Bedrock vs. SageMaker JumpStart for Llama**
    
    - _Rule:_ If the question asks for _"Llama with minimal operational overhead and pay-per-token billing"_, choose **Amazon Bedrock**. If it requires _"deploying customized Llama weights on dedicated EC2/Inferentia infrastructure with full control"_, choose **Amazon SageMaker JumpStart**.
        
- **Exam Trap 2: Model API Consistency**
    
    - _Rule:_ Moving between Nova, Claude, and Llama on Bedrock does **not** require rewriting payload format adapters. Use the **Bedrock Converse API** (`converse` / `converse_stream`), which provides a unified interface for system prompts, messages, and tool configuration across all providers.
        
- **Exam Trap 3: Cost Optimization Strategies**
    
    - _Rule:_ For non-real-time bulk processing (e.g., overnight document indexing), do not use On-Demand. Select **Amazon Bedrock Batch Inference** for a **50% cost discount** across supported models (Nova, Claude, Llama).
        
    - _Rule:_ For variable request volumes with mixed simple and complex prompts, select **Amazon Bedrock Intelligent Prompt Router** to route traffic dynamically between Lite and Pro tiers within the same model family.