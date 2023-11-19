from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from CriadexSDK.core.api.route import Route, BaseResponse, outputs


class IndexInfo(BaseModel):
    id: int
    name: str
    type: int
    llm_model_id: int
    embedding_model_id: int
    created: str


class IndexAboutRoute(Route):

    class Response(BaseResponse):
        info: Optional[IndexInfo]

    @outputs(Response)
    async def execute(self, index_name: str) -> Optional[dict]:

        return await self._get(
            path=f"/criadex/{index_name}/about"
        )
