from app.Modules.Debt.domain.interfaces import IDebt


class Debt(IDebt):
    def __init__(self, id, name, currency, date, amount, debtor, creditor):
        self.id = id
        self.name = name
        self.currency = currency
        self.date = date
        self.amount = amount
        self.debtor = debtor
        self.creditor = creditor

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_currency(self):
        return self.currency

    def get_date(self):
        return self.date

    def get_amount(self):
        return self.amount

    def get_debtor(self):
        return self.debtor

    def get_creditor(self):
        return self.creditor
