from contextlib import contextmanager, suppress
from sqlmodel import create_engine, Session


class Database:
    def __init__(self, uri: str, **kwargs: dict) -> None:
        self.engine = create_engine(url=uri, connect_args=kwargs)
        self.session = Session(self.engine)

    def __enter__(self):
        return self

    def get_engine(self):
        return self.engine

    def get_session(self):
        return self.session

    def __exit__(self):
        self.session.close()


class SQLiteDatabase:
    def __init__(self, uri: str, **kwargs: dict) -> None:
        self.database = Database(uri, **kwargs)

    @contextmanager
    def session(self):
        with suppress(Exception):
            yield self.database
