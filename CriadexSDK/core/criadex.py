from typing import Optional

from httpx import Response

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

    def __init__(self, api_base: str):
        # Remove trailing slash
        self._api_base: str = (api_base[:-1] if api_base.endswith("/") else api_base)

        # Routers
        self.content: Optional[ContentRouter] = None
        self.manage: Optional[ManageRouter] = None
        self.auth: Optional[AuthRouter] = None
        self.index_auth: Optional[IndexAuthRouter] = None
        self.models: Optional[ModelsRouter] = None

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

        self._include_routers(api_key=api_key)

    async def is_master(self, api_key: str) -> bool:
        """
        Check if an api_key has access to the /check endpoint (which requires a master key)

        :param api_key: The Criadex api key
        :return: Whether it's authorized

        """

        async with create_httpx_client() as client:
            response: Response = await client.get(
                self._api_base + f"/auth/{api_key}/check",
                headers={"x-api-key": api_key}
            )

            return response.status_code != 401

    def _include_routers(self, api_key: str) -> None:
        """
        Set up the CriadexSDK routers with a validated api key

        :param api_key: The api key
        :return: None

        """

        router_kwargs: dict = {"api_base": self._api_base, "api_key": api_key}

        self.content: ContentRouter = ContentRouter(**router_kwargs)
        self.manage: ManageRouter = ManageRouter(**router_kwargs)
        self.auth: AuthRouter = AuthRouter(**router_kwargs)
        self.index_auth: IndexAuthRouter = IndexAuthRouter(**router_kwargs)
        self.models: ModelsRouter = ModelsRouter(**router_kwargs)
