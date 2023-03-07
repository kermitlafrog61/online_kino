from datetime import date

from app.models.posts.post_model import Genre, PostGenres, Post
from app.models.basemodel import db_connection, db
from app.queries.genres import create_genre, delete_genre, get_genres
from app.queries.posts import create_post, delete_post, get_posts, get_post_by_id, update_post
from app.schemas.posts import PostCreateSchema
from app.routes.posts import router

from fastapi import FastAPI 


@db
def create_tables():
    db_connection.create_tables([Genre, Post, PostGenres])

create_tables()


app = FastAPI()

app.include_router(router)


# create_genre('Детектив')
# create_genre('Ужасы')
# create_genre('Боевик')
# create_genre('Комедия')
# delete_genre('Детектив')
# print(get_genres())

# create_post(PostCreateSchema(
#     title='Batman',
#     description='Рыцарь ночи',
#     year=date(2008, 1, 1),
#     country='USA',
#     genres=['Детектив', 'Ужасы']
# ))

# update_post(
#     76,
#     'Такси',
#     '1998',
#     'Franсe',
#     ['Боевик']
# )
# print(delete_post(133))
# print(get_posts())
# print(get_post_by_id(135))


if __name__ == '__main__':
    ...
