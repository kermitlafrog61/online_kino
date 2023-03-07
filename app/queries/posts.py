from typing import List
from datetime import date
import json
from peewee import IntegrityError, DoesNotExist, fn

from app.models.posts.post_model import Post, PostGenres, Genre
from app.models.basemodel import db
from app.schemas.posts import (
    PostAllSchema,
    PostOneSchema,
    PostCreateSchema,
    )


@db
def create_post(post_in: PostCreateSchema):
    try:
        post = Post.create(
            title=post_in.title,
            description=post_in.description,
            year=post_in.year,
            country=post_in.country
        )

        for genre in post_in.genres:
            g = Genre.get(title=genre)
            post.genres.add(g)

    except IntegrityError:
        post = 0

    return post


@db
def get_posts() -> list[Post]:
    try:
        posts = Post.select(Post.id, Post.title, Post.year)
        # SELECT title, year FROM post;
        return [{'id': post.id,
                 'title': post.title,
                 'year': post.year.year} for post in posts]

    except IntegrityError:
        return 0


@db
def get_post_by_id(id: int) -> Post:
    post = (Post
            .select(Post, fn.array_agg(Genre.title)
                    .alias('genre_title'))
            .join(PostGenres)
            .join(Genre)
            .where(Post.id == id)
            .group_by(Post.id)
            .get_or_none())

    return dict(PostOneSchema(
        id=post.id,
        title=post.title,
        description=post.description,
        year=post.year.year,
        country=post.country,
        genres=[genre.title for genre in post.genres]
    ))


@db
def delete_post(id):
    try:
        post = Post.get_by_id(id)
        genres = Genre.select()
        post.genres.remove(genres)
        post.delete_instance()

    except DoesNotExist:
        post = 0

    return post


@db
def update_post(post_id, post_in: PostCreateSchema):
    try:
        post = Post.get_by_id(post_id)
        res = (post.update(
            title=post_in.title or post.title,
            year=post_in.year or post.year,
            country=post_in.country or post.country,
            description=post_in.description or post.description)
            .where(Post.id == post_id)
            .execute())

        if post_in.genres:
            post.genres.remove(Genre.select())
            for genre in post_in.genres:
                g = Genre.get(title=genre)
                post.genres.add(g)

    except DoesNotExist:
        res = 0

    return f"Updated {res}"
