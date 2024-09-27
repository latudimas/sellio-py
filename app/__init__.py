from fasthtml import common as fh
import fastlite

db = fh.database("data/dev/data.db")
todos = db.t.todos
Todo = todos.dataclass()


def connect_db(db_name: str):
    return fh.database(db_name)


def create_app():
    app, rt = fh.fast_app()
