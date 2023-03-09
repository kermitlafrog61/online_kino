from peewee import IntegrityError, DoesNotExist, fn

from app.models.posts.post_model import Genre, Post, PostGenres
from app.models.basemodel import db
from app.schemas.genres import GenreAllSchema, GenreOneSchema, GenreCreateSchema


@db
def create_genre(genre_in: GenreCreateSchema):
    try:
        genre = Genre.create(title=genre_in.title)
        # INSERT INTO genre(title) VALUES ('Детектив')

    except IntegrityError:
        genre = 0

    return genre


@db
def get_genres():
    genres = Genre.select(Genre.id, Genre.title)
    return [GenreAllSchema.from_orm(genre) for genre in genres]


@db
def get_genre_by_id(genre_id: int):
    genre = (Genre.select(Genre, fn.array_agg(Post.title)
                          .alias('films_title'))
             .join(PostGenres)
             .join(Post)
             .where(Genre.id == genre_id)
             .group_by(Genre.id)
             .get_or_none())

    if not genre:
        return 0

    return dict(GenreOneSchema.from_orm(genre))


@db
def delete_genre(genre_id: int):
    try:
        genre = Genre.get_by_id(genre_id)
        films = Post.select()
        genre.films.remove(films)
        genre.delete_instance()

    except DoesNotExist:
        genre = 0

    return genre
