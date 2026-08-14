### 🏗️ High-Level Architectural Flow (HLD)

```
 [ External SaaS Clients ]
 (Basic / Pro / Enterprise)
            │
            │  1. HTTP POST Request (API Key in Header)
            ▼
┌────────────────────────────────────────────────────────────────────────┐
│                        AMAZON API GATEWAY                              │
│                                                                        │
│   ┌────────────────────────────────────────────────────────────────┐   │
│   │ 2. API KEYS & USAGE PLANS (Tiered Throttling at Edge)          │   │
│   │    • Checks Tenant Tier (Rate Limit / Burst Limit)             │   │
│   │    • Exceeded limit? ──> ❌ 429 Too Many Requests (Blocked)     │   │
│   └───────────────────────────────┬────────────────────────────────┘   │
│                                   │ Passed Throttling                 │
│                                   ▼                                    │
│   ┌────────────────────────────────────────────────────────────────┐   │
│   │ 3. REQUEST VALIDATORS & JSON SCHEMA                            │   │
│   │    • Checks required JSON body fields & parameter types        │   │
│   │    • Rejects prompts exceeding token/character limits          │   │
│   │    • Invalid payload? ──> ❌ 400 Bad Request (Blocked)          │   │
│   └───────────────────────────────┬────────────────────────────────┘   │
└───────────────────────────────────┼────────────────────────────────────┘
                                    │ 4. Valid Request Only
                                    ▼
                         ┌────────────────────┐
                         │    AWS LAMBDA      │
                         │ (Business Logic)   │
                         └──────────┬─────────┘
                                    │ 5. Invoke Model
                                    ▼
                         ┌────────────────────┐
                         │   AMAZON BEDROCK   │
                         │ (Foundation Model) │
                         └────────────────────┘
```

### 🔄 End-to-End Workflow Steps

1. **Client Request:** The external customer sends a request to the text analysis API endpoint, including their assigned **API Key** in the header.
    
2. **Tiered Throttling (API Gateway Usage Plans):**
    
    - API Gateway matches the API key to a specific **Subscription Tier** (e.g., _Free: 10 req/sec_, _Enterprise: 1,000 req/sec_).
        
    - If a customer spikes traffic beyond their plan's rate or burst limit, API Gateway instantly drops the request with a `429 Too Many Requests` error. **Lambda and Bedrock are never called.**
        
3. **Payload Validation (JSON Schema & Method Validation):**
    
    - API Gateway inspects the request body against a predefined **JSON Schema**.
        
    - If required fields are missing or if the prompt length exceeds predefined limits, API Gateway immediately rejects the request with a `400 Bad Request` error.
        
4. **Compute Execution (AWS Lambda):**
    
    - Once a request successfully passes both validation and throttling at the edge, it is forwarded to AWS Lambda.
        
5. **Model Inference (Amazon Bedrock):**
    
    - Lambda calls the Amazon Bedrock `InvokeModel` or `Converse` API to perform text classification and sentiment analysis safely.
        

### 💡 Why These Two Choices Are the Gold Standard

| **Feature**            | **Feature Choice**             | **Why It Solves the Scenario**                                                                                                                            |
| ---------------------- | ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Request Validation** | **JSON Schema in API Gateway** | Validates payloads _at the API Gateway edge_. Bad or oversized prompts are rejected **before** compute resources (Lambda/Bedrock) are billed or consumed. |
| **Traffic Control**    | **API Keys & Usage Plans**     | Applies plan-based throttling (Rate/Burst limits) per customer. Prevents any single tenant from overloading Bedrock endpoints during traffic spikes.      |