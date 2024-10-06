from typing import Annotated
from functools import lru_cache

from fastapi import FastAPI, Depends

from .config import Settings
from .database import get_db, init_db
import models


@lru_cache
def get_settings():
    return Settings()


def create_application() -> FastAPI:
    settings = get_settings()
    app = FastAPI()

    # DB initialization
    engine, session_factory = init_db(settings.db_url)
    db_dependency = lambda: get_db(session_factory)

    models.Base.metadata.create_all(bind=engine)
    api_router = create_routes
    return app


app = create_application()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
