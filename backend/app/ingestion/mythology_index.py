import os
import json
from typing import Dict, List, Set

class MythologyIndex:
    """
    Builds static indices of mythology entities mapping to verse references.
    This helps in high-precision navigation and future Knowledge Graph construction.
    """
    def __init__(self):
        self.indices = {
            "characters": {}, # { "Rama": ["१-१-१", "१-१-२"] }
            "themes": {},     # { "Dharma": ["१-१-२"] }
            "events": {}
        }

    def build_from_payloads(self, payloads: List[Dict]):
        for p in payloads:
            meta = p.get('metadata', {})
            v_ref = meta.get('verse_ref')
            if not v_ref: continue

            # Index Characters
            for char in meta.get('characters', []):
                if char not in self.indices['characters']:
                    self.indices['characters'][char] = []
                if v_ref not in self.indices['characters'][char]:
                    self.indices['characters'][char].append(v_ref)

            # Index Themes/Concepts
            for concept in meta.get('concepts', []):
                if concept not in self.indices['themes']:
                    self.indices['themes'][concept] = []
                if v_ref not in self.indices['themes'][concept]:
                    self.indices['themes'][concept].append(v_ref)

            # Index Events
            event = meta.get('event')
            if event:
                if event not in self.indices['events']:
                    self.indices['events'][event] = []
                if v_ref not in self.indices['events'][event]:
                    self.indices['events'][event].append(v_ref)

    def save(self, output_dir: str = "data/indices"):
        os.makedirs(output_dir, exist_ok=True)
        for name, data in self.indices.items():
            with open(os.path.join(output_dir, f"{name}_index.json"), "w") as f:
                json.dump(data, f, indent=2)

myth_index = MythologyIndex()
