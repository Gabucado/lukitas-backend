from abc import ABC, abstractmethod

from app.common.http import Route


class IAPIPort(ABC):
    @abstractmethod
    def add_route(self, route: Route) -> None: ...
