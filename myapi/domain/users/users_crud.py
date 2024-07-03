from models import Users
from sqlalchemy.orm import Session
from datetime import datetime
from domain.users.users_schema import UserCreate

def create_user(db: Session, user_create: Users):
    db_user = Users(user_id = user_create.user_id + 1,
                    username = user_create.username,
                    user_pw = user_create.user_pw,
                    create_date = datetime.now())
    db.add(db_user)
    db.commit()


def get_user(db: Session, user_login: Users):
    user = db.query(Users).filter(Users.username == user_login.username).all()
    return user
