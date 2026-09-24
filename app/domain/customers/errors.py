from app.domain.errors import DomainError


class ClientNotFoundError(DomainError):
    """Exception raised when a client is not found."""
    http_code = 404

class ClientAlreadyExistsError(DomainError):
    """Exception raised when a client with the given email already exists."""
    http_code = 409