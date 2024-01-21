from typing import Optional, List

from CriadexSDK.core.api.route import Route, BaseResponse, outputs
from CriadexSDK.routers.agents.chat import LLMAgentResponse, QueryModelParameters
from CriadexSDK.routers.content.search import TextNode, NodeWithScore


class RerankAgentResponse(LLMAgentResponse):
    ranked_nodes: List[NodeWithScore] = []


class RerankAgentConfig(QueryModelParameters):
    prompt: str
    nodes: List[TextNode]


class AgentRerankRoute(Route):
    class Response(BaseResponse):
        agent_response: Optional[RerankAgentResponse]

    @outputs(Response)
    async def execute(
            self,
            model_id: int,
            agent_config: RerankAgentConfig
    ) -> Optional[dict]:
        return await self._post(
            path=f"/azure/models/{model_id}/agents/rerank",
            json=agent_config
        )
