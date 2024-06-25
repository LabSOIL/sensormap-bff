from typing import Any
from fastapi import Depends, APIRouter, Query, Response, Body
from app.config import config
from app.tools.proxy import get_async_client
import httpx
from uuid import UUID
from app.models.user import User
from app.tools.auth import require_admin


router = APIRouter()


@router.get("/{project_id}")
async def get_project(
    client: httpx.AsyncClient = Depends(get_async_client),
    *,
    project_id: UUID,
) -> Any:
    """Get a project by id"""

    res = await client.get(
        f"{config.SOIL_API_URL}/v1/projects/{project_id}",
    )

    return res.json()


@router.get("")
async def get_projects(
    response: Response,
    *,
    filter: str = Query(None),
    sort: str = Query(None),
    range: str = Query(None),
    client: httpx.AsyncClient = Depends(get_async_client),
) -> Any:
    """Get all projects"""

    res = await client.get(
        f"{config.SOIL_API_URL}/v1/projects",
        params={"sort": sort, "range": range, "filter": filter},
    )
    response.headers["Access-Control-Expose-Headers"] = "Content-Range"
    response.headers["Content-Range"] = res.headers["Content-Range"]

    return res.json()


@router.post("")
async def create_project(
    project: Any = Body(...),
    client: httpx.AsyncClient = Depends(get_async_client),
    user: User = Depends(require_admin),
) -> Any:
    """Creates a project"""

    res = await client.post(
        f"{config.SOIL_API_URL}/v1/projects",
        json=project,
    )

    return res.json()


@router.post("")
async def create_many_projects(
    project: Any = Body(...),
    client: httpx.AsyncClient = Depends(get_async_client),
    user: User = Depends(require_admin),
) -> Any:
    """Creates a project"""

    res = await client.post(
        f"{config.SOIL_API_URL}/v1/projects/many",
        json=project,
    )

    return res.json()


@router.put("/{project_id}")
async def update_project(
    project_id: UUID,
    project: Any = Body(...),
    client: httpx.AsyncClient = Depends(get_async_client),
    user: User = Depends(require_admin),
) -> Any:
    """Updates a project by id"""

    res = await client.put(
        f"{config.SOIL_API_URL}/v1/projects/{project_id}", json=project
    )

    return res.json()


@router.delete("/{project_id}")
async def delete_project(
    project_id: UUID,
    client: httpx.AsyncClient = Depends(get_async_client),
    user: User = Depends(require_admin),
) -> None:
    """Delete a project by id"""

    res = await client.delete(
        f"{config.SOIL_API_URL}/v1/projects/{project_id}"
    )

    return res.json()
