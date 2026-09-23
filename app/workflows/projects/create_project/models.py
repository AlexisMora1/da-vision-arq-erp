from datetime import date

from pydantic import BaseModel


class CreateProjectInput(BaseModel):
    name: str
    description: str
    client_id: str
    start_date: str
    end_date: str
    cover_image_id: str | None = None


class CreateProjectOutput(BaseModel):
    project_id: str
    name: str
    description: str
    client_id: str
    start_date: date
    end_date: date
    cover_image_id: str | None = None