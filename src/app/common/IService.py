from abc import ABC, abstractmethod


class IService(ABC):
    @abstractmethod
    def run(self, *args, **kwargs) -> object:
        ...
