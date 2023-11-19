from typing import Optional, List

from pydantic import BaseModel

from CriadexSDK.core.api.route import Route, BaseResponse, outputs
from CriadexSDK.routers.manage.about import IndexInfo


class IndexAuthListRoute(Route):

    class Response(BaseResponse):
        indexes: List[IndexInfo]

    @outputs(Response)
    async def execute(self, api_key: str) -> Optional[dict]:

        return await self._get(
            path=f"/index_auth/list",
            params={"api_key": api_key}
        )
