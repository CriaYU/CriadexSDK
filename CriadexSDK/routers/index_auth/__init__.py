from httpx import AsyncClient

from CriadexSDK.core.api.router import Router
from CriadexSDK.routers.index_auth.check import IndexAuthCheckRoute
from CriadexSDK.routers.index_auth.create import IndexAuthCreateRoute
from CriadexSDK.routers.index_auth.delete import IndexAuthDeleteRoute
from CriadexSDK.routers.index_auth.list import IndexAuthListRoute


class IndexAuthRouter(Router):

    def __init__(self, api_base: str, http: AsyncClient):
        super().__init__(api_base, http)

        self.check: IndexAuthCheckRoute = self._create_route(IndexAuthCheckRoute)
        self.create: IndexAuthCreateRoute = self._create_route(IndexAuthCreateRoute)
        self.delete: IndexAuthDeleteRoute = self._create_route(IndexAuthDeleteRoute)
        self.list: IndexAuthListRoute = self._create_route(IndexAuthListRoute)


__all__ = ["IndexAuthRouter"]
