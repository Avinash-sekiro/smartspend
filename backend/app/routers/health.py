from fastapi import APIRouter
from app.schemas.connection import client

router = APIRouter()

@router.get("/health")
def server_health():
    return {"status": "healthy"}


@router.get("/health/db")
def db_health():
    try:
        client.admin.command('ping')
        return {"status": "healthy","connection": "MongoDB connection successful!"}
    except Exception as e:
        return {"status": "unhealthy", "error": str(e)}