from enum import Enum
from pydantic.main import BaseModel
from pydantic.networks import EmailStr

"""
DB 모델이 아닌 Validation 체크용 모듈이다.
request, response 
모든 데이터를 객체화 시켜서 사용할 수 있도록 만든 model
"""


class UserRegister(BaseModel):
    email: EmailStr = None
    pw: str = None


class SnsType(str, Enum):
    email: str = "email"
    facebook: str = "facebook"
    google: str = "google"
    kakao: str = "kakao"


class Token(BaseModel):
    Authorization: str = None


class UserToken(BaseModel):
    id: int
    pw: str = None
    email: str = None
    name: str = None
    phone_number: str = None
    profile_img: str = None
    sns_type: str = None

    class Config:
        orm_mode = True
