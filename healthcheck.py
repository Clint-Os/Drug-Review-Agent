from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health():
    """
    Health check endpoint to verify if the service is running.
    """
    return {"status": "ok", "message": "Service is running"}