import logging
import os
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    ENVIRONMENT: str
    LOGGING_LEVEL: int = logging.INFO

    JWT_SECRET: str

    NODE_SERVER: str

    class Config:
        case_sensitive = True
        env_file_encoding = "utf-8"


environment = os.environ.get("ENVIRONMENT", "local")
config = Config(  # type: ignore
    ENVIRONMENT=environment,
    # ".env.{environment}" takes priority over ".env"
    _env_file=[".env", f".env.{environment}"],
)
