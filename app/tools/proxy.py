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
        yield {"client": client}


async def _reverse_proxy(
    request: Request,
):
    client = request.state.client
    path = request.url.path.replace("/api", "/v1")
    path = path.replace("/soil_profiles", "/soil/profiles")
    path = path.replace("/soil_types", "/soil/types")

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
