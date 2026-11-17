from app.common.http import delete, get, patch, post
from app.common.IAPIPort import IAPIPort
from app.Modules.Account.app.Create import CreateAccountService
from app.Modules.Account.app.Delete import DeleteAccountService
from app.Modules.Account.app.Get import GetAccountService
from app.Modules.Account.app.Update import UpdateAccountService


class FastAPIAccountAdapter:
    prefix = "account"
    api: IAPIPort

    def __init__(
        self,
        create_account_service: CreateAccountService,
        delete_account_service: DeleteAccountService,
        get_account_service: GetAccountService,
        update_account_service: UpdateAccountService,
    ):
        self.create_account_service = create_account_service
        self.delete_account_service = delete_account_service
        self.get_account_service = get_account_service
        self.update_account_service = update_account_service

    @post()
    def create(self, body: dict):
        self.create_account_service.run(body)

    @get("/{account_id}")
    def read(self, account_id: str):
        self.get_account_service.run(account_id)

    @patch("/{account_id}")
    def update(self, body: dict):
        self.update_account_service.run(body)

    @delete("/{account_id}")
    def delete(self, account_id: str):
        self.delete_account_service.run(account_id)
