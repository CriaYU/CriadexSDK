from httpx import AsyncClient

from CriadexSDK.core.api.router import Router
from CriadexSDK.routers.models.about import ModelAboutRoute
from CriadexSDK.routers.models.create import ModelCreateRoute
from CriadexSDK.routers.models.delete import ModelDeleteRoute
from CriadexSDK.routers.models.update import ModelUpdateRoute


class ModelsRouter(Router):

    def __init__(self, api_base: str, http: AsyncClient):
        super().__init__(api_base, http)

        self.delete: ModelDeleteRoute = self._create_route(ModelDeleteRoute)
        self.create: ModelCreateRoute = self._create_route(ModelCreateRoute)
        self.about: ModelAboutRoute = self._create_route(ModelAboutRoute)
        self.update: ModelUpdateRoute = self._create_route(ModelUpdateRoute)


__all__ = ["ModelsRouter"]
