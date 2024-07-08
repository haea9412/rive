import models


from typing import Union
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from domain.answers import answer_router
from domain.posts import posts_router
from domain.users import users_router

from database import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

origins = [
    "http://127.0.0.1:3000",
    "0.0.0.0:3000",
    "http://localhost:3000",
    "http://127.0.0.1:80",
    "0.0.0.0:80",
    "http://localhost:80"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"], 
)


"""
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

"""
app.include_router(posts_router.router)
app.include_router(answer_router.router)
app.include_router(users_router.router)
