from fastapi import APIRouter
from main.schemas.common import EmptySchema

router = APIRouter()


@router.get("/pings", response_model=EmptySchema)
async def ping():
    return {}


@router.get("/ready", response_model=EmptySchema)
async def is_ready():
    return {}
