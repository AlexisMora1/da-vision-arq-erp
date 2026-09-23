from pydantic import BaseModel


class GetUploadUrlInput(BaseModel):
    file_name: str


class GetUploadUrlOutput(BaseModel):
    file_id: str
    url: str
