import csv
import os
from typing import List, Dict, Any

class CSVLoader:
    """
    Loads Shlokas from CSV files.
    Expected columns: kanda_name, sarga, verse_ref, shloka, translation
    """
    def load(self, filepath: str) -> List[Dict[str, Any]]:
        shlokas = []
        with open(filepath, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Ensure we have the basic fields
                if not row.get('shloka') or not row.get('translation'):
                    continue

                shlokas.append({
                    "text": f"{row['shloka']}\n\nTranslation: {row['translation']}",
                    "metadata": {
                        "source": os.path.basename(filepath),
                        "kanda": row.get('kanda_name'),
                        "sarga": row.get('sarga'),
                        "verse": row.get('verse_ref'),
                        "shloka_raw": row.get('shloka'),
                        "translation_raw": row.get('translation'),
                        "type": "shloka",
                        "language": "sanskrit+english"
                    }
                })
        return shlokas
