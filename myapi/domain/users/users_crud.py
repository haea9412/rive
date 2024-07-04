from passlib.context import CryptContext
from models import Users
from sqlalchemy.orm import Session
from datetime import datetime
from domain.users.users_schema import UserCreate
import hashlib


#pwd_context = CryptContext(schemes=["bcrypt"], deprecated = 'auto')
#hash_obj = hashlib.sha256() #해시 객체 초기화

salt = 'rive' #"1324756931"
def create_user(db: Session, user_create: UserCreate):
     
    db_user = Users(user_id = user_create.user_id + 1,
                    username = user_create.username,
                    #user_pw = user_create.user_pw1,
                    user_pw = hash_pw(user_create.user_pw1),
                    email = user_create.email,
                    create_date = datetime.now())
    db.add(db_user)
    db.commit()


#username으로 조회
def get_user(db: Session, username: str):
    user = db.query(Users).filter(Users.username == username).first()
    return user

def get_existing_user(db: Session, user_create: UserCreate):
   user = db.query(Users).filter((Users.username == user_create.username) | (Users.email == user_create.email)).first()
   #user = db.register.find_one({'username': user_create.username, 'user_pw': user_create.user_pw1})
   return user

#비밀번호 해시 암호화 함수
def hash_pw(password: str):
    pw = password + salt
    hashcode = hashlib.sha512(pw.encode("utf-8")).hexdigest()
    return hashcode