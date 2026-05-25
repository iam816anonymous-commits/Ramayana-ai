from abc import ABC, abstractmethod

class LLMInterface(ABC):
    @abstractmethod
    async def generate_response(self, persona: dict, context: str, user_message: str) -> str:
        pass

class SimulatedLLM(LLMInterface):
    async def generate_response(self, persona: dict, context: str, user_message: str) -> str:
        response = f"[{persona['name']} responding with {persona['speech_style']} style]\n"
        response += f"Based on what I know: {context[:100]}...\n"
        response += f"I, {persona['name']}, acknowledge your message: '{user_message}'. My path is one of {', '.join(persona['traits'])}."
        return response
