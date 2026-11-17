from app.Modules.MigrationRunner.domain.IMigrationRunner import IMigrationRunner


class PostgresMigrationRunner(IMigrationRunner):
    def scan_migrations(self) -> list[str]:
        scan: list[str] = self.scan_modules()

        return scan

    def run_migrations(self):
        pass

    def scan_seeds(self):
        pass

    def run_seeds(self):
        pass
