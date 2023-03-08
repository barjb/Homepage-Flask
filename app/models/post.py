from typing import List
from datetime import datetime
from sqlalchemy import String, Text, DateTime
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from dataclasses import dataclass
from app.extensions import db
from sqlalchemy.sql import func


@dataclass
class Post(db.Model):
    __tablename__ = 'post'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(30))
    tags: Mapped[List["Tag"]] = relationship(
        back_populates="post", cascade='all, delete-orphan')
    text: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now())

    def __repr__(self) -> str:
        return f"Post(id={self.id!r}, title={self.title!r} tags=[{self.tags!r}])"

    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'tags': [tag.as_dict() for tag in self.tags],
            'text': self.text,
            'created_at': self.created_at.isoformat()
        }


class Tag(db.Model):
    __tablename__ = 'tag'
    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(String(30))
    post_id = mapped_column(ForeignKey("post.id"))
    post: Mapped[Post] = relationship(back_populates="tags")

    def __repr__(self) -> str:
        return f"Tag(id={self.id!r}, text={self.text!r})"

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @property
    def serialize(self):
        return {
            'id': self.id,
            'text': self.text
        }
