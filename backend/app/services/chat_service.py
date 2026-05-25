from backend.app.core.personas import PERSONAS
from backend.app.services.retrieval import retrieval_service
from backend.app.services.llm_interface import SimulatedLLM

class ChatService:
    def __init__(self, llm=SimulatedLLM()):
        self.llm = llm

    async def get_response(self, character_name: str, user_message: str):
        persona = PERSONAS.get(character_name)
        if not persona:
            return f"Character {character_name} not found."

        # Retrieve context
        context = retrieval_service.retrieve_context(user_message)
        context_str = "\n".join(context)

        # Use the LLM interface
        return await self.llm.generate_response(persona, context_str, user_message)

chat_service = ChatService()
