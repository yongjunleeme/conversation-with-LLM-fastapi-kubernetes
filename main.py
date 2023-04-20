from fastapi import FastAPI

from app.api.api_v1.routes import api_router
from app.core.config import settings

app = FastAPI(
   openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.include_router(api_router, prefix=settings.API_V1_STR)
