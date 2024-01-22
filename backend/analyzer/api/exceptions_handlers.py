import traceback
from typing import Any, Callable

from fastapi import FastAPI, Request, Response, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import ValidationError

from analyzer.services.exceptions.exceptions import (
    AlreadyExistsError,
    BadRequestError,
    ErrorCodeEnum,
    MenuServiceError,
    NotFoundError,
    UnauthorizedError,
)


def catch_exceptions_middleware(
    request: Request,
    call_next: Callable[[Request], Response],
) -> Response:
    """
    Catch exceptions and return a JSON response with the error details.

    :param request: incoming request.
    :param call_next: next function to call.
    :returns: response.
    """
    try:
        return call_next(request)
    except Exception as ex:
        traceback.print_exc()
        return JSONResponse(
            {
                "error": {
                    "message": ex.args[0],
                    "code": ErrorCodeEnum.INTERNAL_SERVER_ERROR.value,
                },
            },
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


def already_exists_exception_handler(
    exc: AlreadyExistsError,
) -> Response:
    """
    Handle AlreadyExists exception.

    :param exc: exception.
    :returns: response.
    """
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={"error": {"message": exc.message, "code": exc.code.value}},
    )


def not_found_exception_handler(request: Request, exc: AlreadyExistsError) -> Response:
    """
    Handle NotFound exception.

    :param request: incoming request.
    :param exc: exception.
    :returns: response.
    """
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "error": {
                "message": f"{request.method} {exc.message}",
                "code": exc.code.value,
            },
        },
    )


def internal_server_exception_handler(exc: AlreadyExistsError) -> Response:
    """
    Handle InternalServer exception.

    :param exc: exception.
    :returns: response.
    """
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"error": {"message": exc.message, "code": exc.code.value}},
    )


def validation_exception_handler(
    request: Request,
    exc: Any,
) -> Response:
    """
    Handle validation exception.

    :param request: incoming request.
    :param exc: exception.
    :returns: response.
    """
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "error": {
                "message": f"{request.method} validation error",
                "code": ErrorCodeEnum.VALIDATION_ERROR.value,
                "details": str(exc),
            },
        },
    )


def request_validation_exception_handler(
    request: Request,
    exc: RequestValidationError,
) -> Response:
    """
    Handle request validation exception.

    :param request: incoming request.
    :param exc: exception.
    :returns: response.
    """
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "error": {
                "message": f"{request.method} validation error",
                "code": ErrorCodeEnum.VALIDATION_ERROR.value,
                "details": exc.errors(),
            },
        },
    )


def unauthorized_exception_handler(
    request: Request,
    exc: UnauthorizedError,
) -> Response:
    """
    Handle unauthorized exception.

    :param request: incoming request.
    :param exc: exception.
    :returns: response.
    """
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content={
            "error": {
                "message": f"{request.method} validation error",
                "code": ErrorCodeEnum.INVALID_CREDENTIALS.value,
                "details": str(exc.message),
            },
        },
    )


def add_exception_handlers(app: FastAPI) -> None:
    """
    Add exception handlers to the application.

    :param app: application.
    """
    app.middleware("http")(catch_exceptions_middleware)
    app.add_exception_handler(AlreadyExistsError, already_exists_exception_handler)
    app.add_exception_handler(ValidationError, validation_exception_handler)
    app.add_exception_handler(
        RequestValidationError,
        request_validation_exception_handler,
    )
    app.add_exception_handler(BadRequestError, validation_exception_handler)
    app.add_exception_handler(NotFoundError, not_found_exception_handler)
    app.add_exception_handler(UnauthorizedError, unauthorized_exception_handler)
    app.add_exception_handler(MenuServiceError, validation_exception_handler)
