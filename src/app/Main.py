import uvicorn
from app.common.APIAdapter import FastAPIAdapter, register
from app.container import Container


class Main:
    def __init__(self, host: str = "0.0.0.0", port: int = 8000):
        self.container = Container()
        uvicorn.run(self.container.get_adapter('Api').app, host=host, port=port)

