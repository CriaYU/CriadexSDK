from typing import List, Optional, Literal, Any

from pydantic import BaseModel

from CriadexSDK.routers.content.search import TokenUsage
from CriadexSDK.core.api.route import Route, BaseResponse, outputs


class ChatMessage(BaseModel):
    role: Literal["user", "assistant", "system"]
    content: str
    additional_kwargs: dict = dict()
    metadata: dict = dict()


class RawChatMessage(BaseModel):
    id: str
    choices: List[dict]
    created: int
    model: str
    object: str
    system_fingerprint: Any
    usage: TokenUsage


class QueryResponse(BaseModel):
    message: ChatMessage
    raw: RawChatMessage


class QueryModelParameters(BaseModel):
    max_tokens: Optional[int] = None
    temperature: Optional[float] = None
    top_p: Optional[float] = None


class QueryModelConfig(QueryModelParameters):
    history: List[ChatMessage]


class ModelQueryRoute(Route):

    class Response(BaseResponse):
        response: Optional[QueryResponse]

    @outputs(Response)
    async def execute(
        self,
        model_id: int,
        query_config: QueryModelConfig
    ) -> Optional[dict]:

        return await self._post(
            path=f"/azure/models/{model_id}/query",
            json=(
                {
                    "max_tokens": query_config.max_tokens,
                    "temperature": query_config.temperature,
                    "top_p": query_config.top_p,
                    "history": query_config.history
                }
            )
        )
