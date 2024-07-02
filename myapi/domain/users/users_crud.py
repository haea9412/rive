from models import Users
from sqlalchemy.orm import Session

def create_user(db: Sessiion, user_create: Users):
    db_user = Users(user_id,
                    username,
                    user_pw,
                    create_date)
    