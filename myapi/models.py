from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship

from database import Base

# user 이용자 계정
class users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False)
    passwd = Column(String(20), nullable=False)
    create_at = Column(DateTime,default=datetime.now(),  nullable=False)

# posts 전체 게시판 글 모음
# type 1: 자유게시판, 2: , ... 하면서 추가
class posts(Base):
    __tablename__ = "posts"

    type = Column(Integer, nullable=False)
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    create_at = Column(DateTime, default=datetime.now(), nullable=False)
    # 나중에 조회수, 파일 업로드 등 추가

# answers 댓글 모음
class answers(Base):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey("posts.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    content = Column(Text, nullable=False)
    create_at = Column(DateTime, default=datetime.now(), nullable=False)


