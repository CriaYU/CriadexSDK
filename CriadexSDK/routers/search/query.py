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


class IndexQueryResponse(BaseModel):
    nodes: List[NodeWithScore]
    token_usage: List[TokenUsage]


class IndexQueryRoute(Route):

    class Response(BaseResponse):
        response: Optional[IndexQueryResponse]

    @outputs(Response)
    async def execute(self, index_name: str, prompt: str, top_k: Optional[int] = None) -> Optional[dict]:

        return await self._post(
            path=f"/criadex/{index_name}/search",
            json=(
                {
                    "prompt": prompt,
                    "top_k": top_k
                }
            )
        )
