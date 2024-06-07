from fastapi import APIRouter

from . import probe, case

router = APIRouter()

router.include_router(probe.router, tags=["probe"])
router.include_router(case.router, tags=["case"])
