from typing import List, Optional

from pydantic import BaseModel

from CriadexSDK.core.api.route import Route, BaseResponse, outputs


class TokenUsage(BaseModel):
    completion_tokens: int
    prompt_tokens: int
    total_tokens: int


class Node(BaseModel):
    metadata: dict
    text: str


class NodeWithScore(BaseModel):
    node: Node
    score: float


class IndexSearchResponse(BaseModel):
    nodes: List[NodeWithScore]
    token_usage: List[TokenUsage]


class Filter(BaseModel):
    should: Optional[List[dict]] = None
    must: Optional[List[dict]] = None
    must_not: Optional[List[dict]] = None


class SearchIndexConfig(BaseModel):
    prompt: str
    top_k: int
    search_filter: Optional[Filter] = None


class IndexContentSearchRoute(Route):
    class Response(BaseResponse):
        response: Optional[IndexSearchResponse]
        index_name: str

    @outputs(Response)
    async def execute(self, index_name: str, search_config: SearchIndexConfig) -> Optional[dict]:

        response: dict = await self._post(
            path=f"/criadex/{index_name}/content/search",
            json=search_config
        )

        response["index_name"] = index_name
        return response
