**Amazon Bedrock Batch Inference** is a powerful feature designed for processing large volumes of asynchronous, non-real-time machine learning and generative AI workloads cost-effectively.

Instead of invoking models synchronously (which can lead to latency bottlenecks, throttling, and higher bills for bulk data), batch inference allows you to submit a massive set of prompts at once, let Amazon Bedrock process them asynchronously in the background, and output the results directly to an Amazon S3 bucket.

### 1. Key Architectural Benefits

- **50% Cost Savings:** Batch inference jobs are priced at a **50% discount** compared to standard on-demand inference rates for supported foundation models.

- **No Throttling or Rate Limit Errors:** Because jobs run asynchronously and are managed by AWS infrastructure queues, you don’t have to implement complex back-off or retry loops for rate limits (`ThrottlingException`).

- **Ideal for Asynchronous Tasks:** Perfect for workloads where results can wait minutes or hours, such as document classification, bulk summarization (e.g., call center transcripts), data enrichment, and model evaluations.

### 2. How It Works (Workflow)

1. **Prepare Input Data (JSONL):** Format your prompts into a JSON Lines (`.jsonl`) file. Each line contains a unique identifier (`recordId`) and the standard model input payload matching the target foundation model's API specifications.
    
    JSON
    
    ```
    {"recordId": "rec-001", "modelInput": {"anthropic_version": "bedrock-2023-05-31", "max_tokens": 512, "messages": [{"role": "user", "content": "Summarize this document..."}]}}
    ```

1. **Upload to Amazon S3:** Upload your input `.jsonl` file to an Amazon S3 bucket.

2. **Configure IAM Permissions:** Ensure you have an IAM service role that permits Amazon Bedrock to assume the role, read the input data from your S3 bucket, and write results back to your destination S3 bucket.

3. **Submit the Job:** Call the Bedrock API (via `CreateModelInvocationJob`, AWS CLI, or SDK like `boto3`), pointing it to your input S3 URI and output S3 destination.

4. **Retrieve Results:** Once the job status changes to `Completed`, download the output `.jsonl` file from your specified S3 folder to review responses.


### 3. Comparison: Batch Inference vs. On-Demand vs. Provisioned Throughput

|**Feature**|**On-Demand Inference**|**Batch Inference**|**Provisioned Throughput**|
|---|---|---|---|
|**Response Time**|Real-time (milliseconds)|Asynchronous (minutes to hours)|Real-time (guaranteed capacity)|
|**Pricing Model**|Standard pay-per-token|**50% off** standard token rates|Hourly commitment (Model Units)|
|**Primary Use Case**|Chatbots, user-facing apps, real-time API calls|Bulk document processing, dataset enrichment, evaluation pipelines|High-scale, predictable, enterprise-grade production workloads|