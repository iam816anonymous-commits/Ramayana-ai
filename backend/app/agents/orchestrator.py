from backend.app.agents.sage import sage_agent
from backend.app.core.retrieval import retrieval_service

class Orchestrator:
    async def process_query(self, query: str):
        # 1. Classify (Simple logic for Phase 1)
        query_type = "moral" if any(word in query.lower() for word in ["why", "meaning", "dharma", "lesson"]) else "factual"

        # 2. Route Retrieval
        context = retrieval_service.retrieve_context(query)
        context_str = "\n".join(context)

        # 3. Sage Interaction
        response = await sage_agent.format_wisdom(context_str, query)

        return response

orchestrator = Orchestrator()
