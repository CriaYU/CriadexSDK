from typing import Optional

from CriadexSDK.core.api.route import Route, BaseResponse, outputs


class IndexAuthCheckRoute(Route):
    class Response(BaseResponse):
        authorized: Optional[bool]

    @outputs(Response)
    async def execute(self, index_name: str, api_key: str) -> Optional[dict]:
        return await self._get(
            path=f"/index_auth/{index_name}/check",
            params={"index_name": index_name, "api_key": api_key}
        )
