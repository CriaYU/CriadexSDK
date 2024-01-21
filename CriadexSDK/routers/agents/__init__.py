from httpx import AsyncClient

from CriadexSDK.core.api.router import Router
from CriadexSDK.routers.agents.chat import AgentChatRoute
from CriadexSDK.routers.agents.intents import AgentIntentsRoute
from CriadexSDK.routers.agents.lang import AgentLanguageRoute
from CriadexSDK.routers.agents.rerank import AgentRerankRoute


class AgentRouter(Router):

    def __init__(self, api_base: str, http: AsyncClient):
        super().__init__(api_base, http)

        self.chat: AgentChatRoute = self._create_route(AgentChatRoute)
        self.intents: AgentIntentsRoute = self._create_route(AgentIntentsRoute)
        self.language: AgentLanguageRoute = self._create_route(AgentLanguageRoute)
        self.rerank: AgentRerankRoute = self._create_route(AgentRerankRoute)


__all__ = ["AgentRouter"]
