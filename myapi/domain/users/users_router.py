
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status


from database import get_db
from domain.users import users_crud, users_schema

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


#post
@router.post("/login")
def user_login(_user_login: users_schema.Users,
               db: Session = Depends(get_db)):
    user = users_crud.get_user(db = db, user_login=_user_login)
    if user:
        return 1
    else:
        return 0