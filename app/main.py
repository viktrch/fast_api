import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()
fr = FileResponse('C:\\Users\\User\\PycharmProjects\\pythonProject\\fast_api\\venv\\index.html')


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


if __name__ == "__main__":
    uvicorn.run("main:app", host='127.0.0.1', port=8081, reload=True, workers=3)
