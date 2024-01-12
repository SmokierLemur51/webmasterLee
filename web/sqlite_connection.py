from pathlib import Path
from sqlite3 import dbapi2 as sqlite3

from quart import g

def _connect_db(app):
    engine = sqlite3.connect(app.config["DATABASE"])
    engine.row_factory = sqlite3.Row
    return engine


def init_db(app):
    db = _connect_db(app)
    with open(Path(app.root_path) / "scripts/sql/schema.sql", mode="r") as file_:
        db.cursor().executescript(file_.read())
        print(file_)
    db.commit()


def _get_db(app):
    if not hasattr(g, "sqlite_db"):
        g.sqlite_db = _connect_db(app)
    return g.sqlite_db