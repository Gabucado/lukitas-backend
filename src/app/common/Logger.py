from app.common.Singleton import SingletonMeta


class Logger(metaclass=SingletonMeta):
    @classmethod
    def print(cls, *args, **kwargs):
        print(*args, **kwargs)
