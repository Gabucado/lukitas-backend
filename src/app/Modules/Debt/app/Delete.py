from app.common.IContainer import IContainer
from app.common.IService import IService


class DeleteDebtService(IService):
    def __init__(self, container: IContainer):
        self.repo = container.get_repo("Debt")

    def run(self, id: str):
        self.repo.delete(id)
