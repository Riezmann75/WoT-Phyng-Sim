import json
from httpx import AsyncClient
from main._config import config


async def create_sensor(client: AsyncClient):
    body = {
        "@type": "sensor",
        "@context": "https://www.w3.org/2019/wot/td/v1",
        "security": "nosec_sc",
        "links": [{"rel": "type", "href": "http://localhost:8081/tms/cht/sensor"}],
        "securityDefinitions": {"nosec_sc": {"scheme": "nosec"}},
        "title": "sensor",
        "phyProperties": {"location": [1, 1, 1], "field": "T"},
    }

    response = await client.post(
        f"{config.NODE_SERVER}/smarthome/actions/addPhyng",
        json=body,
    )
    return response.status_code 


async def create_ac(client: AsyncClient):
    body = {
        "@type": "ac",
        "@context": "https://www.w3.org/2019/wot/td/v1",
        "security": "nosec_sc",
        "securityDefinitions": {"nosec_sc": {"scheme": "nosec"}},
        "title": "ac",
        "links": [{"rel": "type", "href": "http://localhost:8081/tms/cht/chtAc"}],
        "phyProperties": {
            "dimensions": [0.5, 0.8, 0.5],
            "location": [0.1, 0.5, 2],
            "dimensionsIn": [0.15, 0.6, 0],
            "locationIn": [0.35, 0.6, 2.5],
            "dimensionsOut": [0, 0.6, 0.2],
            "locationOut": [0.6, 0.6, 2.1],
        },
    }

    response = await client.post(
        f"{config.NODE_SERVER}/smarthome/actions/addPhyng",
        json=body,
    )
    return response.status_code 


async def create_walls(client: AsyncClient):
    body = {
        "@type": "walls",
        "@context": "https://www.w3.org/2019/wot/td/v1",
        "security": "nosec_sc",
        "securityDefinitions": {"nosec_sc": {"scheme": "nosec"}},
        "links": [{"rel": "type", "href": "http://localhost:8081/tms/cht/chtWalls"}],
        "title": "walls",
        "phyProperties": {"dimensions": [3, 4, 3], "location": [0, 0, 0]},
    }

    response = await client.post(
        f"{config.NODE_SERVER}/smarthome/actions/addPhyng",
        json=body,
    )
    return response.status_code 


async def create_heater(client: AsyncClient):
    body = {
        "@type": "heater",
        "@context": "https://www.w3.org/2019/wot/td/v1",
        "security": "nosec_sc",
        "securityDefinitions": {"nosec_sc": {"scheme": "nosec"}},
        "links": [{"rel": "type", "href": "http://localhost:8081/tms/cht/chtHeater"}],
        "title": "heater",
        "phyProperties": {
            "dimensions": [0.1, 0.8, 0.5],
            "location": [0.1, 1, 0.2],
            "material": "copper",
        },
    }

    response = await client.post(
        f"{config.NODE_SERVER}/smarthome/actions/addPhyng",
        json=body,
    )
    return response.status_code 
