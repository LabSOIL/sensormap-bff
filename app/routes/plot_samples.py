from typing import Any
from fastapi import Depends, APIRouter
from uuid import UUID
from app.models.user import User
from app.tools.auth import require_admin
from app.tools.proxy import _reverse_proxy


router = APIRouter()


@router.get("/{plot_sample_id}")
async def get_plot_sample(
    plot_sample_id: UUID,
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:
    """Get a plot samples by id"""

    return reverse_proxy


@router.get("")
async def get_plot_samples(
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:
    """Get all plot_samples"""

    return reverse_proxy


@router.post("")
async def create_plot_sample(
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:
    """Creates a plot samples"""

    return reverse_proxy


@router.post("/batch")
async def create_plot_batch(
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:
    """Creates plots from a batch import"""

    return reverse_proxy


@router.put("/{plot_sample_id}")
async def update_plot_sample(
    plot_sample_id: UUID,
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:
    """ "Updates a plot samples by id"""

    return reverse_proxy


@router.delete("/batch")
async def delete_batch(
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> None:
    """Delete by a list of ids"""

    return reverse_proxy


@router.delete("/{plot_sample_id}")
async def delete_plot_sample(
    plot_sample_id: UUID,
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> None:
    """Delete a plot samples by id"""

    return reverse_proxy
