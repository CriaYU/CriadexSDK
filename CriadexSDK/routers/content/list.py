from typing import Optional, List

from CriadexSDK.core.api.route import Route, BaseResponse, outputs


class IndexContentListRoute(Route):

    class Response(BaseResponse):
        files: List[str]

    @outputs(Response)
    async def execute(self, index_name: str) -> Optional[dict]:

        return await self._get(
            path=f"/criadex/{index_name}/content/list"
        )
