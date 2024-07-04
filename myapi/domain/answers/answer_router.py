from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from domain.answers import answer_schema, answer_crud
from domain.posts import posts_crud
#from domain.users.users_router import get_current_user
from models import Users

router = APIRouter(
    prefix = "/api/answer",
)

#입력: answer_schema.AnswerCreate , 출력: 없음
@router.post("/create/{post_id}", status_code = status.HTTP_204_NO_CONTENT) #204: 응답없음
def answer_create(post_id: int,
                  _answer_create: answer_schema.AnswerCreate,
                  db: Session = Depends(get_db),):
                  #current_user: Users = Depends(get_current_user)):
        #create answer
        post = posts_crud.get_post(db, post_id=post_id)
        if not post:
                raise HTTPException(status_code = 404, detail = "Post not found")
        answer_crud.create_answer(db, post_id = post_id,
                                  answer_create=_answer_create)
                                  #user = current_user)

#answer_list
@router.post("/list", response_model = list[answer_schema.Answers])
def answer_list(post_id: int, db: Session = Depends(get_db)):
        _answer_list = answer_crud.get_answers_list(db, post_id=post_id)
        return _answer_list