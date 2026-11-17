from app.common.IContainer import IContainer
from app.common.IService import IService


class GetDebtService(IService):
    def __init__(self, container: IContainer):
        self.repo = container.get_repo("Debt")

    def run(self, id: str):
        return self.repo.get(id)
