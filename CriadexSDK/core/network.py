import os

import httpx

TIMEOUT = float(os.environ.get("CRIADEX_SDK_TIMEOUT", 30.0))

limits: httpx.Limits = httpx.Limits(
    max_keepalive_connections=None,  # Never limit
    max_connections=None  # Never limit
)

timeout: httpx.Timeout = httpx.Timeout(
    read=TIMEOUT,
    connect=TIMEOUT,
    write=TIMEOUT,
    pool=TIMEOUT
)


def create_httpx_client(error_stacktrace: bool, **kwargs) -> httpx.AsyncClient:
    return httpx.AsyncClient(
        headers={**kwargs.pop("headers", dict()), "x-api-stacktrace": str(error_stacktrace)},
        limits=limits,
        timeout=timeout,
        **kwargs
    )
