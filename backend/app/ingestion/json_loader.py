import json
import os

class JSONLoader:
    def load(self, filepath: str):
        with open(filepath, 'r') as f:
            data = json.load(f)

        normalized = []
        if isinstance(data, list):
            for item in data:
                normalized.append(self._normalize(item, filepath))
        else:
            normalized.append(self._normalize(data, filepath))
        return normalized

    def _normalize(self, item, source):
        # Flatten simple structures for RAG
        text_parts = []
        for k, v in item.items():
            if isinstance(v, list):
                text_parts.append(f"{k}: {', '.join(map(str, v))}")
            else:
                text_parts.append(f"{k}: {v}")

        return {
            "text": "\n".join(text_parts),
            "metadata": {
                "source": source,
                "type": "json_record"
            }
        }
