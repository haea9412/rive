from passlib.context import CryptContext
from models import Users
from sqlalchemy.orm import Session
from datetime import datetime
from domain.users.users_schema import UserCreate
import hashlib


#pwd_context = CryptContext(schemes=["bcrypt"], deprecated = 'auto')


def create_user(db: Session, user_create: UserCreate):
    passwd = user_create.user_pw + "1324756931"
    hashcode = hashlib.sha512(passwd.encode("utf-8")).hexdigest()
    db_user = Users(user_id = user_create.user_id + 1,
                    username = user_create.username,
                    #user_pw = user_create.user_pw1,
                    user_pw = hashcode,
                    email = user_create.email,
                    create_date = datetime.now())
    db.add(db_user)
    db.commit()


def get_user(db: Session, user_login: Users):
    user = db.query(Users).filter(Users.username == user_login.username).all()
    return user

def get_existing_user(db: Session, user_create: UserCreate):
    return db.query(Users).filter((Users.username == user_create.username) | (Users.email == user_create.email)).first()