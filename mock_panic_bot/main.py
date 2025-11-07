from fastapi import FastAPI

app = FastAPI(title="Mock Panic Checklist Bot")

@app.get("/simulate")
def simulate():
    return {
        "bot": "panic-checklist-bot",
        "content": [
            "🧘 Сделай вдох и выдох",
            "💧 Выпей воды",
            "🪞 Посмотри вокруг: всё реально",
            "📱 Напиши другу — ты не один"
        ]
    }

@app.get("/health")
def health():
    return {"status": "ok", "service": "mock_panic_bot"}
