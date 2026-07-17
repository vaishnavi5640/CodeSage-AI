from fastapi import APIRouter, UploadFile, File
from app.services.analyzer import analyze_code
from app.services.report_service import save_report

router = APIRouter()


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    content = await file.read()

    code = content.decode("utf-8")

    analysis = analyze_code(code)

    save_report(file.filename, analysis)

    return {
        "filename": file.filename,
        "analysis": analysis
    }