from typing import List
from schemas import GameInput, UpdateGame
from models import Game
from services import IGameService
from sqlmodel import Session, select


class GameRepository(IGameService):
    def __init__(self, db_factory) -> None:
        self.db_factory = db_factory

    def get_games(self) -> List[Game]:
        with self.db_factory() as db:
            session: Session = db.get_session()
            stmt = select(Game)
            return session.exec(stmt).all()

    def get_game(self, id: int) -> Game | None:
        with self.db_factory() as db:
            session: Session = db.get_session()
            stmt = select(Game).where(Game.id == id)
            return session.exec(stmt).one_or_none()

    def get_game_by_title(self, title: str) -> Game | None:
        with self.db_factory() as db:
            session: Session = db.get_session()
            stmt = select(Game).where(Game.title == title)
            return session.exec(stmt).one_or_none()

    def create_game(self, game: GameInput) -> bool:
        with self.db_factory() as db:
            session: Session = db.get_session()
            session.add(Game(**game.model_dump()))
            session.commit()
            return True

    def update_game(self, game: Game, new_game: UpdateGame) -> bool:
        with self.db_factory() as db:
            session: Session = db.get_session()

            new_game = new_game.model_dump(exclude_none=True)
            game.title = new_game.get('title', game.title)
            game.description = new_game.get('description', game.description)
            game.platform = new_game.get('platform', game.platform)
            game.genre = new_game.get('genre', game.genre)
            game.price = new_game.get('price', game.price)

            session.add(game)
            session.commit()
            return True

    def delete_game(self, game: Game) -> bool:
        with self.db_factory() as db:
            session: Session = db.get_session()
            session.delete(game)
            session.commit()
            return True
