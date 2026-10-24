import sqlite3
from abc import ABC, abstractmethod
 
 
class Storage(ABC):
 
    @abstractmethod
    def save(self, data: str) -> None:
        pass
 
    @abstractmethod
    def retrieve(self, id: int) -> str:
        pass


class DatabaseStorage(Storage):
 
    def __init__(self, connection: sqlite3.Connection):
        self._connection = connection
        self._connection.execute(
            "CREATE TABLE IF NOT EXISTS storage ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT, "
            "data TEXT NOT NULL)"
        )
        self._connection.commit()
 
    def save(self, data: str):
        self._connection.execute(
            "INSERT INTO storage (data) VALUES (?)", (data,)
        )
        self._connection.commit()
 
    def retrieve(self, id: int):
        row = self._connection.execute(
            "SELECT data FROM storage WHERE id = ?", (id+1,)
        ).fetchone()
        return row[0] if row else None

