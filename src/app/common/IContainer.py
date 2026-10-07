from abc import ABC, abstractmethod

from app.common.IFactory import Factory
from app.common.IRepository import IRepository
from app.common.IService import IService


class IContainer(ABC):
    @abstractmethod
    def get_model(self, key: str) -> Factory: ...

    @abstractmethod
    def get_service(self, key: str) -> IService: ...

    @abstractmethod
    def get_adapter(self, key: str) -> object: ...

    @abstractmethod
    def get_repo(self, key: str) -> IRepository: ...
