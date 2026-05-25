# Technical Requirements Document: Ramayana AI

## Tech Stack
- **Frontend:** NextJS 15, TypeScript, Tailwind CSS, Framer Motion, ThreeJS, Shadcn UI.
- **Backend:** FastAPI (Python), Postgres (Relational), Redis (Caching), Qdrant (Vector), Neo4j (Graph), Celery (Tasks).
- **AI:** RAG (Retrieval Augmented Generation), Sentence Embeddings, LLM Orchestration.

## System Components
1. **Orchestrator:** Classifies user intent (moral, factual, personal) and routes to appropriate services.
2. **Sage Agent:** A tone and formatting layer that transforms LLM output into scripture-style wisdom.
3. **Retrieval Service:** Manages embeddings and similarity search in Qdrant.
4. **Knowledge Graph (Future):** Manages relationships between entities (Rama -> brother -> Lakshmana).
5. **Timeline Engine:** Manages sequential events and their metadata.

## Folder Structure
- `backend/app/core/`: Retrieval, embeddings, vector store, timeline, graph logic.
- `backend/app/agents/`: Orchestrator, Sage, character engines.
- `backend/app/api/`: API endpoints (sanctum, characters, timeline).
- `backend/app/services/`: Specific business logic (RAG, prompts, quotes).

## Deployment
- Containerized using Docker and Docker Compose.
- Postgres for user and metadata; Qdrant for vectors; Neo4j for relations.
