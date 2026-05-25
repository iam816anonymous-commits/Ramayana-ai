from pydantic import BaseModel
from typing import List

class SanctumResponse(BaseModel):
    reflection: str
    meaning: str
    context: str
    takeaway: str
    type: str
    brain_synthesis: str # Added to show the Brain's work

class SageAgent:
    async def format_wisdom(self, brain_thought: dict) -> SanctumResponse:
        query = brain_thought["query"]
        wisdom = brain_thought["wisdom_nugget"]
        connections = brain_thought["connections"]

        # Sage transforms the Brain's synthesis into scripture-style formatting
        reflection = f"The inquiry into '{query}' reveals a path through the eternal story."

        meaning = f"In the records of the past, we find: {wisdom[:150]}..."
        if connections:
            meaning += f" This is tied to {', '.join(connections)}."

        context = "This fragment is preserved in the annals of Dharma."
        takeaway = "Let your actions be guided by truth, not desire."

        return SanctumResponse(
            reflection=reflection,
            meaning=meaning,
            context=context,
            takeaway=takeaway,
            type="philosophical",
            brain_synthesis=brain_thought["synthesis"]
        )

sage_agent = SageAgent()
