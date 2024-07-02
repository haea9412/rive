
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


from database import get_db



router = APIRouter(
    prefix="/api/users",
)


@router.get("/login")
def user_create(user_id: int, db: Session = Depends(get_db)):
    user_id = int(user_id)
    user_pw = int(db.session.query())


@router.get("/login")
def user_login(user_id: int, db: Session = Depends(get_db)):
    user_id = int(user_id)
    user_pw = int(db.session.query())
