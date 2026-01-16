from fastapi import APIRouter
from .health import router as healt_router


router = APIRouter()

router.include_router(healt_router)
