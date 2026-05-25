from backend.app.agents.brain import brain_agent
from backend.app.agents.sage import sage_agent

class Orchestrator:
    async def process_query(self, query: str):
        # 1. Consult the Brain (The Intelligence layer)
        # The brain retrieves context and synthesizes it.
        brain_thought = await brain_agent.consult_brain(query)

        # 2. Route to Sage for Experience formatting
        # The Sage takes the Brain's logic and makes it "Sanctum-ready"
        response = await sage_agent.format_wisdom(brain_thought)

        return response

orchestrator = Orchestrator()
