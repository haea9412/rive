from datetime import timedelta, datetime

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from domain.users import users_crud, users_schema
import hashlib


ACCESS_TOKEN_EXPIRE_MINUTES = 60 *24
SECRET_KEY = "4ab2fce7a6bd79e1c014396315ed322dd6edb1c5d975c6b74a2904135172c03c"
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/users/login")


router = APIRouter(
    prefix="/api/users",
)


#unique user create
@router.post("/create", status_code = status.HTTP_204_NO_CONTENT)
def user_create(_user_create: users_schema.UserCreate,
                db: Session = Depends(get_db)):  
    user = users_crud.get_existing_user(db,user_create=_user_create)
    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail='이미 존재하는 사용자입니다.')
    user2 = users_crud.create_user(db = db, user_create=_user_create)
    if len(user2.user_pw) <= 1:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail='잘못된 비밀번호 설정입니다.')
    users_crud.add_user(db, user2)
    


#login
@router.post("/login")
def user_login(_user_login: users_schema.Users,
               db: Session = Depends(get_db)):
    user = users_crud.get_user(db = db, username=_user_login.username)
    if user:
        return True
    else:
        return False
    


#token login
@router.post("/login/token", response_model=users_schema.Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),
                           db: Session = Depends(get_db)):   
    #check user and passwd
    user = users_crud.get_user(db, form_data.username)
    h_pw = users_crud.hash_pw(form_data.password)
    if not user or not (h_pw == user.user_pw):  #error 패스워드 비교 내용 수정 필요!!!!!!!!!!!!!
    #if not user or not hashlib.verify(form_data.user_pw, user.user_pw):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password ",
            headers={"WWW-Authenticate": "Bearer"},
        ) 
    #make access token
    data = {
        "sub": user.username,
        "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    }
    access_token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "username": user.username,
        "user_id": user.user_id
    }

"""
#get user 글쓰려면 로그인 해야함
#헤더 정보 토큰값으로 사용자 정보 조회
def get_current_user(token: str = Depends(oauth2_scheme),
                     db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        token_data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        #jwt.decode() : 토큰을 복호화하여 토큰에 담겨있는 사용자명 get
        username: str = token_data.get("sub")
        if username is None:
            raise credentials_exception #사용자명이 없을 경우 예외 발생
    except JWTError:
        raise credentials_exception
    else:
        user = users_crud.get_user(db, username=username)
        if user is None:
            raise credentials_exception
        return user
"""
