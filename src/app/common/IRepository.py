from abc import ABC, abstractmethod
from typing import TypeVar

T = TypeVar("T")


class IRepository[T](ABC):
    @abstractmethod
    def save(self, obj: T): ...

    @abstractmethod
    def get(self, id: str) -> T: ...

    @abstractmethod
    def delete(self, obj: T): ...

    @abstractmethod
    def update(self, obj: T): ...
