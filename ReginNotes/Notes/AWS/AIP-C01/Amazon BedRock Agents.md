Generative AI -> Agentic AI

Agentic AI Framework
Amazon Bedrock coreAgent

[FAQ](https://aws.amazon.com/bedrock/agentcore/faqs/)

### Agentic framework 
Agent is 
1. Goal-oriented
2. Resourceful
3. Remembers
4. Learn and adapt
5. Escalates
#### Agents has
	Tools
	LLM
	Memory

Tools - API
LLM - Reasoning and Judgement. 
Memory - How much memory you need ai to remember

![[BedRock Agent.png|697]]

##### Open-source Frameworks for building AI agents

1. Crewai
2. LangGRAPH
3. Langchain
4. ..
5. ....
6. ...

##### Bedrock core provides the essentials Building blocks

Context 
- Role
- Tools,APIs
- Data
- Memory
Intelligent
- Models
- Thinking modes
Trust
- Identity and Security
- Guardrails

Github : https://github.com/awslabs/agentcore-samples

Auto create ECR
When you deploy an agent to **Amazon Bedrock AgentCore** using the container deployment method (for custom runtimes or complex dependencies), it requires an Amazon Elastic Container Registry (ECR) repository to store your agent's container image.

During the configuration process (`agentcore configure`), the setup wizard will ask for an "ECR Repository URI". **Auto-create ECR** is an option within this setup wizard. If you press "Enter" without providing an existing ECR Repository URI, the AgentCore SDK will automatically create a new ECR repository for you.

This streamlines the deployment process, as you don't need to manually set up the registry beforehand. When you subsequently run `agentcore launch`, it builds the container image and pushes it to this auto-created ECR repository before deploying it to the AgentCore Runtime.

**Communication:**
	with in AWS - IAM role
	with External - JWT
