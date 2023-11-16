from CriadexSDK.routers.content.upload import IndexContentUploadRoute


class IndexContentUpdateRoute(IndexContentUploadRoute):

    ENDPOINT: str = "update"
    METHOD: str = "_patch"
