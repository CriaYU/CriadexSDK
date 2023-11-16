from typing import List, Tuple, Type, TypeVar

from httpx import AsyncClient

from CriadexSDK.core.api.route import Route

T = TypeVar('T', bound=Route)


class Router:

    def __init__(
        self,
        api_base: str,
        api_key: str
    ):

        self._api_base: str = api_base
        self._http: AsyncClient = AsyncClient(headers={
            "x-api-key": api_key
        })

        pass

    def _create_route(self, route: Type[T]) -> T:

        return route(api_base=self._api_base, http=self._http)



