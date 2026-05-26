from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from app.services.llm_service import llm_service

class SanctumResponse(BaseModel):
    reflection: str
    meaning: str
    context: str
    takeaway: str
    type: str
    brain_synthesis: str
    sources: List[Dict[str, Any]] = []

class SageAgent:
    async def format_wisdom(self, brain_thought: dict) -> SanctumResponse:
        """
        The Sage Agent uses an LLM to wrap the Brain's raw synthesis in a sacred tone.
        """
        query = brain_thought["query"]
        synthesis = brain_thought["synthesis"]
        fragments = brain_thought.get("all_fragments", [])

        prompt = f"""
        Transform the following technical synthesis into a poetic and philosophical 'Sanctum Response'.
        The response must be structured in four distinct parts:
        1. Reflection: A short, resonant opening regarding the user's inquiry.
        2. Meaning: The core philosophical essence of the synthesis.
        3. Context: Where this truth sits within the wider Ramayana universe.
        4. Takeaway: A practical, meditative lesson for the seeker.

        User Query: {query}
        Synthesis: {synthesis}

        Structure the output as JSON.
        """

        raw_response = await llm_service.generate(prompt, system_prompt="You are the Sage of the Sanctum.")

        try:
            import json
            # Attempt to parse JSON response from Sage LLM
            data = json.loads(raw_response)
            return SanctumResponse(
                reflection=data.get("reflection", f"The query '{query}' echoes in the void."),
                meaning=data.get("meaning", synthesis),
                context=data.get("context", "Distilled from the eternal song."),
                takeaway=data.get("takeaway", "Seek the truth within."),
                type="wisdom",
                brain_synthesis=synthesis,
                sources=fragments
            )
        except:
            # Poetic fallback
            return SanctumResponse(
                reflection=f"The inquiry into '{query}' resonates deeply.",
                meaning=synthesis,
                context="Drawn from the ancient scrolls.",
                takeaway="Let the wisdom guide your path.",
                type="wisdom",
                brain_synthesis=synthesis,
                sources=fragments
            )

sage_agent = SageAgent()
