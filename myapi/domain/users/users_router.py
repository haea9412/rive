
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status


from database import get_db
from domain.users import users_crud, users_schema

router = APIRouter(
    prefix="/api/users",
)


@router.post("/create", status_code = status.HTTP_204_NO_CONTENT)
def user_create(_user_create: users_schema.Users,
                db: Session = Depends(get_db)):
    users_crud.create_user(db = db, user_create=_user_create)


#post
@router.post("/login")
def user_login(_user_login: users_schema.Users, db: Session = Depends(get_db)):
    user = users_crud.get_user(db = db, user_login=_user_login)
    return user