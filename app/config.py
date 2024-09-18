from pydantic_settings import BaseSettings
from functools import lru_cache
import httpx
from enum import Enum


class DeploymentType(str, Enum):
    LOCAL = "local"
    DEV = "dev"
    STAGE = "stage"
    PROD = "prod"


class Config(BaseSettings):
    API_PREFIX: str = "/api"
    DEPLOYMENT: DeploymentType
    # Common Keycloaksettings
    KEYCLOAK_REALM: str
    KEYCLOAK_URL: str

    # Keycloak Admin settings
    KEYCLOAK_BFF_ID: str
    KEYCLOAK_BFF_SECRET: str

    # Keycloak UI settings
    KEYCLOAK_CLIENT_ID: str

    # SOIL-API settings
    SOIL_API_URL: str  # Full path to the Soil API (eg: http://soil-api-dev)
    SOIL_API_SECONDARY_URL: str | None = None  # The path to replacement API

    TIMEOUT: httpx.Timeout = httpx.Timeout(
        20.0,
        connect=10.0,
    )
    LIMITS: httpx.Limits = httpx.Limits(
        max_connections=500, max_keepalive_connections=50
    )


@lru_cache()
def get_config():
    return Config()


config = get_config()
