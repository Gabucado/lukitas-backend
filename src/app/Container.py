from app.common.APIAdapter import FastAPIAdapter, register
from app.common.DBService import DBService
from app.common.IContainer import IContainer
from app.common.IFactory import Factory
from app.common.IRepository import IRepository
from app.common.IService import IService
from app.Exceptions.AdapterNotFoundException import AdapterNotFoundException
from app.Exceptions.ModelNotFoundException import ModelNotFoundException
from app.Exceptions.ServiceNotFoundException import ServiceNotFoundException
from app.Modules.Account.app.Create import CreateAccountService
from app.Modules.Account.app.Delete import DeleteAccountService
from app.Modules.Account.app.Get import GetAccountService
from app.Modules.Account.app.Update import UpdateAccountService
from app.Modules.Account.domain.model import Account

from app.Modules.Category.app.Create import CreateCategoryService
from app.Modules.Category.app.Delete import DeleteCategoryService
from app.Modules.Category.app.Get import GetCategoryService
from app.Modules.Category.app.Update import UpdateCategoryService
from app.Modules.Category.domain.model import Category

from app.Modules.Debt.app.Create import CreateDebtService
from app.Modules.Debt.app.Delete import DeleteDebtService
from app.Modules.Debt.app.Get import GetDebtService
from app.Modules.Debt.app.Update import UpdateDebtService
from app.Modules.Debt.domain.model import Debt

from app.Modules.Transaction.app.Create import CreateTransactionService
from app.Modules.Transaction.app.Delete import DeleteTransactionService
from app.Modules.Transaction.app.Get import GetTransactionService
from app.Modules.Transaction.app.Update import UpdateTransactionService
from app.Modules.Transaction.domain.model import Transaction

from app.Modules.Account.infrastructure.repository.postgres.PostgresAccountRepository import (
    PostgresAccountRepository,
)
from app.Modules.Category.infrastructure.repository.postgres.PostgresCategoryRepository import (
    PostgresCategoryRepository,
)
from app.Modules.Debt.infrastructure.repository.postgres.PostgresDebtRepository import (
    PostgresDebtRepository,
)
from app.Modules.Transaction.infrastructure.repository.postgres.PostgresTransactionRepository import (
    PostgresTransactionRepository,
)
from app.Modules.Account.infrastructure.api.FastAPI.FastAPIAccountAdapter import (
    FastAPIAccountAdapter,
)
from app.Modules.MigrationRunner.infrastructure.Runner.PostgresRunner import (
    PostgresMigrationRunner,
)


class Container(IContainer):

    def __init__(self):
        self.models: dict[str, Factory] = {}
        self.repositories: dict[str, IRepository] = {}
        self.services: dict[str, IService] = {}
        self.adapters = {}
        self.__initialize_domain()
        self.__initialize_repositories()
        self.__initialize_services()
        self.__initialize_adapters()

    def __initialize_domain(self):
        # Models
        self.models["Account"] = Factory(Account)
        self.models["Transaction"] = Factory(Transaction)
        self.models["Debt"] = Factory(Debt)
        self.models["Category"] = Factory(Category)
        self.models["Migration"] = PostgresMigrationRunner(DBService())

    def __initialize_repositories(self):
        self.repositories["Account"] = PostgresAccountRepository(DBService())
        self.repositories["Category"] = PostgresCategoryRepository(DBService())
        self.repositories["Debt"] = PostgresDebtRepository(DBService())
        self.repositories["Transaction"] = PostgresTransactionRepository(DBService())

    def __initialize_adapters(self):
        self.adapters["DBService"] = DBService()
        self.adapters["Api"] = FastAPIAdapter()

        register(
            self.adapters["Api"],
            FastAPIAccountAdapter(
                self.get_service("CreateAccount"),
                self.get_service("DeleteAccount"),
                self.get_service("GetAccount"),
                self.get_service("UpdateAccount"),
            ),
        )

    def __initialize_services(self):

        # Modules
        ## Account
        self.services["CreateAccount"] = CreateAccountService(self)
        self.services["DeleteAccount"] = DeleteAccountService(self)
        self.services["GetAccount"] = GetAccountService(self)
        self.services["UpdateAccount"] = UpdateAccountService(self)

        ## Category
        self.services["CreateCategory"] = CreateCategoryService(self)
        self.services["DeleteCategory"] = DeleteCategoryService(self)
        self.services["GetCategory"] = GetCategoryService(self)
        self.services["UpdateCategory"] = UpdateCategoryService(self)

        ## Debt
        self.services["CreateDebt"] = CreateDebtService(self)
        self.services["DeleteDebt"] = DeleteDebtService(self)
        self.services["GetDebt"] = GetDebtService(self)
        self.services["UpdateDebt"] = UpdateDebtService(self)

        ## Transaction
        self.services["CreateTransaction"] = CreateTransactionService(self)
        self.services["DeleteTransaction"] = DeleteTransactionService(self)
        self.services["GetTransaction"] = GetTransactionService(self)
        self.services["UpdateTransaction"] = UpdateTransactionService(self)

    def get_repo(self, key: str) -> IRepository:
        try:
            return self.repositories[key]
        except KeyError:
            raise ModelNotFoundException(key)

    def get_model(self, key: str):
        try:
            return self.models[key]
        except KeyError:
            raise ModelNotFoundException(key)

    def get_service(self, key: str):
        try:
            return self.services[key]
        except KeyError:
            raise ServiceNotFoundException(key)

    def get_adapter(self, key: str):
        try:
            return self.adapters[key]
        except KeyError:
            raise AdapterNotFoundException(key)

    def __repr__(self) -> str:
        model_paragraph = "\n".join(
            f"\t- {key}: {value}" for key, value in sorted(self.models.items())
        )
        services_paragraph = "\n".join(
            f"\t- {key}: {value}" for key, value in sorted(self.services.items())
        )
        adapters_paragraph = "\n".join(
            f"\t- {key}: {value}" for key, value in sorted(self.adapters.items())
        )
        return f"""
- Models
{model_paragraph}

- Services
{services_paragraph}

- Adapters
{adapters_paragraph}
        """
