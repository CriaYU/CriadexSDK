from typing import Optional

from CriadexSDK.core.api.route import Route, BaseResponse, outputs
from CriadexSDK.routers.models.create import AzureCompleteModelConfig


class ModelAboutRoute(Route):
    class Response(BaseResponse):
        model: Optional[AzureCompleteModelConfig]

    @outputs(Response)
    async def execute(self, model_id: int) -> Optional[dict]:
        return await self._get(
            path=f"/azure/models/{model_id}/about"
        )
