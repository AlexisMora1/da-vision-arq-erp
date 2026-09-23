from dataclasses import dataclass


@dataclass
class DownloadFileResult:
    data: bytes
    mime_type: str
    file_name: str
