from dataclasses import asdict
import uvicorn
from fastapi import FastAPI
from app.database.conn import db

from app.common.config import conf


def create_app():
    """
    앱 함수 실행
    :return:
    """
    c = conf
    app = FastAPI()
    conf_dict = asdict(c)
    db.init

    # 데이터 베이스 이니셜라이즈

    # 레디스 이니셜라이즈

    # 미들웨어 정의

    # 라우터 정의

    return app


app = create_app()

if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
    # uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=conf().PROJ_RELOAD)





# from fastapi.responses import FileResponse
# @app.get("/")
# async def root():
#     return FileResponse('../index.html')
#
#
# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}
#
# @app.get("/data")
# async def data():
#     return {'hello':1234}
#
# from pydantic import BaseModel
# class SendRequest(BaseModel):
#     name: str
#     phone: int
#
#
# @app.post("/send")
# async def send(data: SendRequest):
#     print(data)
#     return '전송완료'
