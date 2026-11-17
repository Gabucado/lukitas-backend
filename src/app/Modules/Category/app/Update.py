from app.common.IContainer import IContainer
from app.common.IService import IService
from app.Modules.Category.domain.dto import CategoryDTO
from app.Modules.Category.domain.model import Category


class UpdateCategoryService(IService):
    def __init__(self, container: IContainer):
        self.repo = container.get_repo("Category")
        self.factory = container.get_model("Category")

    def run(self, obj: dict):
        dto = CategoryDTO(obj)
        category: Category = self.factory.build(dto)
        self.repo.update(category)
