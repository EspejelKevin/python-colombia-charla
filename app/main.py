import uvicorn
from fastapi import FastAPI
from container import AppContainer
from sqlmodel import SQLModel
from models import Game
from routes import router


def on_startup():
    AppContainer.init()
    SQLModel.metadata.create_all(AppContainer.engine())


tags = [
    {
        'name': 'Health Check',
        'description': 'Verify is the server is up'
    },
    {
        'name': 'Games',
        'description': 'CRUD Games'
    }
]


app = FastAPI(
    title='Games',
    summary='CRUD Games',
    description='Service to handler operations CRUD about Games',
    openapi_tags=tags,
    on_startup=[on_startup]
)

app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
