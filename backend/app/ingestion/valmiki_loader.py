import json
import os

class ValmikiLoader:
    def load(self, filepath):
        if not os.path.exists(filepath):
            return []

        with open(filepath, 'r') as f:
            data = json.load(f)

        documents = []
        for entry in data:
            # Build unified content for indexing but keep metadata structured
            content = f"{entry.get('translation', '')}\n\nExplanation: {entry.get('explanation', '')}\n\nCommentary: {entry.get('comments', '')}"

            doc = {
                "text": content,
                "metadata": {
                    "source": "Valmiki Ramayana",
                    "type": "shloka",
                    "kanda": entry.get("kanda"),
                    "sarga": entry.get("sarga"),
                    "verse": entry.get("shloka"),
                    "shloka_raw": entry.get("shloka_text"),
                    "translation_raw": entry.get("translation"),
                    "transliteration": entry.get("transliteration"),
                    "verse_ref": f"{entry.get('kanda')} {entry.get('sarga')}:{entry.get('shloka')}"
                }
            }
            documents.append(doc)
        return documents

valmiki_loader = ValmikiLoader()
