from typing import Optional, Literal

from pydantic import BaseModel

from CriadexSDK.core.api.route import Route, BaseResponse, outputs


class PartialIndexConfig(BaseModel):
    type: Literal["DOCUMENT", "QUESTION", "CACHE"]
    llm_model_id: int
    embedding_model_id: int


class IndexConfig(PartialIndexConfig):
    name: str


class IndexCreateRoute(Route):

    class Response(BaseResponse):
        config: Optional[IndexConfig]

    @outputs(Response)
    async def execute(self, index_name: str, index_config: PartialIndexConfig) -> Optional[dict]:

        return await self._post(
            path=f"/criadex/{index_name}/create",
            json=index_config
        )
