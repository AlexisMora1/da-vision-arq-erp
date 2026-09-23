from app.domain.storage import (
    FileRepositoryPort,
    GetUploadFileUrlRequest,
    get_upload_file_url,
)
from app.workflows.exceptions_handler import exceptions_handler
from app.workflows.storage.get_upload_url.models import (
    GetUploadUrlInput,
    GetUploadUrlOutput,
)


@exceptions_handler
async def get_upload_url_workflow(
    request: GetUploadUrlInput,
    file_repository: FileRepositoryPort,
) -> GetUploadUrlOutput:
    file = await get_upload_file_url(
        request=GetUploadFileUrlRequest(file_name=request.file_name),
        file_repository=file_repository
    )

    return GetUploadUrlOutput(
        file_id=file.file_id,
        url=file.url
    )
