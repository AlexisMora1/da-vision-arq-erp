from typing import Protocol, TypedDict


class UploadFile(TypedDict):
    file_id: str
    file_name: str
    mime_type: str


class UploadFileSigned(UploadFile):
    url: str


class DownloadFile(TypedDict):
    file_id: str
    mime_type: str
    file_name: str
    data: bytes


class DownloadFileSigned(DownloadFile):
    url: str


class FileMetadata(TypedDict):
    file_id: str
    mime_type: str
    file_name: str


class FileRepositoryPort(Protocol):
    async def get_upload_file_url(self, file_name: str) -> UploadFileSigned:
        ...

    async def get_download_file_url(self, file_id: str) -> DownloadFileSigned:
        ...

    async def upload_file(self, file_id: str, data: bytes, mime_type: str) -> UploadFile:
        ...

    async def download_file(self, file_id: str) -> DownloadFile:
        ...

    async def get_file_metadata(self, file_id: str) -> FileMetadata:
        ...