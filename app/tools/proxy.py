import httpx
from fastapi import FastAPI, Request, Depends
from starlette.background import BackgroundTask
from fastapi.responses import StreamingResponse
from contextlib import asynccontextmanager
from app.config import config
from fastapi import APIRouter


router = APIRouter()


async def get_async_client():
    # Asynchronous client to be used as a dependency in calls to the Soil API
    async with httpx.AsyncClient() as client:
        yield client


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with httpx.AsyncClient(
        base_url=f"{config.SOIL_API_URL}",
        timeout=config.TIMEOUT,
        limits=config.LIMITS,
    ) as client:
        if config.SOIL_API_SECONDARY_URL is None:
            # If no secondary URL is provided, use the primary URL for both
            # clients
            yield {"client": client, "client_secondary": client}
        else:
            async with httpx.AsyncClient(
                base_url=f"{config.SOIL_API_SECONDARY_URL}",
                timeout=config.TIMEOUT,
                limits=config.LIMITS,
            ) as secondary_client:
                yield {"client": client, "client_secondary": secondary_client}


async def _reverse_proxy(
    request: Request,
):
    client = request.state.client

    path = request.url.path.replace("/api", "/v1")
    path = path.replace("/soil_profiles", "/soil/profiles")
    path = path.replace("/soil_types", "/soil/types")

    if request.method == "GET" and (
        path
        in [
            "/v1/plots",
            "/v1/areas",
            "/v1/projects",
        ]
    ):
        # These routes are in the refactored API and are used inplace of the
        # primary API
        client = request.state.client_secondary

    url = httpx.URL(
        path=path,
        query=request.url.query.encode("utf-8"),
    )
    req = client.build_request(
        request.method,
        url,
        headers=request.headers.raw,
        content=request.stream(),
    )
    r = await client.send(req, stream=True)

    return StreamingResponse(
        r.aiter_raw(),
        status_code=r.status_code,
        headers=r.headers,
        background=BackgroundTask(r.aclose),
    )
