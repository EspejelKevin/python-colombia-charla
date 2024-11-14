from controllers import GameController
from pytest_mock import MockerFixture
from fastapi.responses import JSONResponse
from services import GameService
from models import Game
import json


class TestGameController:
    def set_config(self, mocker: MockerFixture) -> None:
        self.game = mocker.Mock(Game)
        self.game.title = 'SpiderMan'
        self.game.model_dump.return_value = {
            'id': 5,
            'title': 'SpiderMan',
            'description': 'SpiderMan Heroe',
            'platform': 'Xbox',
            'genre': 'Action',
            'price': 50
        }
        self.games = [self.game for _ in range(3)]

        self.game_service = mocker.Mock(GameService)

    def test_get_games_controller(self, mocker: MockerFixture) -> None:
        self.set_config(mocker)

        self.game_service.get_games.return_value = self.games

        self.game_controller = GameController(self.game_service)
        response = self.game_controller.get_games()
        body = json.loads(response.body)

        assert isinstance(response, JSONResponse)
        assert response.status_code == 200
        assert isinstance(body, list)
        assert isinstance(body[0], dict)
        assert body[0]['title'] == 'SpiderMan'

    def test_get_game_controller(self, mocker: MockerFixture) -> None:
        self.set_config(mocker)

        self.game_service.get_game.return_value = None

        self.game_controller = GameController(self.game_service)
        response = self.game_controller.get_game(1)
        body = json.loads(response.body)

        assert isinstance(response, JSONResponse)
        assert response.status_code == 404
        assert isinstance(body, dict)
        assert 'message' in body
        assert body['message'] == 'game not found with id 1'

        self.game_service.get_game.return_value = self.game

        self.game_controller = GameController(self.game_service)
        response = self.game_controller.get_game(1)
        body = json.loads(response.body)

        assert isinstance(response, JSONResponse)
        assert response.status_code == 200
        assert isinstance(body, dict)
        assert 'game' in body

    def test_create_game_controller(self, mocker: MockerFixture) -> None:
        self.set_config(mocker)

        self.game_service.get_game_by_title.return_value = self.game

        self.game_controller = GameController(self.game_service)
        response = self.game_controller.create_game(self.game)
        body = json.loads(response.body)

        assert isinstance(response, JSONResponse)
        assert response.status_code == 409
        assert isinstance(body, dict)
        assert 'message' in body

        self.game_service.get_game_by_title.return_value = None
        self.game_service.create_game.return_value = False

        self.game_controller = GameController(self.game_service)
        response = self.game_controller.create_game(self.game)
        body = json.loads(response.body)

        assert isinstance(response, JSONResponse)
        assert response.status_code == 500
        assert isinstance(body, dict)
        assert 'message' in body

        self.game_service.get_game_by_title.return_value = None
        self.game_service.create_game.return_value = True

        self.game_controller = GameController(self.game_service)
        response = self.game_controller.create_game(self.game)
        body = json.loads(response.body)

        assert isinstance(response, JSONResponse)
        assert response.status_code == 201
        assert isinstance(body, dict)
        assert 'message' in body
        assert body['message'] == 'game SpiderMan created with success'

    def test_update_game_controller(self, mocker: MockerFixture) -> None:
        self.set_config(mocker)

        self.game_service.get_game.return_value = None

        self.game_controller = GameController(self.game_service)
        response = self.game_controller.update_game(1, self.game)
        body = json.loads(response.body)

        assert isinstance(response, JSONResponse)
        assert response.status_code == 404
        assert isinstance(body, dict)
        assert 'message' in body

        self.game_service.get_game.return_value = self.game
        self.game_service.update_game.return_value = False

        self.game_controller = GameController(self.game_service)
        response = self.game_controller.update_game(1, self.game)
        body = json.loads(response.body)

        assert isinstance(response, JSONResponse)
        assert response.status_code == 500
        assert isinstance(body, dict)
        assert 'message' in body

        self.game_service.get_game.return_value = self.game
        self.game_service.update_game.return_value = True

        self.game_controller = GameController(self.game_service)
        response = self.game_controller.update_game(1, self.game)
        body = json.loads(response.body)

        assert isinstance(response, JSONResponse)
        assert response.status_code == 200
        assert isinstance(body, dict)
        assert 'message' in body

    def test_delete_game_controller(self, mocker: MockerFixture) -> None:
        self.set_config(mocker)

        self.game_service.get_game.return_value = None

        self.game_controller = GameController(self.game_service)
        response = self.game_controller.delete_game(1)
        body = json.loads(response.body)

        assert isinstance(response, JSONResponse)
        assert response.status_code == 404
        assert isinstance(body, dict)
        assert 'message' in body

        self.game_service.get_game.return_value = self.game
        self.game_service.delete_game.return_value = False

        self.game_controller = GameController(self.game_service)
        response = self.game_controller.delete_game(1)
        body = json.loads(response.body)

        assert isinstance(response, JSONResponse)
        assert response.status_code == 500
        assert isinstance(body, dict)
        assert 'message' in body

        self.game_service.get_game.return_value = self.game
        self.game_service.delete_game.return_value = True

        self.game_controller = GameController(self.game_service)
        response = self.game_controller.delete_game(1)
        body = json.loads(response.body)

        assert isinstance(response, JSONResponse)
        assert response.status_code == 200
        assert isinstance(body, dict)
        assert 'message' in body
        assert body['message'] == 'game SpiderMan deleted with success'
