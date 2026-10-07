from abc import ABC, abstractmethod
from decimal import Decimal


class IAccount(ABC):

    @abstractmethod
    def get_amount(self) -> Decimal: ...
    @abstractmethod
    def get_name(self) -> str: ...
    @abstractmethod
    def get_id(self) -> str: ...
