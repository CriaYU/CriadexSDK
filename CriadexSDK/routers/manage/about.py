from typing import Optional

from CriadexSDK.core.api.route import Route, BaseResponse, outputs


class IndexAboutRoute(Route):

    class Response(BaseResponse):
        info: Optional[dict]

    @outputs(Response)
    async def execute(self, index_name: str) -> Optional[dict]:

        return await self._get(
            path=f"/criadex/{index_name}/about"
        )
