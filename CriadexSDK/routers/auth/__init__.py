from CriadexSDK.routers.auth.check import AuthCheckRoute
from CriadexSDK.routers.auth.create import AuthCreateRoute
from CriadexSDK.routers.auth.delete import AuthDeleteRoute
from CriadexSDK.core.api.router import Router


class AuthRouter(Router):

    def __init__(self, api_base: str, api_key: str):
        super().__init__(api_base, api_key)
       
        self.check: AuthCheckRoute = self._create_route(AuthCheckRoute)
        self.create: AuthCreateRoute = self._create_route(AuthCreateRoute)
        self.delete: AuthDeleteRoute = self._create_route(AuthDeleteRoute)



__all__ = ["AuthRouter"]