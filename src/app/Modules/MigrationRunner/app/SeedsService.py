from app.common.IService import IService
from backend.app.src.app.Modules.MigrationRunner.domain.IMigrationRunner import (
    IMigrationRunner,
)
from backend.app.src.app.container import Container


class SeedsService(IService):
    def __init__(self, container: Container):
        self.container = container
        self.runner: IMigrationRunner = self.container.get_model("Seeds")

    def run(self):
        self.runner.scan_seeds()
        self.runner.run_seeds()
