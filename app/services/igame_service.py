from abc import ABCMeta, abstractmethod
from typing import List
from models import Game
from schemas import GameInput, UpdateGame


class IGameService(metaclass=ABCMeta):
    @abstractmethod
    def get_games(self) -> List[Game]:
        raise NotImplementedError

    @abstractmethod
    def get_game(self, id: int) -> Game | None:
        raise NotImplementedError

    @abstractmethod
    def get_game_by_title(self, title: str) -> Game | None:
        raise NotImplementedError

    @abstractmethod
    def create_game(self, game: GameInput) -> bool:
        raise NotImplementedError

    @abstractmethod
    def update_game(self, game: Game, new_game: UpdateGame) -> bool:
        raise NotImplementedError

    @abstractmethod
    def delete_game(self, game: Game) -> bool:
        raise NotImplementedError
