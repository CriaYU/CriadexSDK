from httpx import AsyncClient

from CriadexSDK.core.api.router import Router
from CriadexSDK.routers.content.delete import IndexContentDeleteRoute
from CriadexSDK.routers.content.list import IndexContentListRoute
from CriadexSDK.routers.content.search import IndexContentSearchRoute
from CriadexSDK.routers.content.update import IndexContentUpdateRoute
from CriadexSDK.routers.content.upload import IndexContentUploadRoute


class ContentRouter(Router):

    def __init__(self, api_base: str, http: AsyncClient):
        super().__init__(api_base, http)

        self.upload: IndexContentUploadRoute = self._create_route(IndexContentUploadRoute)
        self.update: IndexContentUpdateRoute = self._create_route(IndexContentUpdateRoute)
        self.delete: IndexContentDeleteRoute = self._create_route(IndexContentDeleteRoute)
        self.list: IndexContentListRoute = self._create_route(IndexContentListRoute)
        self.search: IndexContentSearchRoute = self._create_route(IndexContentSearchRoute)


__all__ = ["ContentRouter"]
