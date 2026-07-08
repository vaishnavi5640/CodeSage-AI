from fastapi import APIRouter

router = APIRouter()

@router.get("/review")
def review():
    return {
        "status": "success",
        "message": "Review API Working!"
    }