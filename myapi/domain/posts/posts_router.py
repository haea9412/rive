from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from starlette import status

from database import get_db
from domain.posts import posts_schema, posts_crud


#post router 생성
router = APIRouter(
    prefix="/api/posts",
)


#post router를 FastAPI에 등록. .get() 요청되면 prefix 등록된 posts_list 실행
@router.get("/list")
def posts_list(db: Session = Depends(get_db), page: int = 0, size: int = 10):
    total, _posts_list = posts_crud.get_posts_list(db, skip=page*size, limit=size)
    return {'total': total, 'posts_list': _posts_list}


@router.get("/list/{post_id}", response_model = posts_schema.Posts)
def posts_detail(post_id: int, db: Session = Depends(get_db)):
    posts = posts_crud.get_post(db, post_id=post_id)
    return posts

@router.post("/create", status_code = status.HTTP_204_NO_CONTENT)
def post_create(_post_create: posts_schema.Posts, db: Session = Depends(get_db)):
    posts_crud.create_post(db = db, post_create=_post_create)

@router.get("/list/user/{user_id}")
def post_userlist(user_id: int, db: Session = Depends(get_db)):
     posts = posts_crud.user_postlist(db, user_id=user_id)
     return posts