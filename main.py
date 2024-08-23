from fastapi import FastAPI

from app.user import users
from db.session import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(
    users
)
