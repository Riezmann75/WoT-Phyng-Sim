import json
from main._config import config
from httpx import AsyncClient
from main.libs.log import get_logger

logger = get_logger(__name__)


async def create_case(client: AsyncClient):
    body = {
        "@context": "https://www.w3.org/2019/wot/td/v1",
        "security": "nosec_sc",
        "securityDefinitions": {"nosec_sc": {"scheme": "nosec"}},
        "links": [{"rel": "type", "href": "http://localhost:8081/tms/cht/chtCase"}],
        "title": "smarthome",
        "sysProperties": {
            "meshQuality": 40,
            "cores": 4,
            "parallel": True,
            "blocking": False,
            "realtime": True,
            "endTime": 0,
            "background": "air",
        },
    }
    
    url = f"{config.NODE_SERVER}/wopsimulator/actions/createCase"
    logger.info(url)

    response = await client.post(
        f"{config.NODE_SERVER}/wopsimulator/actions/createCase",
        json=body,
    )
    return response.status_code


async def delete_case(client: AsyncClient):
    response = await client.post(
        f"{config.NODE_SERVER}/wopsimulator/actions/deleteCase"
    )
    return response.status_code


async def run_case(client: AsyncClient):
    response = await client.post(f"{config.NODE_SERVER}/smarthome/actions/run")
    return response.status_code


async def stop_case(client: AsyncClient):
    response = await client.post(f"{config.NODE_SERVER}/smarthome/actions/stop")
    return response.status_code


async def clean_case(client: AsyncClient):
    response = await client.post(f"{config.NODE_SERVER}/smarthome/actions/clean")
    return response.status_code
