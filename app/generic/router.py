from fastapi import (
    Depends,
    APIRouter,
    HTTPException,
    Request,
    status,
)
from typing import Any
from uuid import UUID
from app.config import config
from app.utils import get_async_client
from app.models.user import User
from app.auth import require_admin
import httpx
from fastapi.responses import StreamingResponse
from starlette.background import BackgroundTask


class ReactAdminBFFRouter:
    def __init__(
        self,
        name_singular: str,
        name_plural: str = None,
        prefix: str = None,
    ):
        self.name_singular = name_singular
        self.name_plural = name_plural or f"{name_singular}s"
        self.router = APIRouter()
        self.prefix = (
            prefix
            if prefix
            else f"/{self.name_plural.replace(' ', '_').lower()}"
        )
        self.tags = [self.name_plural]
        self.machine_name = self.name_plural.lower().replace(" ", "_")

        # English stuff, "an" or "a" depending on first letter of singular name
        a_or_an = "an" if self.name_singular[0].lower() in "aeiou" else "a"

        # Routes
        self.router.add_api_route(
            "/{id}",
            self.get_one,
            methods=["GET"],
            name=f"Get {a_or_an} {self.name_singular}",
            description=f"Get a single {self.name_singular} by its id",
        )
        self.router.add_api_route(
            "",
            self.get_many,
            methods=["GET"],
            name=f"Get {self.name_plural}",
            description=f"Get multiple {self.name_plural}",
        )
        self.router.add_api_route(
            "",
            self.create,
            methods=["POST"],
            name=f"Create {a_or_an} {self.name_singular}",
            description=f"Create a new {self.name_singular}",
        )
        self.router.add_api_route(
            "/{id}",
            self.update,
            methods=["PUT"],
            name=f"Update {a_or_an} {self.name_singular}",
            description=f"Update a {self.name_singular} by its id",
        )
        self.router.add_api_route(
            "/{id}",
            self.delete,
            methods=["DELETE"],
            name=f"Delete {a_or_an} {self.name_singular}",
            description=f"Delete a {self.name_singular} by its id",
        )

    async def update(
        self,
        id: UUID,
        request: Request,
        client: httpx.AsyncClient = Depends(get_async_client),
        user: User = Depends(require_admin),
    ) -> Any:

        try:
            URL = f"{config.SOIL_API_URL}/v1/{self.name_plural}/{id}"
            req = client.build_request(
                "PUT",
                URL,
                headers=request.headers.raw,
                content=request.stream(),
            )
            r = await client.send(req, stream=True)
            return StreamingResponse(
                r.aiter_raw(),
                status_code=r.status_code,
                headers=r.headers,
                background=BackgroundTask(r.aclose),
            )

        except httpx.HTTPStatusError as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=e.response.text,
            )

    async def delete(
        self,
        id: UUID,
        request: Request,
        client: httpx.AsyncClient = Depends(get_async_client),
        user: User = Depends(require_admin),
    ) -> None:
        try:
            URL = f"{config.SOIL_API_URL}/v1/{self.name_plural}/{id}"
            req = client.build_request(
                "DELETE",
                URL,
                headers=request.headers.raw,
                content=request.stream(),
            )
            r = await client.send(req, stream=True)
            return StreamingResponse(
                r.aiter_raw(),
                status_code=r.status_code,
                headers=r.headers,
                background=BackgroundTask(r.aclose),
            )

        except httpx.HTTPStatusError as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=e.response.text,
            )

    async def create(
        self,
        request: Request,
        client: httpx.AsyncClient = Depends(get_async_client),
        user: User = Depends(require_admin),
    ) -> Any:

        try:
            URL = f"{config.SOIL_API_URL}/v1/{self.name_plural}"
            req = client.build_request(
                "POST",
                URL,
                headers=request.headers.raw,
                content=request.stream(),
            )
            r = await client.send(req, stream=True)
            return StreamingResponse(
                r.aiter_raw(),
                status_code=r.status_code,
                headers=r.headers,
                background=BackgroundTask(r.aclose),
            )

        except httpx.HTTPStatusError as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=e.response.text,
            )

    async def get_one(
        self,
        id: UUID,
        request: Request,
        client: httpx.AsyncClient = Depends(get_async_client),
        user: User = Depends(require_admin),
    ) -> Any:

        try:
            URL = f"{config.SOIL_API_URL}/v1/{self.name_plural}/{id}"
            req = client.build_request(
                "GET",
                URL,
                headers=request.headers.raw,
                content=request.stream(),
            )
            r = await client.send(req, stream=True)
            return StreamingResponse(
                r.aiter_raw(),
                status_code=r.status_code,
                headers=r.headers,
                background=BackgroundTask(r.aclose),
            )

        except httpx.HTTPStatusError as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=e.response.text,
            )

    async def get_many(
        self,
        request: Request,
        client: httpx.AsyncClient = Depends(get_async_client),
        user: User = Depends(require_admin),
    ) -> Any:

        try:
            URL = f"{config.SOIL_API_URL}/v1/{self.name_plural}"
            req = client.build_request(
                "GET",
                URL,
                headers=request.headers.raw,
                content=request.stream(),
            )
            r = await client.send(req, stream=True)
            return StreamingResponse(
                r.aiter_raw(),
                status_code=r.status_code,
                headers=r.headers,
                background=BackgroundTask(r.aclose),
            )

        except httpx.HTTPStatusError as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=e.response.text,
            )
