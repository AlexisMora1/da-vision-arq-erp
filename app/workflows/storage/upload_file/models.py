from pydantic import BaseModel


class UploadFileOutput(BaseModel):
    file_id: str
    file_name: str
    mime_type: str
