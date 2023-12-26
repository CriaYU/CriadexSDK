from typing import List, Optional, Union

from pydantic import BaseModel

from CriadexSDK.core.api.route import Route, BaseResponse, outputs
from CriadexSDK.routers.agents.chat import AgentExecution


class AgentLanguageExecution(AgentExecution):
    language: Union[str, None]
    supported_languages: List[str]
    usage: None = None


class LanguageAgentConfig(BaseModel):
    prompt: str


class AgentLanguageRoute(Route):
    class Response(BaseResponse):
        agent_response: Optional[AgentLanguageExecution]

    @outputs(Response)
    async def execute(
            self,
            model_id: int,
            agent_config: LanguageAgentConfig
    ) -> Optional[dict]:
        return await self._post(
            path=f"/azure/models/{model_id}/agents/language",
            json=agent_config
        )
