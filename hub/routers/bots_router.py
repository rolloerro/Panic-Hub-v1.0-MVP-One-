from fastapi import APIRouter
import requests
import os

router = APIRouter()
MOCK_BOT_URL = f"http://mock_panic_bot:{os.getenv('MOCK_PANIC_BOT_PORT', 8002)}"

@router.get("/checklist")
def get_checklist():
    """Запрос к тестовому panic bot"""
    response = requests.get(f"{MOCK_BOT_URL}/simulate")
    return {"source": "mock_panic_bot", "response": response.json()}
