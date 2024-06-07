from main._config import config
from httpx import AsyncClient


async def turn_on_ac(client: AsyncClient):
    response = await client.post(
        f"{config.NODE_SERVER}/smarthome-ac/actions/turnOn"
    )
    return response.status_code 


async def turn_off_ac(client: AsyncClient):
    response = await client.post(
        f"{config.NODE_SERVER}/smarthome-ac/actions/turnOff"
    )
    return response.status_code 


async def update_ac_velocity(new_velocity: float, client: AsyncClient):
    response = await client.put(
        f"{config.NODE_SERVER}/smarthome-ac/properties/velocity",
        json=new_velocity,
    )
    return response.status_code 


async def update_ac_angle(new_angle: float, client: AsyncClient):
    response = await client.put(
        f"{config.NODE_SERVER}/smarthome-ac/properties/angle",
        json=new_angle,
    )
    return response.status_code 


async def update_ac_temperature(new_temperature: float, client: AsyncClient):
    response = await client.put(
        f"{config.NODE_SERVER}/smarthome-ac/properties/temperature",
        json=new_temperature,
    )
    return response.status_code 


async def update_heater_temperature(new_temperature: float, client: AsyncClient):
    response = await client.put(
        f"{config.NODE_SERVER}/smarthome-heater/properties/temperature",
        json=new_temperature,
    )
    return response.status_code 
