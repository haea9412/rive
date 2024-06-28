from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# alembic.init 파일 아래와 같이 수정
# sqlalchemy.url = mysql+pymysql://kitri:rive123@localhost:3306/rive

# 연결할 db URL
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://kitri:rive123@db:3306/rive"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 접속 끝나도 연결 상태 유지하기 위해 세션 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
