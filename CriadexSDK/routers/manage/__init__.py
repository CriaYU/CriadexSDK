from httpx import AsyncClient

from CriadexSDK.core.api.router import Router
from CriadexSDK.routers.manage.about import IndexAboutRoute
from CriadexSDK.routers.manage.create import IndexCreateRoute
from CriadexSDK.routers.manage.delete import IndexDeleteRoute


class ManageRouter(Router):

    def __init__(self, api_base: str, http: AsyncClient):
        super().__init__(api_base, http)

        self.about: IndexAboutRoute = self._create_route(IndexAboutRoute)
        self.delete: IndexDeleteRoute = self._create_route(IndexDeleteRoute)
        self.create: IndexCreateRoute = self._create_route(IndexCreateRoute)


__all__ = ["ManageRouter"]
