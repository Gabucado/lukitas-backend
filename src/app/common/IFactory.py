from collections.abc import Callable


class Factory[**P, T]:
    def __init__(self, product: Callable[P, T]) -> None:
        self._product = product

    def build(self, *args: P.args, **kwargs: P.kwargs) -> T:
        return self._product(*args, **kwargs)
