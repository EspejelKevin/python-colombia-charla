from services import GameService
from pytest_mock import MockerFixture
from models import Game


class TestGameService:
    def set_config(self, mocker: MockerFixture, mock_data) -> None:
        self.game = mock_data
        self.games = [self.game for _ in range(3)]

        self.game_repository = mocker.Mock()
        self.game_repository.get_games.return_value = self.games
        self.game_repository.get_game.return_value = self.game
        self.game_repository.get_game_by_title.return_value = self.game
        self.game_repository.create_game.return_value = True
        self.game_repository.update_game.return_value = True
        self.game_repository.delete_game.return_value = True

        self.game_service = GameService(self.game_repository)

    def test_get_games_service(self, mocker: MockerFixture, mock_data) -> None:
        self.set_config(mocker, mock_data)

        games = self.game_service.get_games()

        for game in games:
            assert isinstance(game, Game)
            assert game.id == 1
            assert game.title == 'Super Mario Party'
            assert game.price == 100

    def test_get_game_service(self, mocker: MockerFixture, mock_data) -> None:
        self.set_config(mocker, mock_data)

        game = self.game_service.get_game(1)

        assert isinstance(game, Game)
        assert game.id == 1
        assert game.title == 'Super Mario Party'
        assert game.price == 100

    def test_get_game_by_title_service(self, mocker: MockerFixture, mock_data) -> None:
        self.set_config(mocker, mock_data)

        game = self.game_service.get_game_by_title('')

        assert isinstance(game, Game)
        assert game.id == 1
        assert game.title == 'Super Mario Party'
        assert game.price == 100

    def test_create_game_service(self, mocker: MockerFixture, mock_data) -> None:
        self.set_config(mocker, mock_data)

        success = self.game_service.create_game(self.game)

        assert success

    def test_update_game_service(self, mocker: MockerFixture, mock_data) -> None:
        self.set_config(mocker, mock_data)

        success = self.game_service.update_game(1, self.game)

        assert success

    def test_delete_game_service(self, mocker: MockerFixture, mock_data) -> None:
        self.set_config(mocker, mock_data)

        success = self.game_service.delete_game(self.game)

        assert success
