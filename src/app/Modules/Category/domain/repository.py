from abc import abstractmethod

from app.common.IRepository import IRepository
from app.Modules.Category.domain.model import Category


class CategoryRepository(IRepository[Category]):
    @abstractmethod
    def save(self, obj: Category): ...

    @abstractmethod
    def get(self, id: str) -> Category: ...

    @abstractmethod
    def delete(self, obj: Category): ...

    @abstractmethod
    def update(self, obj: Category): ...
