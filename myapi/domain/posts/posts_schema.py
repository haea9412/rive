import datetime
from pydantic import BaseModel




class Posts(BaseModel):
    type: int
    id: int | None = None
    user_id: int | None  = None
    title: str
    content: str
    create_at: datetime.datetime
# str|None = None : 필수 항목이 아닌 경우 들어가는 옵션(str or none, default none)