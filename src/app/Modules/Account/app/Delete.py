from app.common.IContainer import IContainer
from app.common.IService import IService
from app.Modules.Account.domain.dto import AccountDTO


class DeleteAccountService(IService):
    def __init__(self, container: IContainer):
        self.repo = container.get_repo("Account")
        self.factory = container.get_model("Account")

    def run(self, object: dict):
        dto = AccountDTO(object)
        account = self.factory.build(dto)
        self.repo.delete(account)
