
from dependency_injector import providers, containers
from db import SQLiteDatabase
from repositories import GameRepository
from services import GameService
from controllers import GameController
from contextlib import contextmanager


class DatabasesContainer(containers.DeclarativeContainer):
    sqlite = providers.Singleton(
        SQLiteDatabase, uri='sqlite:///games.db')


class RepositoriesContainer(containers.DeclarativeContainer):
    databases: DatabasesContainer = providers.DependenciesContainer()
    game_repository = providers.Singleton(
        GameRepository, db_factory=databases.sqlite.provided.session)


class ServicesContainer(containers.DeclarativeContainer):
    repositories: RepositoriesContainer = providers.DependenciesContainer()
    game_service = providers.Factory(
        GameService, game_repository=repositories.game_repository)


class ControllersContainer(containers.DeclarativeContainer):
    services: ServicesContainer = providers.DependenciesContainer()
    game_controller = providers.Factory(
        GameController, game_service=services.game_service)


class MainContainer(containers.DeclarativeContainer):
    databases = providers.Container(DatabasesContainer)
    repositories = providers.Container(
        RepositoriesContainer, databases=databases)
    services = providers.Container(
        ServicesContainer, repositories=repositories)
    controllers = providers.Container(
        ControllersContainer, services=services)


class AppContainer:
    container: MainContainer | None = None

    @classmethod
    @contextmanager
    def scope(cls):
        try:
            cls.container.services.init_resources()
            yield cls.container
        finally:
            cls.container.services.shutdown_resources()

    @classmethod
    def init(cls):
        if cls.container is None:
            cls.container = MainContainer()

    @classmethod
    def engine(cls):
        with cls.container.databases.sqlite().session() as db:
            return db.get_engine()
