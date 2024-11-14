from typing import List
from schemas import GameInput, UpdateGame
from models import Game
from .igame_service import IGameService


class GameService(IGameService):
    def __init__(self, game_repository: IGameService) -> None:
        self.game_repository = game_repository

    def get_games(self) -> List[Game]:
        return self.game_repository.get_games()

    def get_game(self, id: int) -> Game | None:
        return self.game_repository.get_game(id)

    def get_game_by_title(self, title: str) -> Game | None:
        return self.game_repository.get_game_by_title(title)

    def create_game(self, game: GameInput) -> bool:
        return self.game_repository.create_game(game)

    def update_game(self, game: Game, new_game: UpdateGame) -> bool:
        return self.game_repository.update_game(game, new_game)

    def delete_game(self, game: Game) -> bool:
        return self.game_repository.delete_game(game)
