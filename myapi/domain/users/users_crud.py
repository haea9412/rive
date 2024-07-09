from passlib.context import CryptContext
from models import Users
from sqlalchemy.orm import Session
from sqlalchemy import select
from datetime import datetime
from domain.users.users_schema import UserCreate
import hashlib
from random import randint

#pwd_context = CryptContext(schemes=["bcrypt"], deprecated = 'auto')
#hash_obj = hashlib.sha256() #해시 객체 초기화

salt = 'rive' #"1324756931"



#unique user_id 생성
def make_userid(db: Session, user_id: int):
    get_id = randint(1, 1000000) #100만명 안에서 user_id 랜덤 생성
    user = db.query(Users).filter(Users.user_id == get_id).first()
    if user:
        return make_userid(db, user_id)
    else:
        user_id = get_id
        return user_id


def create_user(db: Session, user_create: UserCreate):
     
    db_user = Users(user_id = make_userid(db,user_create.user_id),
                    username = user_create.username,
                    #user_pw = user_create.user_pw1,
                    user_pw = create_pw(user_create.user_pw1),
                    email = user_create.email,
                    create_date = datetime.now())
    return db_user

def add_user(db: Session, db_user:Users):
    db.add(db_user)
    db.commit()

#회원 탈퇴
def del_user(db: Session, username: str):
    db_user = db.execute(select(Users).filter(Users.username == username)).scalars().first()
    db.delete(db_user)
    db.commit()


#username으로 조회
def get_user(db: Session, username: str):
    user = db.query(Users).filter(Users.username == username).first()
    return user

def get_existing_user(db: Session, user_create: UserCreate):
   user = db.query(Users).filter((Users.username == user_create.username) | 
                                 (Users.email == user_create.email)).first()
   #user = db.register.find_one({'username': user_create.username, 'user_pw': user_create.user_pw1})
   return user



def create_pw(password: str):
    pw_len = len(password) #입력받은 패스워드 길이 반환
    if (8 > pw_len) | (pw_len > 30):
        return '0'
    else:
        return hash_pw(password)

        

#비밀번호 해시 암호화 함수
def hash_pw(password: str):
    pw = password + salt
    hashcode = hashlib.sha512(pw.encode("utf-8")).hexdigest()
    return hashcode
