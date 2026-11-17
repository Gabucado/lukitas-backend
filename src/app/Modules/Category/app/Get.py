from app.common.IContainer import IContainer
from app.common.IService import IService


class GetCategoryService(IService):
    def __init__(self, container: IContainer):
        self.repo = container.get_repo("Category")

    def run(self, id: str):
        return self.repo.get(id)
