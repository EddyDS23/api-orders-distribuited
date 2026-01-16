
from fastapi import APIRouter

router = APIRouter(tags=["Health"])

@router.get("/healt")
def healt_check():
    return {"status":"Ok"}