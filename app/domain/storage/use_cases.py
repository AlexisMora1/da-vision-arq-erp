
from app.domain.storage.models import (
    DownloadFileRequest,
    DownloadFileResponse,
    GetDownloadFileUrlRequest,
    GetDownloadFileUrlResponse,
    GetFileMetadataRequest,
    GetFileMetadataResponse,
    GetUploadFileUrlRequest,
    GetUploadFileUrlResponse,
    UploadFileRequest,
    UploadFileResponse,
)
from app.domain.storage.ports import FileRepositoryPort


async def get_upload_file_url(
    request: GetUploadFileUrlRequest,
    file_repository: FileRepositoryPort,
) -> GetUploadFileUrlResponse:
    """Generate a URL for uploading a file to the storage service.

    Args:
        request (GetUploadFileUrlRequest): The request object containing the file name.

    Returns:
        GetUploadFileUrlResponse: The response object containing the file ID and the URL for uploading the file.
    """
    file = await file_repository.get_upload_file_url(
        file_name=request.file_name
    )

    return GetUploadFileUrlResponse(
        file_id=file["file_id"],
        url=file["url"]
    )


async def get_download_file_url(
    request: GetDownloadFileUrlRequest,
    file_repository: FileRepositoryPort,
) -> GetDownloadFileUrlResponse:
    """Generate a URL for downloading a file from the storage service.

    Args:
        request (GetDownloadFileUrlRequest): The request object containing the file ID.

    Returns:
        GetDownloadFileUrlResponse: The response object containing the file ID and the URL for downloading the file.
    """

    file = await file_repository.get_download_file_url(
        file_id=request.file_id
    )

    return GetDownloadFileUrlResponse(
        file_id=request.file_id,
        mime_type=file["mime_type"],
        file_name=file["file_name"],
        url=file["url"]
    )


async def upload_file(
    request: UploadFileRequest,
    file_repository: FileRepositoryPort,
) -> UploadFileResponse:
    """Upload a file to the storage service. This use case should be deprecated when passing to S3.

    Args:
        request (UploadFileRequest): The request object containing the file name, data, and MIME type.

    Returns:
        UploadFileResponse: The response object containing the file ID and the URL for the uploaded file.
    """
    file = await file_repository.upload_file(
        file_id=request.file_id,
        data=request.data,
        mime_type=request.mime_type
    )

    return UploadFileResponse(
        file_id=file["file_id"],
        file_name=file["file_name"],
        mime_type=file["mime_type"]
    )


async def download_file(
    request: DownloadFileRequest,
    file_repository: FileRepositoryPort,
) -> DownloadFileResponse:
    """Download a file from the storage service. This use case should be deprecated when passing to S3.

    Args:
        request (DownloadFileRequest): The request object containing the file ID.

    Returns:
        DownloadFileResponse: The response object containing the file ID, MIME type, file name, and the URL for the downloaded file.
    """
    file = await file_repository.download_file(
        file_id=request.file_id
    )

    return DownloadFileResponse(
        file_id=request.file_id,
        mime_type=file["mime_type"],
        file_name=file["file_name"],
        data=file["data"]
    )


async def get_file_metadata(
    request: GetFileMetadataRequest,
    file_repository: FileRepositoryPort,
) -> GetFileMetadataResponse:
    """Retrieve metadata for a file from the storage service.

    Args:
        request (GetFileMetadataRequest): The request object containing the file ID.

    Returns:
        GetFileMetadataResponse: The response object containing the file ID, MIME type, and file name.
    """
    file = await file_repository.get_file_metadata(
        file_id=request.file_id
    )

    return GetFileMetadataResponse(
        file_id=request.file_id,
        mime_type=file["mime_type"],
        file_name=file["file_name"]
    )