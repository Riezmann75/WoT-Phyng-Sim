from typing import Any, Optional

from .base import BaseResponseSchema


class ErrorSchema(BaseResponseSchema):
    error_message: Optional[str]
    error_data: Optional[Any]
    error_code: Optional[int]
