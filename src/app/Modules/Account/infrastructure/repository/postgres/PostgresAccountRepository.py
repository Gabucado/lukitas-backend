from app.common.DBService import DBService
from app.common.Logger import Logger
from app.Modules.Account.domain.model import Account
from app.Modules.Account.domain.repository import AccountRepository


class PostgresAccountRepository(AccountRepository):
    def __init__(self, db_service: DBService) -> None:
        self.db = db_service

    def save(self, obj: Account):
        self.db.execute(
            f"INSERT INTO Accounts (amount, name) VALUES ({obj.amount}, {obj.name});"
        )

    def delete(self, obj: Account):
        self.db.execute(f"DELETE Accounts WHERE id={obj.id};")

    def update(self, obj: Account):
        self.db.fetch_one(
            f"UPDATE Accounts SET amount={obj.amount} AND name={obj.name} WHERE id={obj.id};"
        )

    def get(self, id: str) -> Account:
        obj = self.db.fetch_one(f"SELECT * FROM Accounts WHERE id={id};")
        Logger.print(obj)
        return Account(obj)
