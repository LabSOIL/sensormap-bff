""" Routes to /soil_profiles are routed to /soil/profiles

    See the _reverse_proxy function in app/tools/proxy.py for more details
"""

from typing import Any
from fastapi import Depends, APIRouter
from uuid import UUID
from app.models.user import User
from app.tools.auth import require_admin
from app.tools.proxy import _reverse_proxy


router = APIRouter()


@router.get("/{soil_profiles_id}")
async def get_soil_profile(
    soil_profiles_id: UUID,
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:
    """Get a soil profile by id"""

    return reverse_proxy


@router.get("")
async def get_soil_profiles(
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:
    """Get all soil_profiles"""

    return reverse_proxy


@router.post("")
async def create_soil_profiles(
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:
    """Creates a soil profile"""

    return reverse_proxy


@router.put("/{soil_profiles_id}")
async def update_soil_profiles(
    soil_profiles_id: UUID,
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> Any:
    """Updates many soil profiles"""

    return reverse_proxy


@router.delete("/batch")
async def delete_batch(
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> None:
    """Delete by a list of ids"""

    return reverse_proxy


@router.delete("/{soil_profiles_id}")
async def delete_soil_profiles(
    soil_profiles_id: UUID,
    reverse_proxy: Any = Depends(_reverse_proxy),
    user: User = Depends(require_admin),
) -> None:
    """Delete a soil profile by id"""

    return reverse_proxy
