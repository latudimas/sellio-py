from dataclasses import dataclass
import fastlite
import sqlite3
from typing import List, Tuple, Optional, Any


class Database:
    def __init__(self, db_name: str) -> None:
        self.db_name: str = db_name
        self.conn: Optional[sqlite3.Connection] = None
        self.cursor: Optional[sqlite3.Cursor] = None

    def connect(self) -> None:
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def close(self) -> None:
        if self.conn:
            self.conn.close()
            self.conn = None
            self.cursor = None


@dataclass
class Db:
    path: str
    db_name: str

    def connect(self) -> None:
        fastlite.database(self.path + self.db_name)
        fastlite.database
