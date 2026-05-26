class CommentaryProcessor:
    def process(self, commentary_text):
        if not commentary_text:
            return []

        # Split by common markers if any, or just return as a list of paragraphs
        paragraphs = [p.strip() for p in commentary_text.split("\n\n") if p.strip()]
        return paragraphs

commentary_processor = CommentaryProcessor()
