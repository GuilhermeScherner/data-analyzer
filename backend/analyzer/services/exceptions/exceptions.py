import enum


class ErrorCodeEnum(enum.Enum):
    """Error codes for the API."""

    INTERNAL_SERVER_ERROR = "internal-server-error"
    VALIDATION_ERROR = "validation-error"
    NOT_FOUND = "not-found"
    BAD_REQUEST = "bad-request"
    ALREADY_EXISTS = "already-exists"
    INVALID_CREDENTIALS = "invalid-credentials"


class ApplicationExceptionError(Exception):
    """Base exception for the API."""

    def __init__(self, code: ErrorCodeEnum, message: str) -> None:
        self.code = code
        self.message = message


class AlreadyExistsError(ApplicationExceptionError):
    """Exception for already exists."""


class NotFoundError(ApplicationExceptionError):
    """Exception for not found."""


class BadRequestError(ApplicationExceptionError):
    """Exception for bad requests."""


class UnauthorizedError(ApplicationExceptionError):
    """Exception for bad requests."""


class MenuServiceError(ApplicationExceptionError):
    """Exception for menu service."""
