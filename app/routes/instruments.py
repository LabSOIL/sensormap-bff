from typing import Any
from fastapi import Depends, APIRouter
from uuid import UUID
from app.models.user import User
from app.tools.auth import require_admin

from app.tools.proxy import _reverse_proxy

router = APIRouter()


@router.get("/{instrument_id}")
async def get_instrument(
    instrument_id: UUID,
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:
    """Get an instrument by id"""

    return reverse_proxy


@router.get("/{instrument_id}/raw")
async def get_instrument_raw_data(
    instrument_id: UUID,
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:

    return reverse_proxy


@router.get("/{instrument_id}/filtered")
async def get_instrument_baseline_filtered_data(
    instrument_id: UUID,
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:

    return reverse_proxy


@router.get("/{instrument_id}/summary")
async def get_instrument_summary(
    instrument_id: UUID,
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:

    return reverse_proxy


@router.get("")
async def get_instruments(
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:
    """Get all instruments"""

    return reverse_proxy


@router.post("")
async def create_instrument(
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:
    """Creates an instrument"""

    return reverse_proxy


@router.post("/batch")
async def create_instrument_sample_batch(
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:
    """Creates an instrument from a batch import"""

    return reverse_proxy


@router.put("/{instrument_id}")
async def update_instrument(
    instrument_id: UUID,
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:
    """ "Updates an instrument by id"""

    return reverse_proxy


@router.delete("/batch")
async def delete_batch(
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> None:
    """Delete by a list of ids"""

    return reverse_proxy


@router.delete("/{instrument_id}")
async def delete_instrument(
    instrument_id: UUID,
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> None:
    """Delete an instrument by id"""

    return reverse_proxy
