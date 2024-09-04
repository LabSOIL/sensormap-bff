from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from app.config import config
from app.tools.proxy import lifespan
from app.models.config import UIConfig
from app.models.health import HealthCheck
from app.routes.areas import router as areas_router
from app.routes.sensors import router as sensors_router
from app.routes.sensordata import router as sensordata_router
from app.routes.users import router as users_router
from app.routes.soil_profiles import router as soil_profiles_router
from app.routes.soil_types import router as soil_types_router
from app.routes.plots import router as plots_router
from app.routes.plot_samples import router as plot_samples_router
from app.routes.projects import router as projects_router
from app.routes.utils import router as utils_router
from app.routes.transects import router as transects_router
from app.routes.gnss import router as gnss_router
from app.routes.instruments import router as instruments_router
from app.routes.instrument_channels import router as instrument_channels_router

app = FastAPI(lifespan=lifespan)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get(f"{config.API_PREFIX}/config")
async def get_keycloak_config() -> UIConfig:
    return UIConfig(
        clientId=config.KEYCLOAK_CLIENT_ID,
        realm=config.KEYCLOAK_REALM,
        url=config.KEYCLOAK_URL,
        deployment=config.DEPLOYMENT,
    )


@app.get(
    "/healthz",
    tags=["healthcheck"],
    summary="Perform a Health Check",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
    response_model=HealthCheck,
)
def get_health() -> HealthCheck:
    """Perform a Health Check

    Useful for Kubernetes to check liveness and readiness probes
    """
    return HealthCheck(status="OK")


app.include_router(
    areas_router,
    prefix=f"{config.API_PREFIX}/areas",
    tags=["areas"],
)
app.include_router(
    sensors_router,
    prefix=f"{config.API_PREFIX}/sensors",
    tags=["sensors"],
)
app.include_router(
    sensordata_router,
    prefix=f"{config.API_PREFIX}/sensordata",
    tags=["sensordata"],
)
app.include_router(
    users_router,
    prefix=f"{config.API_PREFIX}/users",
    tags=["users"],
)
app.include_router(
    soil_profiles_router,
    prefix=f"{config.API_PREFIX}/soil_profiles",
    tags=["soil", "soil_profiles"],
)
app.include_router(
    soil_types_router,
    prefix=f"{config.API_PREFIX}/soil_types",
    tags=["soil", "soil_types"],
)
app.include_router(
    plots_router,
    prefix=f"{config.API_PREFIX}/plots",
    tags=["plots"],
)
app.include_router(
    plot_samples_router,
    prefix=f"{config.API_PREFIX}/plot_samples",
    tags=["projects"],
)
app.include_router(
    projects_router,
    prefix=f"{config.API_PREFIX}/projects",
    tags=["projects"],
)
app.include_router(
    utils_router,
    prefix=f"{config.API_PREFIX}/utils",
    tags=["utils"],
)
app.include_router(
    transects_router,
    prefix=f"{config.API_PREFIX}/transects",
    tags=["transects"],
)
app.include_router(
    gnss_router,
    prefix=f"{config.API_PREFIX}/gnss",
    tags=["gnss"],
)
app.include_router(
    instruments_router,
    prefix=f"{config.API_PREFIX}/instruments",
    tags=["instruments"],
)
app.include_router(
    instrument_channels_router,
    prefix=f"{config.API_PREFIX}/instrument_channels",
    tags=["instrument_channels"],
)
