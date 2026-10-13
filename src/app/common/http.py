from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class Route:
    method: str
    path: str
    handler: Callable[..., Any]
    options: dict = field(default_factory=dict)


def route(method: str, path: str = "", **options):
    def decorator(fn):
        fn.__route__ = (method, path, options)
        return fn

    return decorator


def collect_routes(controller: object) -> list[Route]:
    prefix = getattr(controller, "prefix", "")
    routes = []
    for name, fn in vars(type(controller)).items():
        meta = getattr(fn, "__route__", None)
        if meta:
            method, path, options = meta
            routes.append(
                Route(
                    method,
                    f"/{prefix.strip('/')}{path}",
                    getattr(controller, name),
                    options,
                )
            )
    return routes


def post(path="", **o):
    return route("POST", path, **o)


def get(path="", **o):
    return route("GET", path, **o)


def patch(path="", **o):
    return route("PATCH", path, **o)


def delete(path="", **o):
    return route("DELETE", path, **o)
