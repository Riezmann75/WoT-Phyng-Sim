from fastapi import Request
from httpx import AsyncClient
from main.libs.log import get_logger

logger = get_logger(__name__)


def get_client_from_request(request: Request) -> AsyncClient:
    logger.error("Getting client from request:", request.app.state.requests_client)
    return request.app.state.requests_client
