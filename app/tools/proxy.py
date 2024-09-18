import httpx
from fastapi import FastAPI, Request, Depends
from starlette.background import BackgroundTask
from fastapi.responses import JSONResponse
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

    # Modify the path based on your existing rules
    path = request.url.path.replace("/api", "/v1")
    path = path.replace("/soil_profiles", "/soil/profiles")
    path = path.replace("/soil_types", "/soil/types")

    if request.method == "GET" and (
        (
            path
            in [
                "/v1/plots",
                "/v1/areas",
                "/v1/projects",
                "/v1/plot_samples",
                "/v1/sensors",
            ]
            or path.startswith("/v1/sensors/")
        )
    ):
        # Use secondary client for specific routes
        client = request.state.client_secondary

    # Build the request to forward to the Rust API
    url = httpx.URL(
        path=path,
        query=request.url.query.encode("utf-8"),
    )
    req = client.build_request(
        request.method,
        url,
        headers=request.headers.raw,
        content=await request.body(),  # Wait for full body content
    )

    # Send the request and get the full response
    r = await client.send(req)

    # Forward the entire response to the client without chunking
    return JSONResponse(
        content=r.json(),  # Assume the Rust API returns JSON
        status_code=r.status_code,
        headers=dict(r.headers),
    )
