from app.common.IContainer import IContainer
from app.common.IService import IService


class GetTransactionService(IService):
    def __init__(self, container: IContainer):
        self.repo = container.get_repo("Transaction")

    def run(self, id: str):
        return self.repo.get(id)
