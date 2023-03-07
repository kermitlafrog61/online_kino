from app.queries.posts import (
    get_posts,
    get_post_by_id,
    create_post,
    delete_post,
    update_post
    )
from app.schemas.posts import PostCreateSchema

from fastapi import APIRouter

router = APIRouter()

@router.get('/posts')
def get_films():
    return get_posts()


@router.post('/create-post')
def create_film(film: PostCreateSchema):
    return create_post(film)


@router.get('/posts/{post_id}')
def get_film_by_id(post_id: int):
    return get_post_by_id(post_id)