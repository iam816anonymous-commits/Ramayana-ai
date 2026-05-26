import re

class ShlokaValidator:
    def validate(self, shloka_data):
        """Checks for common issues in the Valmiki dataset."""
        errors = []
        if not shloka_data.get("shloka_text"):
            errors.append("Missing Sanskrit text")
        if not shloka_data.get("translation"):
            errors.append("Missing translation")

        # Detect merged shlokas (e.g., "1-1-1, 2")
        ref = str(shloka_data.get("shloka", ""))
        if "," in ref or "-" in ref.split("-")[-1]:
             shloka_data["is_merged"] = True

        return errors

shloka_validator = ShlokaValidator()

class OCRCleaner:
    def clean_text(self, text):
        if not text:
            return ""
        # Remove common OCR artifacts
        text = re.sub(r'\[\d+\]', '', text) # Remove citations like [1]
        text = re.sub(r'\s+', ' ', text).strip()
        return text

ocr_cleaner = OCRCleaner()
