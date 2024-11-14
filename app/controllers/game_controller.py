from services import IGameService
from schemas import GameSchema, GameInput, UpdateGame
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import status


class GameController:
    def __init__(self, game_service: IGameService) -> None:
        self.game_service = game_service

    def get_games(self) -> JSONResponse:
        games = self.game_service.get_games()
        games_mapped = [GameSchema(**game.model_dump()) for game in games]
        return JSONResponse(jsonable_encoder(games_mapped), status.HTTP_200_OK)

    def get_game(self, id: int) -> JSONResponse:
        game = self.game_service.get_game(id)
        if not game:
            return JSONResponse({'message': f'game not found with id {id}'},
                                status.HTTP_404_NOT_FOUND)

        game_mapped = GameSchema(**game.model_dump())
        return JSONResponse(jsonable_encoder({'game': game_mapped}), status.HTTP_200_OK)

    def create_game(self, game: GameInput) -> JSONResponse:
        game_db = self.game_service.get_game_by_title(game.title)
        if game_db:
            return JSONResponse({'message': f'game {game.title} already exists'},
                                status.HTTP_409_CONFLICT)

        success = self.game_service.create_game(game)
        if not success:
            return JSONResponse({'message': f'error while inserting game {game.title}'},
                                status.HTTP_500_INTERNAL_SERVER_ERROR)

        return JSONResponse({'message': f'game {game.title} created with success'},
                            status.HTTP_201_CREATED)

    def update_game(self, id: int, new_game: UpdateGame) -> JSONResponse:
        game = self.game_service.get_game(id)
        if not game:
            return JSONResponse({'message': f'game not found with id {id}'},
                                status.HTTP_404_NOT_FOUND)

        success = self.game_service.update_game(game, new_game)
        if not success:
            return JSONResponse({'message': f'error while updating game with id {id}'},
                                status.HTTP_500_INTERNAL_SERVER_ERROR)

        return JSONResponse({'message': f'game {game.title} updated with success'},
                            status.HTTP_200_OK)

    def delete_game(self, id: int) -> JSONResponse:
        game = self.game_service.get_game(id)
        if not game:
            return JSONResponse({'message': f'game not found with id {id}'},
                                status.HTTP_404_NOT_FOUND)

        success = self.game_service.delete_game(game)
        if not success:
            return JSONResponse({'message': f'error while deleting game with id {id}'},
                                status.HTTP_500_INTERNAL_SERVER_ERROR)

        return JSONResponse({'message': f'game {game.title} deleted with success'},
                            status.HTTP_200_OK)
