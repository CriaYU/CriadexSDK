from typing import Optional, Any, List

from pydantic import BaseModel

from CriadexSDK.core.api.route import Route, BaseResponse, outputs


class AzureModelConfig(BaseModel):

    api_resource: str = "your-resource"
    api_version: str = "2023-05-15"
    api_key: str = "your-controllers-key"
    api_deployment: str = "your-deployment-name"
    api_model: str = "text-embedding-ada-002"


class AzureCompleteModelConfig(AzureModelConfig):

    id: int


class ModelCreateRoute(Route):

    class Response(BaseResponse):
        model: Optional[AzureCompleteModelConfig]

    @outputs(Response)
    async def execute(self, model_id: int, model_config: AzureModelConfig) -> Optional[dict]:

        return await self._post(
            path=f"/azure/models/create",
            json=model_config
        )
