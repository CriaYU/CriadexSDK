import asyncio
from typing import Optional

from httpx import Response, AsyncClient

from CriadexSDK.core.network import create_httpx_client
from CriadexSDK.core.schemas import CriadexUnauthorizedError
from CriadexSDK.routers.auth import AuthRouter
from CriadexSDK.routers.content import ContentRouter
from CriadexSDK.routers.index_auth import IndexAuthRouter
from CriadexSDK.routers.manage import ManageRouter
from CriadexSDK.routers.models import ModelsRouter


class CriadexSDK:
    """
    Wrapper for interacting with the Criadex server programmatically

    """

    def __init__(self, api_base: str, error_stacktrace: bool = True):
        """
        Initialization configuration

        :param api_base: The base API url
        :param error_stacktrace: Include stacktrace when Criadex has an internal error

        """

        # Remove trailing slash
        self._api_base: str = (api_base[:-1] if api_base.endswith("/") else api_base)

        # Routers
        self.content: Optional[ContentRouter] = None
        self.manage: Optional[ManageRouter] = None
        self.auth: Optional[AuthRouter] = None
        self.index_auth: Optional[IndexAuthRouter] = None
        self.models: Optional[ModelsRouter] = None

        # Client for requesting
        self._httpx: AsyncClient = create_httpx_client(
            error_stacktrace=error_stacktrace
        )

    def __del__(self) -> None:
        """
        When the SDK is deleted, gracefully close the async client
        :return: None

        """

        asyncio.get_running_loop().create_task(self._httpx.aclose())

    async def authenticate(self, api_key: str) -> None:
        """
        Set up routers using an api_key after checking it is valid

        :param api_key: The API key to use with Criadex
        :return: None
        :raises: CriadexUnauthorizedError

        """

        is_master: bool = await self.is_master(api_key=api_key)

        if not is_master:
            raise CriadexUnauthorizedError("You must submit a master api_key to run the Criadex SDK")

        self._include_routers()

    async def is_master(self, api_key: str) -> bool:
        """
        Check if an api_key has access to the /check endpoint (which requires a master key)

        :param api_key: The Criadex api key
        :return: Whether it's authorized

        """

        response: Response = await self._httpx.get(
            self._api_base + f"/auth/{api_key}/check",
            headers={"x-api-key": api_key}
        )

        return response.status_code != 401

    def _include_routers(self) -> None:
        """
        Set up the CriadexSDK routers with a validated api key

        :param api_key: The api key
        :return: None

        """

        router_kwargs: dict = {"api_base": self._api_base, "http": self._httpx}

        self.content: ContentRouter = ContentRouter(**router_kwargs)
        self.manage: ManageRouter = ManageRouter(**router_kwargs)
        self.auth: AuthRouter = AuthRouter(**router_kwargs)
        self.index_auth: IndexAuthRouter = IndexAuthRouter(**router_kwargs)
        self.models: ModelsRouter = ModelsRouter(**router_kwargs)
