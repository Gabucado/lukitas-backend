from app.common.DBService import DBService
from app.common.Logger import Logger
from app.Modules.Category.domain.model import Category
from app.Modules.Category.domain.repository import CategoryRepository


class PostgresCategoryRepository(CategoryRepository):
    def __init__(self, db_service: DBService) -> None:
        self.db = db_service

    def save(self, obj: Category):
        self.db.execute(
            f"INSERT INTO Categorys (amount, name) VALUES ({obj.id}, {obj.name});"
        )

    def delete(self, obj: Category):
        self.db.execute(f"DELETE Categorys WHERE id={obj.id};")

    def update(self, obj: Category):
        self.db.fetch_one(
            f"UPDATE Categorys SET amount={obj.amount} AND name={obj.name} WHERE id={obj.id};"
        )

    def get(self, id: str) -> Category:
        obj = self.db.fetch_one(f"SELECT * FROM Categorys WHERE id={id};")
        Logger.print(obj)
        return Category(obj)
