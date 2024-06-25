from typing import Any
from fastapi import Depends, APIRouter
from app.tools.proxy import _reverse_proxy

router = APIRouter()


@router.get("/slope")
async def get_slope_class(
    reverse_proxy: Any = Depends(_reverse_proxy),
) -> Any:
    """Get slope class"""

    return reverse_proxy
