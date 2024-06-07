from typing import Optional
from fastapi import HTTPException
from fastapi.responses import JSONResponse

from main.schemas.exceptions import ErrorSchema


class StatusCode:
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    METHOD_NOT_ALLOWED = 405
    INTERNAL_SERVER_ERROR = 500
    TOO_MANY_REQUESTS = 429


class ErrorCode:
    BAD_REQUEST = 400000
    VALIDATION_ERROR = 400001
    INVALID_AUTHORIZATION_HEADER = 400002
    PAYLOAD_TOO_LARGE = 400003

    OPENAI_ERROR = 400100

    UNAUTHORIZED = 401000
    INVALID_ACCESS_TOKEN = 401001
    EXPIRED_ACCESS_TOKEN = 401002
    FRESH_ACCESS_TOKEN_REQUIRED = 401003

    FORBIDDEN = 403000
    NOT_FOUND = 404000
    METHOD_NOT_ALLOWED = 405000

    INTERNAL_SERVER_ERROR = 500000

    TOO_MANY_REQUESTS = 429000


class ErrorMessage:
    BAD_REQUEST = "Bad request."
    VALIDATION_ERROR = "Validation error."
    UNAUTHORIZED = "Unauthorized."
    FORBIDDEN = "Forbidden."
    NOT_FOUND = "Not found."
    METHOD_NOT_ALLOWED = "Method not allowed."
    INTERNAL_SERVER_ERROR = "Internal server error."

    EMPTY_AUTHORIZATION_HEADER = "Empty authorization header."
    INVALID_AUTHORIZATION_HEADER = "Authorization header should start with Bearer."

    INVALID_AUTH_PAYLOAD = "Invalid auth payload."
    EMPTY_TOKEN_FIELD = "Empty token field."

    DUPLICATE_DEVICE_NAME = "Device name already exists."


class BaseError(HTTPException):
    def __init__(
        self,
        *,
        error_message=None,
        error_data=None,
        status_code: Optional[int] = None,
        error_code: Optional[int] = None,
    ):
        """
        Customize the response exception

        :param error_message: <string> Message field in the response body
        :param status_code: <number> HTTP status code
        :param error_data: <dict> Json body data
        :param error_code: <number> error code
        """

        if error_message is not None:
            self.error_message = error_message

        if status_code is not None:
            self.status_code = status_code

        if error_code is not None:
            self.error_code = error_code

        self.error_data = error_data

    def __str__(self):
        class_name = self.__class__.__name__
        status_code = self.status_code
        error_code = self.error_code
        return f"{class_name}({status_code=}, {error_code=})"

    def to_response(self):
        return JSONResponse(
            ErrorSchema.model_validate(self).model_dump(),
            self.status_code,
        )


class InternalServerError(BaseError):
    status_code = StatusCode.INTERNAL_SERVER_ERROR
    error_code = ErrorCode.INTERNAL_SERVER_ERROR
    error_message = ErrorMessage.INTERNAL_SERVER_ERROR


class ValidationError(BaseError):
    status_code = StatusCode.BAD_REQUEST
    error_code = ErrorCode.VALIDATION_ERROR
    error_message = ErrorMessage.INTERNAL_SERVER_ERROR


class Unauthorized(BaseError):
    status_code = StatusCode.UNAUTHORIZED
    error_code = ErrorCode.UNAUTHORIZED
    error_message = ErrorMessage.UNAUTHORIZED


class BadRequest(BaseError):
    status_code = StatusCode.BAD_REQUEST
    error_code = ErrorCode.BAD_REQUEST
    error_message = ErrorMessage.BAD_REQUEST


class Forbidden(BaseError):
    status_code = StatusCode.FORBIDDEN
    error_code = ErrorCode.FORBIDDEN
    error_message = ErrorMessage.FORBIDDEN


class NotFound(BaseError):
    status_code = StatusCode.NOT_FOUND
    error_code = ErrorCode.NOT_FOUND
    error_message = ErrorMessage.NOT_FOUND


class DuplicateDeviceName(BaseError):
    status_code = StatusCode.BAD_REQUEST
    error_code = ErrorCode.BAD_REQUEST
    error_message = ErrorMessage.DUPLICATE_DEVICE_NAME
