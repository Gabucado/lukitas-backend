from decimal import Decimal


class DebtDTO:
    def __init__(self, obj: dict) -> None:
        self.id = obj.get("id", "")
        self.name = obj.get("name", "")
        self.currency = obj.get("currency", "")
        self.date = obj.get("date", "")  # Decimal(obj.get('ammount', 0))
        self.amount = Decimal(obj.get("amount", 0))
        self.debtor = obj.get("debtor", "")
        self.creditor = obj.get("creditor", "")
