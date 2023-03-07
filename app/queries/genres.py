from peewee import IntegrityError, DoesNotExist

from app.models.posts.post_model import Genre
from app.models.basemodel import db
from app.schemas.genres import GenreSchema


@db
def create_genre(genre_in: GenreSchema):
    try:
        genre = Genre.create(title=genre_in.title)
        # INSERT INTO genre(title) VALUES ('Детектив')
    except IntegrityError:
        genre = 0
    return genre


@db
def delete_genre(genre_in: GenreSchema):
    try:
        genre = Genre.get(title=genre_in.title)
        # SELECT * FROM genre WHERE title=title
        genre.delete_instance()
    except DoesNotExist:
        return 0
    return 1


@db
def get_genres():
    return [genre.title for genre in Genre.select()]
