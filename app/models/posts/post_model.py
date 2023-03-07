import peewee as pw

from app.models.basemodel import AbstractModel


class Genre(AbstractModel):
    title = pw.CharField(100, unique=True)


class Post(AbstractModel):
    title = pw.CharField(100, unique=True)
    description = pw.TextField(null=True)
    year = pw.DateField(formats=['%Y'])
    country = pw.CharField(100)
    genres = pw.ManyToManyField(Genre, backref='films')


PostGenres = Post.genres.through_model
# class PostGenres(AbstractModel):
#     post_id = pw.ForeignKeyField(Post)
#     genre_id = pw.ForeignKeyField(Genre)
