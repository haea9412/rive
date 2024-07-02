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
@router.get("/list", response_model = list[posts_schema.Posts])
def posts_list(db: Session = Depends(get_db)):
    
    #db = SessionLocal()
    #posts_list는 db 세션 생성하여 질문 목록 조회, 리턴한다.
    #_posts_list = db.query(Posts).order_by(Posts.create_date.desc()).all()
    #db.close() #사용한 세션 반환(종료 아님)
    
    #with get_db() as db:
        #_posts_list = db.query(Posts).order_by(Posts.create_at.desc()).all()
        #오류 여부에 상관없이 with 문을 벗어나는 순간 db.close()가 실행되어 보다 안전한 코드가 된다.

    _posts_list = posts_crud.get_posts_list(db)
    return _posts_list


@router.get("/detail/{post_id}", response_model = posts_schema.Posts)
def posts_detail(post_id: int, db: Session = Depends(get_db)):
    posts = posts_crud.get_posts(db, post_id=post_id)
    return posts

@router.post("/create", status_code = status.HTTP_204_NO_CONTENT)
def post_create(_post_create: posts_schema.Posts,
                db: Session = Depends(get_db)):
        posts_crud.create_post(db = db, post_create=_post_create)

@router.get("/list/{user_id}")
def post_userlist(user_id: int, db: Session = Depends(get_db)):
     posts = posts_crud.user_postlist(db, user_id=user_id)
     return posts