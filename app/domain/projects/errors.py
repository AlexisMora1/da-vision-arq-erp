from app.domain.errors import DomainError


class ProjectNotFoundError(DomainError):
    http_code = 404

    def __init__(self, message: str = "Project not found") -> None:
        super().__init__(message)

class InvalidProjectDatesError(DomainError):
    http_code = 422

    def __init__(self, message: str = "end_date must be on or after start_date") -> None:
        super().__init__(message)
