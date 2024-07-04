from datetime import datetime

from domain.posts.posts_schema import PostCreate
from models import Posts, Users
from sqlalchemy.orm import Session

#skip: 조회한 데이터의 시작 위치, limit: 시작 위치부터 가져올 데이터 개수
def get_posts_list(db: Session, skip: int = 0, limit: int = 10):
    _posts_list = db.query(Posts).order_by(Posts.create_date.desc())
    total = _posts_list.count()
    posts_list = _posts_list.offset(skip).limit(limit).all()    
    return total, posts_list #전체 개수, 페이지 목록

def get_post(db: Session, post_id: int):
    posts = db.query(Posts).get(post_id)
    return posts

#글쓴이 정보 추가
def create_post(db: Session, post_create: PostCreate):#, user: Users):
    db_post = Posts(type = post_create.type,
                    user_id=post_create.user_id,
                    title = post_create.title,
                    content = post_create.content,
                    create_date = datetime.now())
                    #user = user)
    db.add(db_post)
    db.commit()

def user_postlist(db: Session, user_id: int):
    posts_list = db.query(Posts).filter(Posts.user_id == user_id).all()
    return posts_list