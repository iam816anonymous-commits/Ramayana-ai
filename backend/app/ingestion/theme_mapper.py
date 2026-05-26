class ThemeMapper:
    def map_themes(self, text):
        themes = []
        keywords = {
            "Dharma": ["duty", "righteousness", "moral", "dharma"],
            "Karma": ["action", "consequence", "fate", "karma"],
            "Bhakti": ["devotion", "prayer", "worship", "bhakti"],
            "Niti": ["politics", "strategy", "leadership", "niti"],
            "Vairagya": ["detachment", "renunciation", "vairagya"]
        }

        lower_text = text.lower()
        for theme, words in keywords.items():
            if any(w in lower_text for w in words):
                themes.append(theme)
        return themes

theme_mapper = ThemeMapper()
