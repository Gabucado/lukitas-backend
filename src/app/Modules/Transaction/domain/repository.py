from abc import abstractmethod

from app.common.IRepository import IRepository
from app.Modules.Transaction.domain.model import Transaction


class TransactionRepository(IRepository[Transaction]):
    @abstractmethod
    def save(self, obj: Transaction): ...

    @abstractmethod
    def get(self, id: str) -> Transaction: ...

    @abstractmethod
    def delete(self, id: str): ...

    @abstractmethod
    def update(self, obj: Transaction): ...
