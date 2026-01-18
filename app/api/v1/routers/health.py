
from fastapi import APIRouter

router = APIRouter(tags=["Health"])

@router.get("/health")
def healt_check():
    return {"status":"Ok"}