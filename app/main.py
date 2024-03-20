import json

import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse

from fast_api.app.models.models import User, UserAdult

app = FastAPI()
fr = FileResponse('index.html')


@app.get('/')
async def index():
    return fr


@app.get('/new')
async def new():
    return {"message": "new end point"}


@app.post('/calculate')
async def calculate(x, y):
    res = int(x) + int(y)
    return {"result": res}

user_1 = {'name': "John Doe", 'id': 1}


@app.get('/users')
async def get_users():
    return User(**user_1)


@app.post('/users')
async def create_user(user: UserAdult):
    if not user.validate_age():
        return {'message': 'пользователь несовершеннолетний'}
    return {**user.dict(), 'is_adult': True}

if __name__ == "__main__":
    uvicorn.run("main:app", host='127.0.0.1', port=8081, reload=True, workers=3)

