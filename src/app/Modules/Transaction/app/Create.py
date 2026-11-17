from app.common.IContainer import IContainer
from app.common.IService import IService
from app.Modules.Transaction.domain.dto import TransactionDTO


class CreateTransactionService(IService):
    def __init__(self, container: IContainer):
        self.repo = container.get_repo("Transaction")
        self.factory = container.get_model("Transaction")

    def run(self, obj: dict):
        dto = TransactionDTO(obj)
        Transaction = self.factory.build(dto)
        self.repo.save(Transaction)
