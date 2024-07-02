from models import Posts
from sqlalchemy.orm import Session

def get_posts_list(db: Session):
    posts_list = db.query(Posts)\
        .order_by(Posts.create_at.desc())\
        .all()
    return posts_list

def get_posts(db: Session, posts_id: int):
    posts = db.query(Posts).get(posts_id)
    return posts