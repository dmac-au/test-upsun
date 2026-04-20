from typing import List
from pydantic import BaseModel


class Book(BaseModel):
    id: int | None = None
    title: str
    author_id: int | None = None
    author: Author | None = None


class Author(BaseModel):
    id: int | None = None
    name: str
    books: List[Book] | None
