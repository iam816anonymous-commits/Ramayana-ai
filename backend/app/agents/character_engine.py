class CharacterEngine:
    def __init__(self):
        pass

    async def get_character_state(self, character_name: str):
        # Future: Load from DB and memory
        return {"name": character_name, "mood": "calm"}

character_engine = CharacterEngine()
