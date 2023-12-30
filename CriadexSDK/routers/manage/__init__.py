from httpx import AsyncClient

from CriadexSDK.core.api.router import Router
from CriadexSDK.routers.manage.about import GroupAboutRoute
from CriadexSDK.routers.manage.create import GroupCreateRoute
from CriadexSDK.routers.manage.delete import GroupDeleteRoute


class ManageRouter(Router):

    def __init__(self, api_base: str, http: AsyncClient):
        super().__init__(api_base, http)

        self.about: GroupAboutRoute = self._create_route(GroupAboutRoute)
        self.delete: GroupDeleteRoute = self._create_route(GroupDeleteRoute)
        self.create: GroupCreateRoute = self._create_route(GroupCreateRoute)


__all__ = ["ManageRouter"]
