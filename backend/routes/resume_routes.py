from fastapi import APIRouter, UploadFile, File
import os
from backend.services.resume_service import process_resume

router = APIRouter()

UPLOAD_FOLDER = "uploads/resumes"


@router.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):

    # create folder if it doesn't exist
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    # save uploaded file
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    # process resume
    result = process_resume(file_path)

    return {
        "message": "Resume uploaded successfully",
        "summary": result["summary"]
    }