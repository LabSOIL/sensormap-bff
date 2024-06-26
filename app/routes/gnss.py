from typing import Any
from fastapi import Depends, APIRouter
from uuid import UUID
from app.models.user import User
from app.tools.auth import require_admin

from app.tools.proxy import _reverse_proxy

router = APIRouter()


@router.get("/{gnss_id}")
async def get_gnss(
    gnss_id: UUID,
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:
    """Get an gnss by id"""

    return reverse_proxy


@router.get("")
async def get_all_gnss(
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:
    """Get all gnss"""

    return reverse_proxy


@router.post("")
async def create_gnss(
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:
    """Creates an gnss"""

    return reverse_proxy


@router.put("/{gnss_id}")
async def update_gnss(
    gnss_id: UUID,
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:
    """Updates an gnss by id"""

    return reverse_proxy


@router.delete("/batch")
async def delete_batch(
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> None:
    """Delete by a list of ids"""

    return reverse_proxy


@router.delete("/{gnss_id}")
async def delete_gnss(
    gnss_id: UUID,
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> None:
    """Delete an gnss by id"""

    return reverse_proxy
