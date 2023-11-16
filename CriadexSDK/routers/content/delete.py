from typing import Optional

from CriadexSDK.core.api.route import Route, BaseResponse, outputs


class IndexContentDeleteRoute(Route):

    class Response(BaseResponse):
        pass

    @outputs(Response)
    async def execute(self, index_name: str, document_name: str) -> Optional[dict]:

        return await self._delete(
            path=f"/criadex/{index_name}/content/delete",
            params={"document_name": document_name}
        )
