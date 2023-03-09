from pydantic import BaseModel, Field


class GenreAllSchema(BaseModel):
    id: int
    title: str

    class Config:
        orm_mode = True


class GenreCreateSchema(BaseModel):
    title: str

    class Config:
        orm_mode = True


class GenreOneSchema(BaseModel):
    id: int
    title: str
    films_title: list[str]

    class Config:
        orm_mode = True

