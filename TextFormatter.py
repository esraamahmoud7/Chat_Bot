import re
# for output shape
class TextFormatter:
    @staticmethod
    def clean(text):
        text = re.sub(r"\n*\*?\*?(\d+)\. (.+?)\*?\*?", r"\n\n\1. \2", text)
        text = text.replace("**", "")
        text = re.sub(r"\n{3,}", "\n\n", text)
        text = text.replace("Tip:", "💡 Tip:")
        return text.strip()