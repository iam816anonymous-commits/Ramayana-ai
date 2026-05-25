import os

class TXTLoader:
    def load(self, filepath: str):
        with open(filepath, 'r') as f:
            content = f.read()

        return [{
            "text": content,
            "metadata": {
                "source": filepath,
                "type": "txt_document",
                "filename": os.path.basename(filepath)
            }
        }]
