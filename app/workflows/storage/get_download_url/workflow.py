from app.domain.storage import (
    FileRepositoryPort,
    GetDownloadFileUrlRequest,
    get_download_file_url,
)
from app.workflows.exceptions_handler import exceptions_handler
from app.workflows.storage.get_download_url.models import (
    GetDownloadUrlInput,
    GetDownloadUrlOutput,
)


@exceptions_handler
async def get_download_url_workflow(
    request: GetDownloadUrlInput,
    file_repository: FileRepositoryPort,
) -> GetDownloadUrlOutput:
    file = await get_download_file_url(
        request=GetDownloadFileUrlRequest(file_id=request.file_id),
        file_repository=file_repository
    )

    return GetDownloadUrlOutput(
        file_id=file.file_id,
        file_name=file.file_name,
        mime_type=file.mime_type,
        url=file.url
    )
