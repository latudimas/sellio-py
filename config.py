from dataclasses import asdict, dataclass
import os
from typing import Dict, Any


@dataclass
class Config:
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///:memory:")
    debug: bool = os.getenv("DEBUG", "false").lower() in ("true", "1", "t")

    def dict(self) -> Dict[str, Any]:
        return asdict(self)


config = Config()
