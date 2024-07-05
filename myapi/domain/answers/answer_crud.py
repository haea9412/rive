from datetime import datetime

from sqlalchemy.orm import Session

from domain.answers.answer_schema import AnswerCreate
from models import Posts, Answers, Users

def create_answer(db: Session, post_id: int, answer_create: AnswerCreate):#, user: Users):
    db_answer = Answers(post_id = post_id,
                       content = answer_create.content,
                       create_date = datetime.now())
#                       user = user)
    db.add(db_answer)
    db.commit()

def get_answers_list(db: Session, post_id: int):
    answers_list = db.query(Answers).filter(Posts.post_id == post_id).all()
    return answers_list
    
