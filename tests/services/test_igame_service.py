from services import IGameService
from pytest_mock import MockerFixture
import pytest


class TestIGameService:
    def set_config(self, mocker: MockerFixture) -> None:
        mocker.patch.multiple(IGameService, __abstractmethods__=set())
        self.igame_service = IGameService()
        self.game = mocker.Mock()

    def test_not_implemented_methods(self, mocker: MockerFixture) -> None:
        self.set_config(mocker)

        with pytest.raises(NotImplementedError):
            self.igame_service.get_games()

        with pytest.raises(NotImplementedError):
            self.igame_service.get_game(1)

        with pytest.raises(NotImplementedError):
            self.igame_service.get_game_by_title('')

        with pytest.raises(NotImplementedError):
            self.igame_service.create_game(self.game)

        with pytest.raises(NotImplementedError):
            self.igame_service.update_game(1, self.game)

        with pytest.raises(NotImplementedError):
            self.igame_service.delete_game(self.game)
