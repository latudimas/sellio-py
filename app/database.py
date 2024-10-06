from typing import Tuple
from sqlalchemy import Engine, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


def init_db(database_url: str) -> Tuple[Engine, sessionmaker]:
    engine = create_engine(database_url, connect_args={"check_same_thread": False})
    session_factory = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return engine, session_factory


def get_db(session_factory: sessionmaker):
    db = session_factory()
    try:
        yield db
    finally:
        db.close()
