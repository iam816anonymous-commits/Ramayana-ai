import json
from typing import List
from app.services.llm_service import llm_service

class ThemeExtractor:
    """
    Extracts key mythological and philosophical themes from a synthesized text using an LLM.
    """
    async def extract_themes(self, text: str) -> List[str]:
        prompt = f"""
        Extract the primary mythological and philosophical themes from the following synthesis of the Ramayana.
        Return only a JSON list of strings representing the themes.

        Synthesis: {text}

        Themes:
        """

        response = await llm_service.generate(prompt, system_prompt="You are a scholar of mythology.")

        try:
            # Attempt to parse JSON if the LLM returned it
            # In a real scenario, we'd use better parsing/validation
            if "[" in response and "]" in response:
                start = response.find("[")
                end = response.rfind("]") + 1
                return json.loads(response[start:end])
        except:
            pass

        # Fallback to keyword extraction if LLM fails or is mock
        themes = []
        lower_text = text.lower()
        if "dharma" in lower_text or "duty" in lower_text:
            themes.append("Dharma")
        if "bhakti" in lower_text or "devotion" in lower_text:
            themes.append("Bhakti")
        if "sacrifice" in lower_text:
            themes.append("Sacrifice")

        return themes or ["General Mythology"]

theme_extractor = ThemeExtractor()
