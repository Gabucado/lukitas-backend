from app.common.IContainer import IContainer
from app.common.IService import IService
from app.Modules.Transaction.domain.dto import TransactionDTO
from app.Modules.Transaction.domain.model import Transaction


class UpdateTransactionService(IService):
    def __init__(self, container: IContainer):
        self.repo = container.get_repo("Transaction")
        self.factory = container.get_model("Transaction")

    def run(self, obj: dict):
        dto = TransactionDTO(obj)
        transaction: Transaction = self.factory.build(dto)
        self.repo.update(transaction)
