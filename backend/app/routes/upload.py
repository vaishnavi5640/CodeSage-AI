from fastapi import APIRouter, UploadFile, File

router = APIRouter()

@router.post("/upload")
async def upload_code(file: UploadFile = File(...)):
    content = await file.read()

    return {
        "filename": file.filename,
        "file_size": len(content),
        "message": "File uploaded successfully!"
    }