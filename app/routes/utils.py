import httpx
from fastapi import FastAPI, Request
from starlette.background import BackgroundTask
from fastapi.responses import StreamingResponse
from contextlib import asynccontextmanager
from app.config import config
from typing import Any
from fastapi import Depends, APIRouter
from app.models.user import User
from app.tools.auth import get_user_info
from app.tools.proxy import _reverse_proxy

router = APIRouter()


@router.get("/slope")
async def get_slope_class(
    reverse_proxy: Any = Depends(_reverse_proxy),
    # user: User = Depends(get_user_info),
) -> Any:
    """Get slope class"""

    return reverse_proxy
