from app.common.IContainer import IContainer
from app.common.IService import IService


class DeleteAccountService(IService):
    def __init__(self, container: IContainer):
        self.repo = container.get_repo("Account")
        self.factory = container.get_model("Account")

    def run(self, id: str):
        self.repo.delete(id)
