from typing import Optional, Any, List

from pydantic import BaseModel

from CriadexSDK.core.api.route import Route, BaseResponse, outputs
from CriadexSDK.routers.models.create import AzureCompleteModelConfig, AzureModelPartialConfig, ModelCreateRoute


class ModelUpdateRoute(Route):

    @outputs(ModelCreateRoute.Response)
    async def execute(self, model_id: int, model_config: AzureModelPartialConfig) -> Optional[dict]:

        return await self._patch(
            path=f"/azure/models/{model_id}/update",
            json=model_config
        )
