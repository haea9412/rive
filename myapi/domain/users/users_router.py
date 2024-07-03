from datetime import timedelta, datetime

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
import jwt

from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from domain.users import users_crud, users_schema
from domain.users.users_crud import hashlib


ACCESS_TOKEN_EXPIRE_MINUTES = 60 *24
SECRET_KEY = "4ab2fce7a6bd79e1c014396315ed322dd6edb1c5d975c6b74a2904135172c03c"
ALGORITHM = "HS256"

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
    users_crud.create_user(db = db, user_create=_user_create)


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
    #if not user or not h.verify(form_data.user_pw, user.user_pw):
    if not user or not hashlib.verify(form_data.user_pw, user.user_pw):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
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
        "username": user.username
    }
