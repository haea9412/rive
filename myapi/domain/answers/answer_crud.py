from datetime import datetime

from sqlalchemy.orm import Session

from domain.answers.answer_schema import AnswerCreate
from models import Posts, Answers

def create_answer(db: Session, posts: Posts, answer_create: AnswerCreate):
    db_answer = Answers(posts = posts,
                       content = answer_create.content,
                       create_date = datetime.now())
    db.add(db_answer)
    db.commit()
