from app.queries.posts import (
    create_post, get_posts, get_post_by_id,
    update_post, delete_post
)
from app.schemas.posts import PostCreateSchema

from fastapi import APIRouter


post_router = APIRouter()


@post_router.post('/posts/create')
def post_film(film_in: PostCreateSchema):
    return create_post(film_in)


@post_router.get('/posts/all')
def get_all_films():
    return get_posts()


@post_router.get('/posts/{post_id}')
def get_film_by_id(post_id: int):
    return get_post_by_id(post_id)


@post_router.put('/posts/{post_id}/update')
def update_film(post_id: int, film_in: PostCreateSchema):
    return update_post(post_id, film_in)


@post_router.delete('/posts/{post_id}/delete')
def delete_film(post_id: int):
    return delete_post(post_id)
