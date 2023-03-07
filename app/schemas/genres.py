from pydantic import BaseModel  


class GenreSchema(BaseModel):
    title: str

    class Config:
        orm_mode = True



# TODO: написать схемы для жанров
# TODO: сделать вывод человеко-читабельным