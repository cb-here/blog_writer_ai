from fastapi import APIRouter

router = APIRouter(tags=["health"])

@router.get("/")
async def root():
    return {
        "message": "Welcome to Blog Writer AI"
    }

@router.get("/status")
async def status():
    return {
        "message": "Server is healthy and running..."
    }