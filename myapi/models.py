from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship

from database import Base


# user 이용자 계정
class Users(Base):
    __tablename__ = "users"

    user_id = Column(Integer, unique=True, primary_key=True, autoincrement=False)
    username = Column(String(20), nullable=False, unique=True)
    user_pw = Column(String(128), nullable=False)
    email = Column(String, unique=True, nullable=False)
    create_date = Column(DateTime,default=datetime.now(),  nullable=False)

# posts 전체 게시판 글 모음
# type 1: 자유게시판, 2: , ... 하면서 추가
class Posts(Base):
    __tablename__ = "posts"

    type = Column(Integer, nullable=False)
    post_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=True)
    user = relationship("Users", backref="posts_users")
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, default=datetime.now(), nullable=False)
    #modify_date = Column(DateTime, nullable=True)
    # 나중에 조회수, 파일 업로드 등 추가


# answers 댓글 모음
class Answers(Base):
    __tablename__ = "answers"

    answer_id = Column(Integer, primary_key=True, autoincrement=True)
    post_id = Column(Integer, ForeignKey("posts.post_id"))
    user_id = Column(Integer, ForeignKey("users.user_id"))
    user = relationship("Users", backref="answers_users")
    content = Column(Text, nullable=True)
    create_date = Column(DateTime, default=datetime.now(), nullable=False)
    #modify_date = Column(DateTime, nullable=True) #nullables

