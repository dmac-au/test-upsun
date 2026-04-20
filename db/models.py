from typing import Optional, List

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class DbAuthor(Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String())

    books: Mapped[List["DbBook"]] = relationship(back_populates="author")

    def __repr__(self) -> str:
        return f"Author(id={self.id!r}, name={self.name!r})"


class DbBook(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[int] = mapped_column(String())
    author_id: Mapped[Optional[int]] = mapped_column(ForeignKey("authors.id"))
    author: Mapped[DbAuthor] = relationship(back_populates="books")
