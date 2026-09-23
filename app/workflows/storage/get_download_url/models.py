from pydantic import BaseModel


class GetDownloadUrlInput(BaseModel):
    file_id: str


class GetDownloadUrlOutput(BaseModel):
    file_id: str
    file_name: str
    mime_type: str
    url: str
