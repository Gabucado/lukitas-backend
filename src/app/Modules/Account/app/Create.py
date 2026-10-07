from src.app.common.IService import IService
from src.app.Modules.Account.domain.dto import AccountDTO
from src.app.Modules.Account.domain.model import Account
from src.app.Modules.Account.domain.repository import AccountRepository


class CreateAccountService(IService):
    def __init__(self, repo:AccountRepository):
        self.repo = repo

    def run(self, object:dict):
        dto = AccountDTO(object)
        account = Account(dto)
        self.repo.save(account)
