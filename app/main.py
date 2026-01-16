from fastapi import FastAPI

from app.core.middleware import register_middleware
from app.core.settings import get_settings
from app.api.v1.routers import router as v1_router

settings = get_settings()

def create_app() -> FastAPI:

    app = FastAPI(
        title=settings.APP_NAME,
        description=settings.APP_DESCRIPTION,
        version=settings.APP_VERSION
    )

    register_middleware(app,settings)
    app.include_router(v1_router, prefix="/api/v1")

    return app


app = create_app()
