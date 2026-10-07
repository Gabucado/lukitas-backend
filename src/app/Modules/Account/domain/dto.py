from decimal import Decimal


class AccountDTO:
    def __init__(self, obj: dict) -> None:
        self.id = obj.get('id', '')
        self.name = obj.get('name', '')
        self.amount = Decimal(obj.get('amount', 0))
