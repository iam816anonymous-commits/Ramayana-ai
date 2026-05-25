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
        """
        The Sage Agent acts as the bridge between raw intelligence and the user.
        It wraps insights in a poetic, philosophical, and sacred tone.
        """
        query = brain_thought["query"]
        wisdom = brain_thought["wisdom_nugget"]
        connections = brain_thought["connections"]

        # Sage transforms the Brain's synthesis into scripture-style formatting
        reflection = f"Your inquiry into '{query}' has resonated through the halls of time."

        # Determine tone based on the content
        if "silence" in wisdom or "void" in brain_thought["synthesis"]:
             meaning = "The fragments of the past are currently obscured, yet the path remains clear for those who seek with a pure heart."
             context = "The unwritten chronicles of the Cosmos."
             takeaway = "Patience is the first step toward true understanding."
        else:
            meaning = f"The sacred records reveal: {wisdom[:250]}..."
            if connections:
                meaning += f" This wisdom is bound to the essences of {', '.join(connections)}."

            context = "This truth was distilled from the ancient songs of the Ramayana."
            takeaway = "Heed the echoes of the ancestors; their steps have carved the way."

        return SanctumResponse(
            reflection=reflection,
            meaning=meaning,
            context=context,
            takeaway=takeaway,
            type="wisdom",
            brain_synthesis=brain_thought["synthesis"]
        )

sage_agent = SageAgent()
