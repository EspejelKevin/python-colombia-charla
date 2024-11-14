from sqlmodel import SQLModel, Field


class Game(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(unique=True)
    description: str
    platform: str
    genre: str
    price: float
