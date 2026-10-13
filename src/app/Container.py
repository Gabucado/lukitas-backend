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
from app.Modules.Account.infrastructure.repository.postgres.PostgresAccountRepository import (
    PostgresAccountRepository,
)
from app.Modules.Category.domain.model import Category
from app.Modules.Debt.domain.model import Debt
from app.Modules.Transaction.domain.model import Transaction


class Container(IContainer):

    def __init__(self):
        self.models: dict[str, Factory] = {}
        self.repositories: dict[str, IRepository] = {}
        self.services: dict[str, IService] = {}
        self.adapters = {}
        self.__initialize_domain()
        self.__initialize_adapters()
        self.__initialize_services()

    def __initialize_domain(self):
        # Models
        self.models["Account"] = Factory(Account)
        self.models["Transaction"] = Factory(Transaction)
        self.models["Debt"] = Factory(Debt)
        self.models["Category"] = Factory(Category)

    def __initialize_adapters(self):
        self.adapters["DBService"] = DBService()
        # TODO: Encapsular FastApi
        api = self.adapters["Api"] = FastAPIAdapter()
        register(
            api,
        )
        self.repositories["Account"] = PostgresAccountRepository(DBService())

    def __initialize_services(self):
        self.services["CreateAccount"] = CreateAccountService(self)
        self.services["DeleteAccount"] = DeleteAccountService(self)
        self.services["GetAccount"] = GetAccountService(self)
        self.services["UpdateAccount"] = UpdateAccountService(self)

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
            f"\t- {key}: {value}" for key, value in self.models.items()
        )
        services_paragraph = "\n".join(
            f"\t- {key}: {value}" for key, value in self.services.items()
        )
        adapters_paragraph = "\n".join(
            f"\t- {key}: {value}" for key, value in self.adapters.items()
        )
        return f"""
- Models
{model_paragraph}

- Services
{services_paragraph}

- Adapters
{adapters_paragraph}
        """
