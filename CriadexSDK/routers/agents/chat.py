from typing import List, Optional, Literal, Any

from pydantic import BaseModel

from CriadexSDK.core.api.route import Route, BaseResponse, outputs
from CriadexSDK.routers.content.search import TokenUsage


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


class ChatModelConfig(QueryModelParameters):
    history: List[ChatMessage]


class AgentExecution(BaseModel):
    usage: List[TokenUsage]


class ChatResponse(BaseModel):
    message: ChatMessage
    raw: RawChatMessage


class AgentChatExecution(AgentExecution):
    chat_response: ChatResponse


class AgentChatRoute(Route):
    class Response(BaseResponse):
        agent_response: Optional[AgentChatExecution]

    @outputs(Response)
    async def execute(
            self,
            model_id: int,
            agent_config: ChatModelConfig
    ) -> Optional[dict]:
        return await self._post(
            path=f"/azure/models/{model_id}/agents/chat",
            json=agent_config
        )
