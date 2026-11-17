from app.common.DBService import DBService
from app.common.Logger import Logger
from app.Modules.Debt.domain.model import Debt
from app.Modules.Debt.domain.repository import DebtRepository


class PostgresDebtRepository(DebtRepository):
    def __init__(self, db_service: DBService) -> None:
        self.db = db_service

    def save(self, obj: Debt):
        self.db.execute(
            f"INSERT INTO Debts (amount, name) VALUES ({obj.amount}, {obj.name});"
        )

    def delete(self, obj: Debt):
        self.db.execute(f"DELETE Debts WHERE id={obj.id};")

    def update(self, obj: Debt):
        self.db.fetch_one(
            f"UPDATE Debts SET amount={obj.amount} AND name={obj.name} WHERE id={obj.id};"
        )

    def get(self, id: str) -> Debt:
        obj = self.db.fetch_one(f"SELECT * FROM Debts WHERE id={id};")
        Logger.print(obj)
        return Debt(obj)
