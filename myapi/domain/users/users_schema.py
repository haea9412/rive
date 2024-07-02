from pydantic import BaseModel
import datetime
from pydantic import BaseModel, field_validator

class Users(BaseModel):
    user_id: int | None = None
    username: str
    user_pw: str
    create_date: datetime.datetime


class UserCreate(BaseModel):

    user_id: int
    username: str
    user_pw: str

    @field_validator('username', 'user_pw', check_fields=False)
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v