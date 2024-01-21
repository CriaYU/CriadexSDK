from typing import List, Optional

from pydantic import BaseModel

from CriadexSDK.core.api.route import Route, BaseResponse, outputs
from CriadexSDK.routers.agents.chat import QueryModelParameters, LLMAgentResponse


class Intent(BaseModel):
    name: str
    description: str


class RankedIntent(Intent):
    score: float


class IntentsAgentResponse(LLMAgentResponse):
    ranked_intents: List[RankedIntent]


class IntentsAgentConfig(QueryModelParameters):
    intents: List[Intent]
    prompt: str


class AgentIntentsRoute(Route):
    class Response(BaseResponse):
        agent_response: Optional[IntentsAgentResponse]

    @outputs(Response)
    async def execute(
            self,
            model_id: int,
            agent_config: IntentsAgentConfig
    ) -> Optional[dict]:
        return await self._post(
            path=f"/azure/models/{model_id}/agents/intents",
            json=agent_config
        )
