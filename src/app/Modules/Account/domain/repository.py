from abc import abstractmethod

from app.common.IRepository import IRepository
from app.Modules.Account.domain.model import Account


class AccountRepository(IRepository[Account]):
    @abstractmethod
    def save(self, obj: Account): ...

    @abstractmethod
    def get(self, id: str) -> Account: ...

    @abstractmethod
    def delete(self, obj: Account): ...

    @abstractmethod
    def update(self, obj: Account): ...
