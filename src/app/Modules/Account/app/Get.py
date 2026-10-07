from src.app.common.IService import IService
from src.app.Modules.Account.domain.repository import AccountRepository


class UpdateAccountService(IService):
    def __init__(self, repo:AccountRepository):
        self.repo = repo

    def run(self, id:str):
        return self.repo.get(id)
