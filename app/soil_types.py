from typing import Any
from fastapi import Depends, APIRouter, Query, Response, Body
from app.config import config
from app.utils import get_async_client
import httpx
from uuid import UUID
from app.models.user import User
from app.auth import require_admin

router = APIRouter()


@router.get("/{soil_type_id}")
async def get_soil_type(
    client: httpx.AsyncClient = Depends(get_async_client),
    *,
    soil_type_id: UUID,
) -> Any:
    """Get a soil_type by id"""

    res = await client.get(
        f"{config.SOIL_API_URL}/v1/soil/types/{soil_type_id}",
    )

    return res.json()


@router.get("")
async def get_soil_types(
    response: Response,
    *,
    filter: str = Query(None),
    sort: str = Query(None),
    range: str = Query(None),
    client: httpx.AsyncClient = Depends(get_async_client),
) -> Any:
    """Get all soil_types"""

    res = await client.get(
        f"{config.SOIL_API_URL}/v1/soil/types",
        params={"sort": sort, "range": range, "filter": filter},
    )
    response.headers["Access-Control-Expose-Headers"] = "Content-Range"
    response.headers["Content-Range"] = res.headers["Content-Range"]

    return res.json()


@router.post("")
async def create_soil_type(
    soil_type: Any = Body(...),
    client: httpx.AsyncClient = Depends(get_async_client),
    user: User = Depends(require_admin),
) -> Any:
    """Creates an soil_type"""

    res = await client.post(
        f"{config.SOIL_API_URL}/v1/soil/types",
        json=soil_type,
    )

    return res.json()


@router.put("/{soil_type_id}")
async def update_soil_type(
    soil_type_id: UUID,
    soil_type: Any = Body(...),
    client: httpx.AsyncClient = Depends(get_async_client),
    user: User = Depends(require_admin),
) -> Any:
    """ "Updates an soil_type by id"""

    res = await client.put(
        f"{config.SOIL_API_URL}/v1/soil/types/{soil_type_id}",
        json=soil_type,
    )

    return res.json()


@router.delete("/{soil_type_id}")
async def delete_soil_type(
    soil_type_id: UUID,
    client: httpx.AsyncClient = Depends(get_async_client),
    user: User = Depends(require_admin),
) -> None:
    """Delete an soil_type by id"""

    res = await client.delete(
        f"{config.SOIL_API_URL}/v1/soil/types/{soil_type_id}"
    )

    return res.json()
