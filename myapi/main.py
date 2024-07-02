from typing import Union
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from domain.posts import posts_router

app = FastAPI()


origins = [
    "http://127.0.0.1:3000",
    "0.0.0.0:3000",
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

