from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root():
    return {
        "message": "Добро пожаловать в Panic Hub 🚀",
        "routes": ["/bots", "/orchestrator", "/health"]
    }
