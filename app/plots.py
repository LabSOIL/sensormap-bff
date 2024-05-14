from typing import Any
from fastapi import Depends, APIRouter, Response, Body, Request
from app.config import config
from app.utils import get_async_client
import httpx
from uuid import UUID
from app.models.user import User
from app.auth import require_admin
from app.utils import _reverse_proxy

router = APIRouter()


@router.get("/{plot_id}")
async def get_plot(
    client: httpx.AsyncClient = Depends(get_async_client),
    *,
    plot_id: UUID,
) -> Any:
    """Get an plot by id"""

    res = await client.get(
        f"{config.SOIL_API_URL}/v1/plots/{plot_id}",
    )

    return res.json()


@router.get("")
async def get_plots(
    request: Request,
    response: Response,
    *,
    filter: str = None,
    sort: str = None,
    range: str = None,
    client: httpx.AsyncClient = Depends(get_async_client),
) -> Any:
    """Get all plots"""
    res = await client.get(
        f"{config.SOIL_API_URL}/v1/plots",
        params={"sort": sort, "range": range, "filter": filter},
    )
    response.headers["Access-Control-Expose-Headers"] = "Content-Range"
    response.headers["Content-Range"] = res.headers["Content-Range"]

    return res.json()


@router.post("")
async def create_plot(
    plot: Any = Body(...),
    client: httpx.AsyncClient = Depends(get_async_client),
    user: User = Depends(require_admin),
) -> Any:
    """Creates an plot"""

    res = await client.post(
        f"{config.SOIL_API_URL}/v1/plots",
        json=plot,
    )

    return res.json()


@router.post("/batch")
async def create_plot_sample_batch(
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:
    """Creates a plot samples from a batch import"""

    return reverse_proxy


@router.put("/{plot_id}")
async def update_plot(
    plot_id: UUID,
    plot: Any = Body(...),
    client: httpx.AsyncClient = Depends(get_async_client),
    user: User = Depends(require_admin),
) -> Any:
    """ "Updates an plot by id"""

    res = await client.put(
        f"{config.SOIL_API_URL}/v1/plots/{plot_id}", json=plot
    )

    return res.json()


@router.delete("/{plot_id}")
async def delete_plot(
    plot_id: UUID,
    client: httpx.AsyncClient = Depends(get_async_client),
    user: User = Depends(require_admin),
) -> None:
    """Delete an plot by id"""

    res = await client.delete(f"{config.SOIL_API_URL}/v1/plots/{plot_id}")

    return res.json()
