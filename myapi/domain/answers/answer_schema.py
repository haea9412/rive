import datetime
from pydantic import BaseModel
from pydantic.functional_validators import field_validator


class Answers(BaseModel):
    answer_id: int | None  = None
    post_id: int | None  = None
    #user_id: int | None  = None
    content: str
    create_date: datetime.datetime


class AnswerCreate(BaseModel):
    
    content: str

    @field_validator('content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v