from pydantic import BaseModel  
from peewee import ManyToManyQuery
from datetime import date
from typing import List, Any, Optional

from app.models.posts.post_model import Genre


class PostAllSchema(BaseModel):
    id: int
    title: str
    year: date

    class Config:
        orm_mode = True


class PostOneSchema(BaseModel):
    id: int
    title: str
    description: str
    year: int
    country: str
    genres: list[str]

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class PostCreateSchema(BaseModel):
    title: str
    description: Optional[str]
    year: date
    country: str
    genres: List[str]

    class Config:
        orm_mode = True

