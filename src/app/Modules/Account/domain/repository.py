from abc import ABC, abstractmethod

from src.app.Modules.Account.domain.model import Account


class AccountRepository(ABC):
    @abstractmethod
    def save(self, account: Account) -> bool:
        ...

    def get(self, id:str) -> Account:
        ...

    def delete(self, account: Account) -> bool:
        ...

    def update(self, account:Account) -> Account:
        ...
