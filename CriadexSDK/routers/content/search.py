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


class IndexContentSearchRoute(Route):

    class Response(BaseResponse):
        response: Optional[IndexSearchResponse]

    @outputs(Response)
    async def execute(self, index_name: str, prompt: str, top_k: int) -> Optional[dict]:

        return await self._post(
            path=f"/criadex/{index_name}/content/search",
            json=(
                {
                    "prompt": prompt,
                    "top_k": top_k
                }
            )
        )
