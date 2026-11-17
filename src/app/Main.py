import uvicorn
from app.common.APIAdapter import FastAPIAdapter, register
from app.container import Container
from app.Modules.MigrationRunner.domain.IMigrationRunner import IMigrationRunner


class Main:
    def __init__(self, host: str = "0.0.0.0", port: int = 8000):
        self.container = Container()
        runner: IMigrationRunner = self.container.get_model("Migration")
        migrations = runner.scan_migrations()
        print(migrations)

        # uvicorn.run(self.container.get_adapter('Api').app, host=host, port=port)
