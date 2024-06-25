from typing import Any
from fastapi import Depends, APIRouter
from uuid import UUID
from app.models.user import User
from app.tools.auth import require_admin

from app.tools.proxy import _reverse_proxy

router = APIRouter()


@router.get("/{transect_id}")
async def get_transect(
    transect_id: UUID,
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:
    """Get a transect by id"""

    return reverse_proxy


@router.get("")
async def get_transects(
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:
    """Get all transects"""

    return reverse_proxy


@router.post("")
async def create_transect(
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:
    """Creates a transect"""

    return reverse_proxy


@router.post("/batch")
async def create_transect_sample_batch(
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:
    """Creates a transect samples from a batch import"""

    return reverse_proxy


@router.put("/{transect_id}")
async def update_transect(
    transect_id: UUID,
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:
    """ "Updates a transect by id"""

    return reverse_proxy


@router.delete("/{transect_id}")
async def delete_transect(
    transect_id: UUID,
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> None:
    """Delete a transect by id"""

    return reverse_proxy
