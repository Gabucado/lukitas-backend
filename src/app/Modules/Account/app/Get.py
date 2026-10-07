from app.common.IContainer import IContainer
from app.common.IService import IService


class GetAccountService(IService):
    def __init__(self, container: IContainer):
        self.repo = container.get_model("Account")

    def run(self, id: str):
        return self.repo.get(id)
