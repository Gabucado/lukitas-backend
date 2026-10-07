class CategoryDTO:
    def __init__(self, obj: dict) -> None:
        self.id = obj.get("id", "")
        self.name = obj.get("category", "")
