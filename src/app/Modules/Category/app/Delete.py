from app.common.IContainer import IContainer
from app.common.IService import IService


class DeleteCategoryService(IService):
    def __init__(self, container: IContainer):
        self.repo = container.get_repo("Category")

    def run(self, id: str):
        self.repo.delete(id)
