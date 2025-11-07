from fastapi import FastAPI
from routers import root, bots_router, orchestrator_router

app = FastAPI(title="DWM Panic Hub", version="1.0")

app.include_router(root.router)
app.include_router(bots_router.router, prefix="/bots")
app.include_router(orchestrator_router.router, prefix="/orchestrator")

@app.get("/health")
def health():
    return {"status": "ok", "service": "hub"}
