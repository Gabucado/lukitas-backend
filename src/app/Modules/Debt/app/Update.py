from app.common.IContainer import IContainer
from app.common.IService import IService
from app.Modules.Debt.domain.dto import DebtDTO
from app.Modules.Debt.domain.model import Debt


class UpdateDebtService(IService):
    def __init__(self, container: IContainer):
        self.repo = container.get_repo("Debt")
        self.factory = container.get_model("Debt")

    def run(self, obj: dict):
        dto = DebtDTO(obj)
        debt: Debt = self.factory.build(dto)
        self.repo.update(debt)
