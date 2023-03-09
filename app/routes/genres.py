from app.queries.genres import (
    create_genre, get_genres,
    get_genre_by_id, delete_genre
)
from app.schemas.genres import GenreCreateSchema

from fastapi import APIRouter


genre_router = APIRouter()


@genre_router.post('/genres/create')
def post_genre(genre_in: GenreCreateSchema):
    return create_genre(genre_in)


@genre_router.get('/genres/all')
def get_all_genres():
    return get_genres()


@genre_router.get('/genres/{genre_id}')
def get_genre_films(genre_id: int):
    return get_genre_by_id(genre_id)


@genre_router.delete('/genres/{genre_id}/delete')
def remove_genre(genre_id: int):
    return delete_genre(genre_id)
