import datetime
from pydantic import BaseModel, field_validator, EmailStr
from pydantic_core.core_schema import FieldValidationInfo
import models


class Users(BaseModel):
    user_id: int
    username: str
    user_pw: str
    create_date: datetime.datetime


class UserCreate(BaseModel):

    user_id: int
    username: str
    user_pw1: str
    user_pw2: str
    email: EmailStr

    @field_validator('username', 'user_pw1', 'user_pw2', 'email', check_fields=False)
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v
    

    @field_validator('user_pw2')
    def passwords_match(cls, v, info: FieldValidationInfo):
        if 'user_pw1' in info.data and v != info.data['user_pw1']:
            raise ValueError("비밀번호가 일치하지 않습니다.")
        return v
    
#login api 출력 스키마
class Token(BaseModel):
    access_token: str
    token_type: str
    username: str
    user_id: int