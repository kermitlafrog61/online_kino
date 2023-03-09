from datetime import date

from app.models.posts.post_model import Genre, PostGenres, Post
from app.models.basemodel import db_connection, db
from app.queries.genres import create_genre, delete_genre, get_genres
from app.queries.posts import create_post, delete_post, get_posts, get_post_by_id, update_post
from app.schemas.posts import PostCreateSchema
from app.routes.posts import post_router
from app.routes.genres import genre_router

from fastapi import FastAPI


@db
def create_tables():
    db_connection.create_tables([Genre, Post, PostGenres])

# create_tables()


app = FastAPI()


app.include_router(post_router)
app.include_router(genre_router)
