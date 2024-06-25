from typing import Any
from fastapi import Depends, APIRouter, Query, Response, Body
from app.config import config
from app.tools.proxy import get_async_client
import httpx
from uuid import UUID
from app.models.user import User
from app.tools.auth import require_admin
from app.tools.proxy import _reverse_proxy


router = APIRouter()


@router.get("/{soil_type_id}")
async def get_soil_type(
    soil_type_id: UUID,
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:
    """Get a soil_type by id"""

    return reverse_proxy


@router.get("")
async def get_soil_types(
    response: Response,
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:
    """Get all soil_types"""

    return reverse_proxy


@router.post("")
async def create_soil_type(
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:
    """Creates an soil_type"""

    return reverse_proxy


@router.put("/{soil_type_id}")
async def update_soil_type(
    soil_type_id: UUID,
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:
    """ "Updates an soil_type by id"""

    return reverse_proxy


@router.delete("/batch")
async def delete_batch(
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> None:
    """Delete by a list of ids"""

    return reverse_proxy


@router.delete("/{soil_type_id}")
async def delete_soil_type(
    soil_type_id: UUID,
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> None:
    """Delete an soil_type by id"""

    return reverse_proxy
