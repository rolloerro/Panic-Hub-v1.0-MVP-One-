from fastapi import FastAPI
from logic.intent_classifier import classify_intent
import requests, os

app = FastAPI(title="Orchestrator")

MOCK_BOT_URL = f"http://mock_panic_bot:{os.getenv('MOCK_PANIC_BOT_PORT', 8002)}"

@app.get("/health")
def health():
    return {"status": "ok", "service": "orchestrator"}

@app.post("/route")
def route_message(msg: dict):
    intent = classify_intent(msg.get("text", ""))
    if intent == "checklist":
        response = requests.get(f"{MOCK_BOT_URL}/simulate")
        return {"intent": intent, "bot_response": response.json()}
    return {"intent": "unknown", "bot_response": "🤷 Не понял запрос"}
