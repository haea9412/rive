from datetime import datetime

from domain.posts.posts_schema import PostCreate
from models import Posts
from sqlalchemy.orm import Session

def get_posts_list(db: Session):
    posts_list = db.query(Posts)\
        .order_by(Posts.create_date.desc())\
        .all()
    return posts_list

def get_post(db: Session, post_id: int):
    posts = db.query(Posts).get(post_id)
    return posts

def create_post(db: Session, post_create: Posts):
    db_post = Posts(type = post_create.type,
                    user_id=post_create.user_id,
                    title = post_create.title,
                    content = post_create.content,
                    create_date = datetime.now())
    db.add(db_post)
    db.commit()

def user_postlist(db: Session, user_id: int):
    posts_list = db.query(Posts).filter(Posts.user_id == user_id).all()
    return posts_list