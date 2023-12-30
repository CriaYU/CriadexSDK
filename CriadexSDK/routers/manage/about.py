from typing import Optional

from pydantic import BaseModel

from CriadexSDK.core.api.route import Route, BaseResponse, outputs


class GroupInfo(BaseModel):
    id: int
    name: str
    type: int
    llm_model_id: int
    embedding_model_id: int
    created: str


class GroupAboutRoute(Route):
    class Response(BaseResponse):
        info: Optional[GroupInfo]

    @outputs(Response)
    async def execute(self, group_name: str) -> Optional[dict]:
        return await self._get(
            path=f"/criadex/{group_name}/about"
        )
