from typing import List, Optional
from pydantic import BaseModel


class Book(BaseModel):
    id: int | None = None
    title: str
    author_id: int | None = None
    author: Optional["Author"] = None


class Author(BaseModel):
    id: int | None = None
    name: str
    books: List[Book] | None
