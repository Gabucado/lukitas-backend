from app.Modules.Category.domain.interfaces import ICategory


class Category(ICategory):
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name
