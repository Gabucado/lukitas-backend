from abc import ABC, abstractmethod


class IDebt(ABC):
    @abstractmethod
    def get_id(self): ...

    @abstractmethod
    def get_name(self): ...

    @abstractmethod
    def get_currency(self): ...

    @abstractmethod
    def get_date(self): ...

    @abstractmethod
    def get_amount(self): ...

    @abstractmethod
    def get_debtor(self): ...

    @abstractmethod
    def get_creditor(self): ...
