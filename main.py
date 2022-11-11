from fastapi import FastAPI

app = FastAPI()

from fastapi.responses import FileResponse


@app.get("/")
async def root():
    return FileResponse('index.html')


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/data")
async def data():
    return {'hello':1234}

from pydantic import BaseModel
class SendRequest(BaseModel):
    name: str
    phone: int


@app.post("/send")
async def send(data: SendRequest):
    print(data)
    return '전송완료'
