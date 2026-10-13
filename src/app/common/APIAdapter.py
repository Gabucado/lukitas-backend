from fastapi import FastAPI

from app.common.http import Route, collect_routes
from app.common.IAPIPort import IAPIPort


class FastAPIAdapter(IAPIPort):
    def __init__(self) -> None:
        self.app = FastAPI()

    def add_route(self, route: Route) -> None:
        self.app.add_api_route(
            route.path, route.handler, methods=[route.method], **route.options
        )


def register(api: IAPIPort, controller: object) -> None:
    for r in collect_routes(controller):
        api.add_route(r)
