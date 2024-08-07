from typing import Any
from fastapi import Depends, APIRouter
from uuid import UUID
from app.models.user import User
from app.tools.auth import require_admin

from app.tools.proxy import _reverse_proxy

router = APIRouter()


@router.get("/{plot_id}")
async def get_plot(
    plot_id: UUID,
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:
    """Get an plot by id"""

    return reverse_proxy


@router.get("")
async def get_plots(
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:
    """Get all plots"""

    return reverse_proxy


@router.post("")
async def create_plot(
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:
    """Creates an plot"""

    return reverse_proxy


@router.post("/batch")
async def create_plot_sample_batch(
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:
    """Creates a plot samples from a batch import"""

    return reverse_proxy


@router.put("/batch")
async def update_many(
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:
    """Updates an plot by id"""

    return reverse_proxy


@router.put("/{plot_id}")
async def update_plot(
    plot_id: UUID,
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:
    """Updates an plot by id"""

    return reverse_proxy


@router.delete("/batch")
async def delete_batch(
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> None:
    """Delete by a list of ids"""

    return reverse_proxy


@router.delete("/{plot_id}")
async def delete_plot(
    plot_id: UUID,
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> None:
    """Delete an plot by id"""

    return reverse_proxy
