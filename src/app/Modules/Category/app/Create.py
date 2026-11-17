from app.common.IContainer import IContainer
from app.common.IService import IService
from app.Modules.Category.domain.dto import CategoryDTO


class CreateCategoryService(IService):
    def __init__(self, container: IContainer):
        self.repo = container.get_repo("Category")
        self.factory = container.get_model("Category")

    def run(self, obj: dict):
        dto = CategoryDTO(obj)
        category = self.factory.build(dto)
        self.repo.save(category)
