from fastapi import APIRouter, UploadFile, File
from app.services.analyzer import analyze_code

router = APIRouter()

@router.post("/upload")
async def upload_code(file: UploadFile = File(...)):
    content = await file.read()

    code = content.decode("utf-8")

    analysis = analyze_code(code)

    return {
        "filename": file.filename,
        "analysis": analysis
    }