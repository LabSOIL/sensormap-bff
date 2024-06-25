from typing import Any
from fastapi import Depends, APIRouter, Response, Body, Request
from app.config import config
from app.tools.proxy import get_async_client, _reverse_proxy
import httpx
from uuid import UUID
from app.models.user import User
from app.tools.auth import require_admin

router = APIRouter()


@router.get("/{area_id}")
async def get_area(
    area_id: UUID,
    reverse_proxy: Any = Depends(_reverse_proxy),
) -> Any:
    """Get an area by id"""

    return reverse_proxy


@router.get("")
async def get_areas(
    request: Request,
    response: Response,
    reverse_proxy: Any = Depends(_reverse_proxy),
) -> Any:
    """Get all areas"""

    return reverse_proxy


@router.post("")
async def create_area(
    area: Any = Body(...),
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:
    """Creates an area"""

    return reverse_proxy


@router.put("/{area_id}")
async def update_area(
    area_id: UUID,
    area: Any = Body(...),
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:
    """ "Updates an area by id"""

    return reverse_proxy


@router.delete("/{area_id}")
async def delete_area(
    area_id: UUID,
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> None:
    """Delete an area by id"""

    return reverse_proxy
