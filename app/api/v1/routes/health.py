from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
async def health_check() -> dict[str, str]:
    """Simple health-check endpoint.

    Returns a JSON object indicating the service status.
    """
    return {"status": "ok"}
