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


class IndexContentUploadRoute(Route):

    ENDPOINT: str = "upload"
    METHOD: str = "_post"

    class Response(BaseResponse):
        pass

    @outputs(Response)
    async def execute(
        self,
        index_name: str,
        upload_file: UploadFile
    ) -> Optional[dict]:

        http_method: Callable = getattr(self, getattr(self, 'METHOD'))
        endpoint: str = getattr(self, 'ENDPOINT')

        return await http_method(
            path=f"/criadex/{index_name}/content/{endpoint}",
            files={'file': (upload_file.file_name, upload_file.file_bytes, upload_file.file_mimetype)}
        )
