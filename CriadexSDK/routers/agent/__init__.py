from httpx import AsyncClient

from CriadexSDK.core.api.router import Router
from CriadexSDK.routers.agent.chat import AgentChatRoute
from CriadexSDK.routers.agent.intents import AgentIntentsRoute
from CriadexSDK.routers.agent.lang import AgentLanguageRoute


class AgentRouter(Router):

    def __init__(self, api_base: str, http: AsyncClient):
        super().__init__(api_base, http)

        self.chat: AgentChatRoute = self._create_route(AgentChatRoute)
        self.intents: AgentIntentsRoute = self._create_route(AgentIntentsRoute)
        self.language: AgentLanguageRoute = self._create_route(AgentLanguageRoute)


__all__ = ["AgentRouter"]
