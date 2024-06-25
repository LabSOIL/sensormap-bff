from typing import Any
from fastapi import Depends, APIRouter
from uuid import UUID
from app.models.user import User
from app.tools.auth import require_admin
from app.tools.proxy import _reverse_proxy


router = APIRouter()


@router.get("/{sensordata_id}")
async def get_sensordata(
    sensordata_id: UUID,
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:
    """Get an individual sensordata record by id"""

    return reverse_proxy


@router.get("")
async def get_all_sensordata(
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:
    """Get all sensordata"""

    return reverse_proxy


@router.post("")
async def create_sensordata(
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:
    """Creates an sensordata record"""

    return reverse_proxy


@router.put("/{sensordata_id}")
async def update_sensordata(
    sensordata_id: UUID,
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:
    """Updates an individual sensordata record by id"""

    return reverse_proxy


@router.delete("/batch")
async def delete_batch(
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> None:
    """Delete by a list of ids"""

    return reverse_proxy


@router.delete("/{sensordata_id}")
async def delete_sensor(
    sensordata_id: UUID,
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> None:
    """Delete an individual sensordata record by id"""

    return reverse_proxy
