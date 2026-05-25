import re

class Cleaner:
    def clean(self, text: str):
        # Remove multiple newlines
        text = re.sub(r'\n+', '\n', text)
        # Remove multiple spaces
        text = re.sub(r' +', ' ', text)
        # Basic cleanup
        text = text.strip()
        return text
