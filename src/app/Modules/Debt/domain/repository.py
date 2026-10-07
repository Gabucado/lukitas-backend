from abc import abstractmethod

from app.common.IRepository import IRepository
from app.Modules.Debt.domain.model import Debt


class DebtRepository(IRepository[Debt]):
    @abstractmethod
    def save(self, obj: Debt): ...

    @abstractmethod
    def get(self, id: str) -> Debt: ...

    @abstractmethod
    def delete(self, obj: Debt): ...

    @abstractmethod
    def update(self, obj: Debt): ...
