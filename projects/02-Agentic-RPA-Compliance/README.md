# Project 02: RAG-Driven Agentic RPA Compliance Gateway
**Part of the `Azure-Cloud-Journey` Repository**

## 1. System Overview
This project implements an enterprise-grade, high-concurrency Anti-Money Laundering (AML) interception gateway. It addresses the semantic blindness and UI fragility of traditional rule-based Robotic Process Automation (RPA). By decoupling the cognitive decision-making layer from the physical execution layer, the system intercepts sophisticated "smurfing" fraud tactics at the API ingress point.

## 2. Core Architecture (The Asymmetric Funnel)
The system architecture forces data through four highly isolated physical tiers:

1. **Ingress Tokenization (Privacy by Design):** We execute an embedded C# script at the API gateway to perform dynamic MD5 hashing. The system strips all Personally Identifiable Information (PII) before routing the payload to the AI engine. 
2. **Asymmetric ML Engine (iForest + SVM):** We deploy Isolation Forest (iForest) to handle broad anomaly sniffing, instantly clearing 95% of routine traffic. The system restricts Support Vector Machine (SVM) hard-margin cuts strictly to the 5% flagged outliers. This setup avoids unnecessary compute burn on normal traffic.
3. **Cognitive Compliance (RAG):** Black-box probability scores are legally void in financial compliance. We implemented a "Quality over Quantity" strategy for the RAG knowledge base. Initial stress tests revealed that massive document retrieval spikes gateway latency. To maintain sub-second execution, we strictly limited the vector database to core AML statutes, prioritizing high-fidelity evidence over broad contextual noise.
4. **API-First Execution:** UiPath bots completely bypass UI scraping. The Agentic brain triggers asynchronous `HTTP POST /api/lockBusiness` requests, commanding the core banking system to freeze assets in milliseconds.

## 3. Performance & Benchmarks
We stress-tested the pipeline using a simulated dataset of 10,000 transactions (mixing benign traffic with camouflaged smurfing).
* **Manual Compliance Review Baseline:** ~80,000 seconds (22.2 hours) 
* **Agentic RPA Pipeline Latency:** 515 seconds (8.5 minutes) for 10,000 transactions.
* **Optimization Variable:** By controlling the RAG chunk-size and limiting queries to the top 5% high-risk outliers, we successfully suppressed retrieval latency, maintaining a 155x throughput increase compared to manual labor.
* **Engineering Impact:** A **155x** increase in throughput. The system effectively eliminates human cognitive fatigue and maintains deterministic interception rates regardless of traffic spikes.

## 4. Azure Cloud Architecture Mapping (AZ-305 Target)
While the prototype utilizes local ML models and UiPath, the architecture maps natively to Azure enterprise components for cloud-scale deployment:
* **Secure API Gateway** -> *Azure API Management (APIM)*
* **Tokenization & Routing** -> *Azure Functions (C# serverless compute)*
* **Hybrid ML Engine** -> *Azure Machine Learning Workspace (Managed Endpoints)*
* **RAG Vector Database** -> *Azure AI Search + Azure OpenAI Service*
* **Execution Layer** -> *Azure Logic Apps (API-first orchestration)*

## 5. Architecture Decision Records (ADR)
For detailed technical trade-offs regarding the separation of concerns and vector database dependencies, refer to:
* [ADR-002: Implementation of RAG-Driven Agentic RPA](../../ADRs/ADR-002-RAG-Driven-Agentic-RPA.md)