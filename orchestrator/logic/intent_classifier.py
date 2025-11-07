def classify_intent(text: str) -> str:
    text = text.lower()
    if "чек" in text or "паник" in text:
        return "checklist"
    return "unknown"
