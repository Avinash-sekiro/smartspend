from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def server_health():
    return {"status": "healthy"}