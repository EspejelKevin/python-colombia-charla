from pydantic import BaseModel


class GameInput(BaseModel):
    title: str
    description: str
    platform: str
    genre: str
    price: float


class GameSchema(GameInput):
    id: int


class UpdateGame(BaseModel):
    title: str | None
    description: str | None 
    platform: str | None
    genre: str | None
    price: float | None
