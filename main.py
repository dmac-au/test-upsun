from typing import List
from sqlalchemy import select
from fastapi import FastAPI
from sqlalchemy.orm import Session
import logging

from db import engine
from db.models import DbAuthor, DbBook
from schema import Book, Author

app = FastAPI()

api_path = "/api/v1"

logging.basicConfig(
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get(f"{api_path}/books")
async def get_books():
    with Session(engine) as session:
        books = session.query(DbBook).all()
        return [
            {"id": book.id, "title": book.title, "author": book.author}
            for book in books
        ]


@app.post(f"{api_path}/books")
async def create_book(books: List[Book] | Book):
    number_of_books = 0
    with Session(engine) as session:
        if isinstance(books, List):
            number_of_books = len(books)
            session.add_all([DbBook(**dict(book)) for book in books])
        else:
            number_of_books = 1
            session.add(DbBook(**dict(books)))
        session.commit()
    return {"message": f"{number_of_books} books created"}
