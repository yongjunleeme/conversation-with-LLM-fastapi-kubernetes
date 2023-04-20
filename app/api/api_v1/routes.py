from fastapi import APIRouter

from app.api.api_v1.endpoints import conversation

api_router = APIRouter()
api_router.include_router(conversation.router, prefix="/conversations", tags=["conversations"])
