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


@router.get("/{sensor_id}")
async def get_sensor(
    sensor_id: UUID,
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:
    """Get a sensor by id"""
    return reverse_proxy


@router.get("")
async def get_sensors(
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:
    """Get all sensors"""

    return reverse_proxy


@router.post("")
async def create_sensor(
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:
    """Creates an sensor"""

    return reverse_proxy


@router.post("")
async def create_many_sensors(
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:
    """Creates an sensor"""

    return reverse_proxy


@router.put("/{sensor_id}")
async def update_sensor(
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:
    """ "Updates an sensor by id"""

    return reverse_proxy


@router.delete("/batch")
async def delete_batch(
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> None:
    """Delete by a list of ids"""

    return reverse_proxy


@router.delete("/{sensor_id}")
async def delete_sensor(
    sensor_id: UUID,
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> None:
    """Delete an sensor by id"""

    return reverse_proxy
