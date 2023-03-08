from typing import List, Optional
from app.models.post import Post, Tag
from flask import request
from app.extensions import db
from pydantic import BaseModel
from flask_pydantic import validate
from datetime import datetime


class PostDAO:
    # TO DO
    def get_all():
        return Post.query.all()

    def find_by_id(id: int):
        return db.session.execute(db.select(Post).where(Post.id == id)).scalar()

    def find_by_tag(tag: str):
        return db.session.execute(db.select(Post).where(Post.id == id)).scalars()


class ResponseModel(BaseModel):
    code: int
    message: str


class RequestBodyModel(BaseModel):
    name: str
    tags: List[str]
    text: str


class PatchBodyModel(BaseModel):
    name: Optional[str] = None
    tags: Optional[List[str]] = []


def get_all():
    posts = Post.query.all()
    return [post.serialize for post in posts]


@validate()
def create(body: RequestBodyModel):
    name = body.name
    tags = body.tags
    text = body.text
    post = Post(title=name, tags=[], text=text)
    for tag in tags:
        post.tags.append(Tag(text=tag))
    db.session.add(post)
    db.session.commit()
    return post.serialize


@validate()
def get_id(id: int):
    post = db.session.execute(
        db.select(Post).where(Post.id == id)).scalar()
    if post == None:
        return {}
    return post.serialize


@validate()
def delete_id(id: int):
    post = db.session.execute(
        db.select(Post).where(Post.id == id)).scalar()
    if post == None:
        return {}
    db.session.delete(post)
    db.session.commit()
    return post.serialize


@validate()
def put_id(id: int, body: RequestBodyModel):
    name = body.name
    tags = body.tags
    text = body.text
    post = db.session.execute(
        db.select(Post).where(Post.id == id)).scalar()
    db.session.execute(db.delete(Tag).where(Tag.post_id == id))
    if post == None:
        post = Post(id=id)
    post.title = name
    post.tags = []
    post.text = text
    for tag in tags:
        post.tags.append(Tag(text=tag))
    db.session.add(post)
    db.session.commit()
    return post.serialize


@validate()
def patch_id(id: int, body: PatchBodyModel):
    name = body.name
    tags = body.tags
    text = body.text
    post = db.session.execute(
        db.select(Post).where(Post.id == id)).scalar()
    if post == None:
        return {}
    if name:
        post.title = name
    if tags:
        post.tags = []
        for tag in tags:
            post.tags.append(Tag(text=tag))
    db.session.add(post)
    db.session.commit()
    return post.serialize


@validate()
def get_tag(tag: str):
    posts = db.session.execute(db.select(Post).join(
        Tag).where(Tag.text == tag)).scalars()
    return [post.serialize for post in posts]


def tags():
    # debugging endpoint
    tags = db.session.execute(db.select(db.distinct(Tag.text)))
    return [row[0] for row in tags]


def phantoms():
    # debugging endpoint
    tags = Tag.query.all()
    return [tag.as_dict() for tag in tags]


def del_phantom():
    # debugging endpoint
    db.session.execute(db.delete(Tag).where(Tag.post_id == None))
    db.session.commit()
    return {'res': 'ok'}
