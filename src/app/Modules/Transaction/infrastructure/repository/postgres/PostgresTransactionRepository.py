from app.common.DBService import DBService
from app.common.Logger import Logger
from app.Modules.Transaction.domain.model import Transaction
from app.Modules.Transaction.domain.repository import TransactionRepository


class PostgresTransactionRepository(TransactionRepository):
    def __init__(self, db_service: DBService) -> None:
        self.db = db_service

    def save(self, obj: Transaction):
        self.db.execute(
            f"INSERT INTO Transactions (amount, name) VALUES ({obj.amount}, {obj.name});"
        )

    def delete(self, obj: Transaction):
        self.db.execute(f"DELETE Transactions WHERE id={obj.id};")

    def update(self, obj: Transaction):
        self.db.fetch_one(
            f"UPDATE Transactions SET amount={obj.amount} AND name={obj.name} WHERE id={obj.id};"
        )

    def get(self, id: str) -> Transaction:
        obj = self.db.fetch_one(f"SELECT * FROM Transactions WHERE id={id};")
        Logger.print(obj)
        return Transaction(obj)
