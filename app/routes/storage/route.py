from typing import Annotated

from fastapi import APIRouter, Depends, Response, UploadFile

from app.dependencies import get_file_repository
from app.domain.storage import FileRepositoryPort
from app.workflows.storage import (
    GetDownloadUrlInput,
    GetDownloadUrlOutput,
    GetUploadUrlInput,
    GetUploadUrlOutput,
    UploadFileOutput,
    download_file_workflow,
    get_download_url_workflow,
    get_upload_url_workflow,
    upload_file_workflow,
)

router = APIRouter(
    tags=["Storage"],
)


@router.post("/files/upload-url")
async def get_upload_url(
    request: GetUploadUrlInput,
    file_repository: Annotated[FileRepositoryPort, Depends(get_file_repository)],
) -> GetUploadUrlOutput:
    return await get_upload_url_workflow(
        request=request,
        file_repository=file_repository
    )


@router.get("/files/{file_id}/download-url")
async def get_download_url(
    file_id: str,
    file_repository: Annotated[FileRepositoryPort, Depends(get_file_repository)],
) -> GetDownloadUrlOutput:
    return await get_download_url_workflow(
        request=GetDownloadUrlInput(file_id=file_id),
        file_repository=file_repository
    )


# POC-only: real uploads will go straight to S3 once the presigned URL points there.
@router.put("/files/{file_id}/upload", deprecated=True)
async def upload_file(
    file_id: str,
    file_repository: Annotated[FileRepositoryPort, Depends(get_file_repository)],
    file: UploadFile,
) -> UploadFileOutput:
    data = await file.read()
    return await upload_file_workflow(
        file_id=file_id,
        data=data,
        mime_type=file.content_type or "application/octet-stream",
        file_repository=file_repository
    )


# POC-only: real downloads will be served directly from S3 once the presigned URL points there.
@router.get("/files/{file_id}/download", deprecated=True)
async def download_file(
    file_id: str,
    file_repository: Annotated[FileRepositoryPort, Depends(get_file_repository)],
) -> Response:
    result = await download_file_workflow(
        file_id=file_id,
        file_repository=file_repository
    )
    return Response(
        content=result.data,
        media_type=result.mime_type,
        headers={"Content-Disposition": f'attachment; filename="{result.file_name}"'}
    )
