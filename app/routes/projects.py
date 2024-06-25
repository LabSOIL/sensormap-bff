from typing import Any
from fastapi import Depends, APIRouter
from uuid import UUID
from app.models.user import User
from app.tools.auth import require_admin
from app.tools.proxy import _reverse_proxy


router = APIRouter()


@router.get("/{project_id}")
async def get_project(
    project_id: UUID,
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:
    """Get a project by id"""

    return reverse_proxy


@router.get("")
async def get_projects(
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:
    """Get all projects"""

    return reverse_proxy


@router.post("")
async def create_project(
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:
    """Creates a project"""

    return reverse_proxy


@router.post("")
async def create_many_projects(
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:
    """Creates a project"""

    return reverse_proxy


@router.put("/{project_id}")
async def update_project(
    project_id: UUID,
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:
    """Updates a project by id"""

    return reverse_proxy


@router.delete("/batch")
async def delete_batch(
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> None:
    """Delete by a list of ids"""

    return reverse_proxy


@router.delete("/{project_id}")
async def delete_project(
    project_id: UUID,
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> None:
    """Delete a project by id"""

    return reverse_proxy
