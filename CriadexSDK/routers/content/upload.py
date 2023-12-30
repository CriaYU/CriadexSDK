import json
from typing import Optional, Type, Literal, Callable

from pydantic import BaseModel

from CriadexSDK.core.api.route import Route, BaseResponse, outputs

AcceptedContentMimeTypes: Type = Literal[
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "application/json"
]


class UploadFile(BaseModel):
    file_name: str
    file_bytes: bytes
    file_mimetype: AcceptedContentMimeTypes


class GroupContentUploadRoute(Route):
    ENDPOINT: str = "upload"
    METHOD: str = "_post"

    class Response(BaseResponse):
        token_usage: Optional[int]

    @outputs(Response)
    async def execute(
            self,
            group_name: str,
            upload_file: UploadFile,
            file_metadata: Optional[dict] = None
    ) -> Optional[dict]:
        http_method: Callable = getattr(self, getattr(self, 'METHOD'))  # Do it this way for inheritance
        endpoint: str = getattr(self, 'ENDPOINT')

        return await http_method(
            path=f"/criadex/{group_name}/content/{endpoint}",
            files={'file': (upload_file.file_name, upload_file.file_bytes, upload_file.file_mimetype)},
            data={'file_metadata': json.dumps(file_metadata) if file_metadata else None}
        )
