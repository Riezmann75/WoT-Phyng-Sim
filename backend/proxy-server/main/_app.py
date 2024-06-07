from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import httpx
from main.commons.error_handlers import register_error_handler
import ssl
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware


def init_app(init_db: bool = True):

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        app.state.requests_client = httpx.AsyncClient(verify=False)
        yield
        await app.state.requests_client.aclose()

    app = FastAPI(redoc_url=None, docs_url="/docs", lifespan=lifespan)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    from main.controllers import router

    app.include_router(router)

    register_error_handler(app)

    return app
