import asyncio
from typing_extensions import Annotated
from fastapi import APIRouter, Depends
from httpx import AsyncClient

from main.commons.dependencies import get_client_from_request
from main.engines.case import create_case, run_case, stop_case
from main.engines.phyng import create_ac, create_heater, create_sensor, create_walls
from main.engines.phyng_prop import (
    turn_on_ac,
    update_ac_temperature,
    update_ac_angle,
    update_ac_velocity,
)
from main.engines.post_process import create_video, post_process
from main.schemas.case import RunCaseSchema
import ssl
import httpx

from main._config import config
from main.libs.log import get_logger

router = APIRouter()

logger = get_logger(__name__)


# write code to create engine
@router.post("/cases")
async def request_simulation(
    client: Annotated[AsyncClient, Depends(get_client_from_request)],
):
    # first need to create_case
    logger.info(await create_case(client))
   
    # next add phyngs to case
    await create_sensor(client)
    await create_ac(client)
    await create_walls(client)
    await create_heater(client)

    return {"message": "Simulation has initiated."}


@router.post("/cases/run")
async def start_case(
    ac_condition: RunCaseSchema,
    client: Annotated[AsyncClient, Depends(get_client_from_request)],
):
    await update_ac_temperature(ac_condition.ac_temperature, client)
    await update_ac_velocity(ac_condition.ac_velocity, client)
    await update_ac_angle(ac_condition.ac_angle, client)
    # start case
    await run_case(client)
    await asyncio.sleep(0.5)
    await turn_on_ac(client)
    return {"message": "Simulation has started."}


@router.post("/cases/stop")
async def end_case(
    client: Annotated[AsyncClient, Depends(get_client_from_request)],
):
    # stop case
    await stop_case(client)
    await post_process(client)
    await create_video()
    return {"message": "Simulation has stopped."}
