from decimal import Decimal


class TransactionDTO:
    def __init__(self, obj: dict) -> None:
        self.id = obj.get("id", "")
        self.name = obj.get("name", "")
        self.paymentMethod = obj.get(
            "payment_method", ""
        )  # Decimal(obj.get('ammount', 0))
        self.amount = Decimal(obj.get("amount", 0))
        self.currency = obj.get("currency", "")
        self.origin = obj.get("origin", "")
        self.destiny = obj.get("destiny", "")
        self.category = obj.get("category", "")
