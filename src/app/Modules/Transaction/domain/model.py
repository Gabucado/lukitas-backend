from app.Modules.Transaction.domain.interfaces import ITransaction


class Transaction(ITransaction):
    def __init__(
        self, id, name, paymentMethod, amount, currency, origin, destiny, category
    ):
        self.id = id
        self.name = name
        self.paymentMethod = paymentMethod
        self.amount = amount
        self.currency = currency
        self.origin = origin
        self.destiny = destiny
        self.category = category

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_paymentMethod(self):
        return self.paymentMethod

    def get_amount(self):
        return self.amount

    def get_currency(self):
        return self.currency

    def get_origin(self):
        return self.origin

    def get_destiny(self):
        return self.destiny

    def get_category(self):
        return self.category
