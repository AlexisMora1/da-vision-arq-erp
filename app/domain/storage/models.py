from dataclasses import dataclass


@dataclass
class GetUploadFileUrlRequest:
    file_name: str


@dataclass
class GetUploadFileUrlResponse:
    file_id: str
    url: str


@dataclass
class GetDownloadFileUrlRequest:
    file_id: str


@dataclass
class GetDownloadFileUrlResponse:
    file_id: str
    mime_type: str
    file_name: str
    url: str


@dataclass
class UploadFileRequest:
    file_id: str
    data: bytes
    mime_type: str


@dataclass
class UploadFileResponse:
    file_id: str
    file_name: str
    mime_type: str


@dataclass
class DownloadFileRequest:
    file_id: str


@dataclass
class DownloadFileResponse:
    file_id: str
    mime_type: str
    file_name: str
    data: bytes


@dataclass
class GetFileMetadataRequest:
    file_id: str


@dataclass
class GetFileMetadataResponse:
    file_id: str
    mime_type: str
    file_name: str