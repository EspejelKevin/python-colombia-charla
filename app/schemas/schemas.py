from pydantic import BaseModel
from typing import Optional


class GameInput(BaseModel):
    title: str
    description: str
    platform: str
    genre: str
    price: float


class GameSchema(GameInput):
    id: int


class UpdateGame(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    platform: Optional[str] = None
    genre: Optional[str] = None
    price: Optional[float] = None
