from fastapi import FastAPI
from app.routers import tasks
from dotenv import load_dotenv

load_dotenv()
app = FastAPI(
    title="Cortex AI API", 
    description="Backend service for the context-aware Cortex Vision AI Assistant."
)

app.include_router(tasks.router)

@app.get("/")
def read_root():
    """Health check endpoint to verify server status."""
    return {"status": "Cortex API is online and ready."}