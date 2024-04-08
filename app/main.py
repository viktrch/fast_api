import json

import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse

from fast_api.app.models.models import User, UserAdult, Feedback, UserCreate

app = FastAPI()
fr = FileResponse('index.html')


# Пример пользовательских данных (для демонстрационных целей)



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


@app.get('/users/')
async def read_users(limit: int = 10):
    return dict(list(fake_users.items())[:limit])
    # return dict(list(fake_users.items())[:limit])


@app.post('/users')
async def create_user(user: UserAdult):
    if not user.validate_age():
        return {'message': 'пользователь несовершеннолетний'}
    return {**user.dict(), 'is_adult': True}


@app.get("/users/{user_id}")
async def read_user(user_id: int):
    if user_id in fake_users:
        return fake_users[user_id]
    return {"error": "User not found"}


@app.post('/feedback')
async def create_feedback(feedback: Feedback):
    return feedback.get_success_message()

if __name__ == "__main__":
    uvicorn.run("main:app", host='127.0.0.1', port=8081, reload=True, workers=3)


@app.post('/create_user')
async def create_user(user: UserCreate):
    return user


from data import sample_products, fake_users


@app.get('/product/{product_id}')
async def get_product(product_id: int):
    return [el for el in sample_products if el['product_id'] == product_id][0]


@app.get('/products/search')
async def get_products(keyword: str, category: str = None, limit: int = 10):
    res = []
    for prod in sample_products:
        if keyword in prod['name'] and (prod['category'] == category or category is None):
            res.append(prod)
    return res[:limit]
