from fastapi import APIRouter, UploadFile, File
from typing import List
from app.core import processor

router = APIRouter()

@router.post("/upload")
async def upload_documents(files: List[UploadFile] = File(...)):
    processed_files = processor.process_uploaded_files(files)
    return {"uploaded_files": processed_files}

@router.get("/query")
async def query_documents(q: str):
    results = processor.query_documents(q)
    return {"query": q, "results": results}
