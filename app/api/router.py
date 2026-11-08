from fastapi import APIRouter
from .routes import health_router, blog_router


api_router = APIRouter(prefix="/api")


api_router.include_router(router=health_router)
api_router.include_router(prefix="/blog", router=blog_router)
