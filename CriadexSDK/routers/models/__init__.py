from CriadexSDK.routers.models.about import ModelAboutRoute
from CriadexSDK.routers.models.create import ModelCreateRoute
from CriadexSDK.routers.models.delete import ModelDeleteRoute
from CriadexSDK.routers.models.query import ModelQueryRoute
from CriadexSDK.core.api.router import Router


class ModelsRouter(Router):

    def __init__(self, api_base: str, api_key: str):
        super().__init__(api_base, api_key)

        self.query: ModelQueryRoute = self._create_route(ModelQueryRoute)
        self.delete: ModelDeleteRoute = self._create_route(ModelDeleteRoute)
        self.create: ModelCreateRoute = self._create_route(ModelCreateRoute)
        self.about: ModelAboutRoute = self._create_route(ModelAboutRoute)

__all__ = ["ModelsRouter"]
