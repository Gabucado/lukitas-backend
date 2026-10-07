from abc import ABC, abstractmethod


class ITransaction(ABC):
    @abstractmethod
    def get_id(): ...

    @abstractmethod
    def get_name(): ...

    @abstractmethod
    def get_paymentMethod(): ...

    @abstractmethod
    def get_amount(): ...

    @abstractmethod
    def get_currency(): ...

    @abstractmethod
    def get_origin(): ...

    @abstractmethod
    def get_destiny(): ...

    @abstractmethod
    def get_category(): ...
