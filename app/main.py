from dataclasses import asdict
import uvicorn
from fastapi import FastAPI
from app.database.conn import db

from app.common.config import conf
from app.router import index, auth
from app.database import schema

def create_app():
    """
    앱 함수 실행
    :return:
    """
    c = conf()
    app = FastAPI()
    conf_dict = asdict(c)
    db.init_app(app, **conf_dict)

    # 데이터 베이스 이니셜라이즈
    # from app.database import sqlalchemist as s
    # s.session.initialize(db.session, schema)

    # 레디스 이니셜라이즈

    # 미들웨어 정의

    # 라우터 정의
    app.include_router(index.router)
    app.include_router(auth.router, tags=["인증"], prefix="/auth")

    return app


app = create_app()

if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
    # uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=conf().PROJ_RELOAD)
