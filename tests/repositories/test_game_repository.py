from repositories import GameRepository
from pytest_mock import MockerFixture
from models import Game
from db import SQLiteDatabase


class TestGameRepository:
    def set_config(self, mocker: MockerFixture, mock_data) -> None:
        self.game = mock_data
        self.games = [self.game for _ in range(3)]
        self.db_factory = mocker.MagicMock(SQLiteDatabase)

    def test_get_games_repository(self, mocker: MockerFixture, mock_data) -> None:
        self.set_config(mocker, mock_data)

        self.db_factory.return_value.__enter__.\
            return_value.get_session.\
            return_value.exec.\
            return_value.all.\
            return_value = self.games

        self.game_repository = GameRepository(self.db_factory)
        games = self.game_repository.get_games()

        for game in games:
            assert isinstance(game, Game)
            assert game.id == 1
            assert game.price == 100

    def test_get_game_repository(self, mocker: MockerFixture, mock_data) -> None:
        self.set_config(mocker, mock_data)

        self.db_factory.return_value.__enter__.\
            return_value.get_session.\
            return_value.exec.\
            return_value.one_or_none.\
            return_value = self.game

        self.game_repository = GameRepository(self.db_factory)
        game = self.game_repository.get_game(1)

        assert isinstance(game, Game)
        assert game.id == 1
        assert game.price == 100

    def test_get_game_by_title_repository(self, mocker: MockerFixture, mock_data) -> None:
        self.set_config(mocker, mock_data)

        self.db_factory.return_value.__enter__.\
            return_value.get_session.\
            return_value.exec.\
            return_value.one_or_none.\
            return_value = self.game

        self.game_repository = GameRepository(self.db_factory)
        game = self.game_repository.get_game_by_title('')

        assert isinstance(game, Game)
        assert game.id == 1
        assert game.price == 100

    def test_create_game_repository(self, mocker: MockerFixture, mock_data) -> None:
        self.set_config(mocker, mock_data)

        self.db_factory.return_value.__enter__.\
            return_value.get_session.\
            return_value.add.\
            return_value.commit.\
            return_value = True

        self.game_repository = GameRepository(self.db_factory)
        self.game.model_dump.return_value = {}
        success = self.game_repository.create_game(self.game)

        assert isinstance(success, bool)
        assert success

    def test_update_game_repository(self, mocker: MockerFixture, mock_data) -> None:
        self.set_config(mocker, mock_data)

        self.db_factory.return_value.__enter__.\
            return_value.get_session.\
            return_value.add.\
            return_value.commit.\
            return_value = True

        self.game_repository = GameRepository(self.db_factory)
        self.game.model_dump.return_value = {}
        success = self.game_repository.update_game(self.game, self.game)

        assert isinstance(success, bool)
        assert success

    def test_delete_game_repository(self, mocker: MockerFixture, mock_data) -> None:
        self.set_config(mocker, mock_data)

        self.db_factory.return_value.__enter__.\
            return_value.get_session.\
            return_value.delete.\
            return_value.commit.\
            return_value = True

        self.game_repository = GameRepository(self.db_factory)
        success = self.game_repository.delete_game(self.game)

        assert isinstance(success, bool)
        assert success
