import os
import sys

import pytest
from pytest_mock import MockerFixture

sys.path.append(f'{os.path.dirname(__file__)}/../app')


@pytest.fixture
def mock_data(mocker: MockerFixture):
    from models import Game

    mock_game = mocker.Mock(Game)
    mock_game.id = 1
    mock_game.title = 'Super Mario Party'
    mock_game.description = 'Mario and Luigi have many adventures'
    mock_game.genre = 'Adventure'
    mock_game.platform = 'Nintendo'
    mock_game.price = 100

    return mock_game
