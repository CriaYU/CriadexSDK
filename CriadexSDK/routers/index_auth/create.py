from typing import Optional

from CriadexSDK.core.api.route import Route, BaseResponse, outputs


class IndexAuthCreateRoute(Route):

    class Response(BaseResponse):
        pass

    @outputs(Response)
    async def execute(self, index_name: str, api_key: str) -> Optional[dict]:

        return await self._post(
            path=f"/index_auth/{index_name}/create",
            params={"index_name": index_name, "api_key": api_key}
        )
