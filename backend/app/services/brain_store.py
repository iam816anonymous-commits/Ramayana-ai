import json
import os

class BrainStore:
    """
    Persistent storage for synthesized wisdom.
    Allows the agents to build upon previous 'revelations'.
    """
    def __init__(self, storage_path="data/brain_store.json"):
        self.storage_path = storage_path
        self.memory = self._load()

    def _load(self):
        if os.path.exists(self.storage_path):
            with open(self.storage_path, 'r') as f:
                return json.load(f)
        return {}

    def _save(self):
        os.makedirs(os.path.dirname(self.storage_path), exist_ok=True)
        with open(self.storage_path, 'w') as f:
            json.dump(self.memory, f, indent=2)

    def get_wisdom(self, topic: str):
        return self.memory.get(topic.lower())

    def store_wisdom(self, topic: str, synthesis: dict):
        self.memory[topic.lower()] = synthesis
        self._save()

brain_store = BrainStore()
