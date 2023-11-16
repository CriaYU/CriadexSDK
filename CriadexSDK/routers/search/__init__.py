from CriadexSDK.routers.search.query import IndexQueryRoute
from CriadexSDK.core.api.router import Router


class SearchRouter(Router):

    def __init__(self, api_base: str, api_key: str):
        super().__init__(api_base, api_key)

        self.query: IndexQueryRoute = IndexQueryRoute(
            http=self._http,
            api_base=api_base
        )


__all__ = ["SearchRouter"]