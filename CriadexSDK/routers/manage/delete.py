from typing import Optional

from CriadexSDK.core.api.route import Route, BaseResponse, outputs


class IndexDeleteRoute(Route):

    class Response(BaseResponse):
        pass

    @outputs(Response)
    async def execute(self, index_name: str) -> Optional[dict]:

        return await self._delete(
            path=f"/criadex/{index_name}/delete"
        )
