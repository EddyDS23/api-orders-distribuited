
from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware

from app.core.settings import Settings


def register_middleware(app:FastAPI, settings:Settings) -> None:

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )