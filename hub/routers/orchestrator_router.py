from fastapi import APIRouter
import requests
import os

router = APIRouter()
ORCH_URL = f"http://orchestrator:{os.getenv('ORCHESTRATOR_PORT', 8001)}"

@router.post("/route")
def route_message(msg: dict):
    response = requests.post(f"{ORCH_URL}/route", json=msg)
    return {"orchestrator_response": response.json()}
