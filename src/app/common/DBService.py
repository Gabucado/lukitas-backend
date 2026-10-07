import os

import psycopg2

from app.common.Singleton import SingletonMeta


class DBService(metaclass=SingletonMeta):
    def __init__(self) -> None:
        # self.__conn = psycopg2.connect(os.environ.get('DB_URL', 'wah'))
        # self.__cursor = self.__conn.cursor()
        ...

    def execute(self, query: str):
        self.__cursor.execute(query)

    def fetch(self, query: str):
        self.__cursor.execute(query)
        return self.__cursor.fetchall()

    def fetch_one(self, query: str):
        self.__cursor.execute(query)
        return self.__cursor.fetchone()

    def fetch_many(self, query: str, quantity: int):
        self.__cursor.execute(query)
        self.__cursor.fetchmany(quantity)
