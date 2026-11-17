from abc import ABC
import os
from app.common.DBService import DBService


class IMigrationRunner(ABC):
    def __init__(self, driver: DBService):
        self.driver = driver
        self.tasks: dict = {}

    def scan_modules(self):
        dbAdapter, base, modules = self.get_module_names()
        migrations = {}
        for module in modules:
            if module == "MigrationRunner":
                continue

            if module in migrations:
                raise Exception("module name duplicated")
            suffix = "infrastructure", "repository", dbAdapter, "migrations"
            files = os.listdir(os.path.join(*(base + (module,) + suffix)))
            migrations[module] = (
                os.path.join(*(base + (module,) + suffix)),
                os.listdir(os.path.join(*(base + (module,) + suffix))),
            )
        return migrations

    def get_module_names(self):
        dbAdapter = "postgres"
        base = "src", "app", "Modules"
        modules = os.listdir(os.path.join(*base))
        return dbAdapter, base, modules

    def scan_migrations(self): ...
    def run_migrations(self): ...
    def scan_seeds(self): ...
    def run_seeds(self): ...
