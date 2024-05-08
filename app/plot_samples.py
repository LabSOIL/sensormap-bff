from typing import Any
from fastapi import Depends, APIRouter, Response, Body, Request
from app.config import config
from app.utils import get_async_client
import httpx
from uuid import UUID
from app.models.user import User
from app.auth import require_admin

router = APIRouter()


@router.get("/{plot_sample_id}")
async def get_plot_sample(
    client: httpx.AsyncClient = Depends(get_async_client),
    *,
    plot_sample_id: UUID,
) -> Any:
    """Get a plot samples by id"""

    res = await client.get(
        f"{config.SOIL_API_URL}/v1/plot_samples/{plot_sample_id}",
    )

    return res.json()


@router.get("")
async def get_plot_samples(
    request: Request,
    response: Response,
    *,
    filter: str = None,
    sort: str = None,
    range: str = None,
    client: httpx.AsyncClient = Depends(get_async_client),
) -> Any:
    """Get all plot_samples"""
    res = await client.get(
        f"{config.SOIL_API_URL}/v1/plot_samples",
        params={"sort": sort, "range": range, "filter": filter},
    )
    response.headers["Access-Control-Expose-Headers"] = "Content-Range"
    response.headers["Content-Range"] = res.headers["Content-Range"]

    return res.json()


@router.post("")
async def create_plot_sample(
    plot_sample: Any = Body(...),
    client: httpx.AsyncClient = Depends(get_async_client),
    user: User = Depends(require_admin),
) -> Any:
    """Creates a plot samples"""

    res = await client.post(
        f"{config.SOIL_API_URL}/v1/plot_samples",
        json=plot_sample,
    )

    return res.json()


@router.put("/{plot_sample_id}")
async def update_plot_sample(
    plot_sample_id: UUID,
    plot_sample: Any = Body(...),
    client: httpx.AsyncClient = Depends(get_async_client),
    user: User = Depends(require_admin),
) -> Any:
    """ "Updates a plot samples by id"""

    res = await client.put(
        f"{config.SOIL_API_URL}/v1/plot_samples/{plot_sample_id}",
        json=plot_sample,
    )

    return res.json()


@router.delete("/{plot_sample_id}")
async def delete_plot_sample(
    plot_sample_id: UUID,
    client: httpx.AsyncClient = Depends(get_async_client),
    user: User = Depends(require_admin),
) -> None:
    """Delete a plot samples by id"""

    res = await client.delete(
        f"{config.SOIL_API_URL}/v1/plot_samples/{plot_sample_id}"
    )

    return res.json()
