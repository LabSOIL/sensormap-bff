from typing import Any
from fastapi import Depends, APIRouter
from uuid import UUID
from app.models.user import User
from app.tools.auth import require_admin

from app.tools.proxy import _reverse_proxy

router = APIRouter()


@router.get("/{instrument_channel_id}")
async def get_instrument_channel(
    instrument_channel_id: UUID,
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:
    """Get an instrument_channel by id"""

    return reverse_proxy


@router.get("")
async def get_instrument_channels(
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:
    """Get all instrument_channel_channels"""

    return reverse_proxy


@router.post("")
async def create_instrument_channel(
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:
    """Creates an instrument_channel"""

    return reverse_proxy


@router.post("/batch")
async def create_instrument_channel_sample_batch(
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:
    """Creates an instrument_channel from a batch import"""

    return reverse_proxy


@router.put("/{instrument_channel_id}")
async def update_instrument_channel(
    instrument_channel_id: UUID,
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:
    """ "Updates an instrument_channel by id"""

    return reverse_proxy


@router.delete("/batch")
async def delete_batch(
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> None:
    """Delete by a list of ids"""

    return reverse_proxy


@router.delete("/{instrument_channel_id}")
async def delete_instrument_channel(
    instrument_channel_id: UUID,
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> None:
    """Delete an instrument_channel by id"""

    return reverse_proxy
