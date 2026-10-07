from decimal import Decimal

from app.Modules.Account.domain.interfaces import IAccount


class Account(IAccount):
    def __init__(self, id: str, amount: Decimal, name: str):
        self.id = id
        self.amount = amount
        self.name = name

    def get_amount(self):
        return self.amount

    def get_id(self) -> str:
        return self.id

    def get_name(self) -> str:
        return self.name
