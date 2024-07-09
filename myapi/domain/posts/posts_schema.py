import datetime
from pydantic import BaseModel, field_validator



class Posts(BaseModel):
    type: int
    post_id: int | None = None
    user_id: int | None  = None
    title: str
    content: str
    create_date: datetime.datetime
    #modify_date: datetime.datetime
# str|None = None : 필수 항목이 아닌 경우 들어가는 옵션(str or none, default none)

class PostCreate(BaseModel): 
    
    post_id: int  
    title: str
    content: str
    

    @field_validator('title', 'content', check_fields=False)
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v
    

#PostCreate 상속    
class PostUpdate(PostCreate):
    post_id: int

class PostList(BaseModel):
    total: int = 0
    posts_list: list[Posts] = []