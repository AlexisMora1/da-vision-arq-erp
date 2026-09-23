from app.domain.errors import DomainError


class FileNotFoundError(DomainError):
    http_code = 404

    def __init__(self, message: str = "File not found") -> None:
        super().__init__(message)
