from app.domain.storage import FileRepositoryPort, UploadFileRequest, upload_file
from app.workflows.exceptions_handler import exceptions_handler
from app.workflows.storage.upload_file.models import UploadFileOutput


@exceptions_handler
async def upload_file_workflow(
    file_id: str,
    data: bytes,
    mime_type: str,
    file_repository: FileRepositoryPort,
) -> UploadFileOutput:
    file = await upload_file(
        request=UploadFileRequest(file_id=file_id, data=data, mime_type=mime_type),
        file_repository=file_repository
    )

    return UploadFileOutput(
        file_id=file.file_id,
        file_name=file.file_name,
        mime_type=file.mime_type
    )
