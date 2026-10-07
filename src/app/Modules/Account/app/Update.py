from app.common.IContainer import IContainer
from app.common.IService import IService
from app.Modules.Account.domain.dto import AccountDTO
from app.Modules.Account.domain.model import Account


class UpdateAccountService(IService):
    def __init__(self, container: IContainer):
        self.repo = container.get_repo("Account")
        self.factory = container.get_model("Account")

    def run(self, object: dict):
        dto = AccountDTO(object)
        account: Account = self.factory.build(dto)
        self.repo.update(account)
