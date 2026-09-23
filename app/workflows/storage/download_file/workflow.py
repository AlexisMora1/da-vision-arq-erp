from app.domain.storage import DownloadFileRequest, FileRepositoryPort, download_file
from app.workflows.exceptions_handler import exceptions_handler
from app.workflows.storage.download_file.models import DownloadFileResult


@exceptions_handler
async def download_file_workflow(
    file_id: str,
    file_repository: FileRepositoryPort,
) -> DownloadFileResult:
    file = await download_file(
        request=DownloadFileRequest(file_id=file_id),
        file_repository=file_repository
    )

    return DownloadFileResult(
        data=file.data,
        mime_type=file.mime_type,
        file_name=file.file_name
    )
