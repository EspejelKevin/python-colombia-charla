from fastapi.routing import APIRouter
from fastapi.responses import JSONResponse
from controllers import GameController
from schemas import GameInput, UpdateGame
import container


router = APIRouter(prefix='/api/v1')


@router.get('/liveness', tags=['Health Check'])
def liveness() -> dict:
    return {'status': 'service is up'}


@router.get('/games', tags=['Games'])
def get_games() -> JSONResponse:
    with container.AppContainer.scope() as app:
        controller: GameController = app.controllers.game_controller()
        return controller.get_games()


@router.get('/games/{id}', tags=['Games'])
def get_game(id: int) -> JSONResponse:
    with container.AppContainer.scope() as app:
        controller: GameController = app.controllers.game_controller()
        return controller.get_game(id)


@router.post('/games', tags=['Games'])
def create_game(game: GameInput) -> JSONResponse:
    with container.AppContainer.scope() as app:
        controller: GameController = app.controllers.game_controller()
        return controller.create_game(game)


@router.put('/games/{id}', tags=['Games'])
def update_game(id: int, new_game: UpdateGame) -> JSONResponse:
    with container.AppContainer.scope() as app:
        controller: GameController = app.controllers.game_controller()
        return controller.update_game(id, new_game)


@router.delete('/games/{id}', tags=['Games'])
def delete_game(id: int) -> JSONResponse:
    with container.AppContainer.scope() as app:
        controller: GameController = app.controllers.game_controller()
        return controller.delete_game(id)
