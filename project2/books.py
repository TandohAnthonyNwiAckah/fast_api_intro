from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int

    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date


class BookRequest(BaseModel):
    id: Optional[int] = Field(description='ID is not needed on create', default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)
    published_date: int = Field(gt=1999, lt=2031)


BOOKS = [
    Book(1, 'PYTHON', 'Tanacom', 'A very nice book!', 5, 2028),
    Book(2, 'KOTLIN', 'Tanacom', 'A great book!', 4, 2025),
    Book(3, 'C++', 'Tanacom', 'A awesome book!', 4, 2026),
    Book(4, 'JAVA', 'Tony', 'Book Description', 5, 2027),
    Book(5, 'PHP', 'Anthony', 'Book Description', 5, 2027),
    Book(6, 'DART', 'Jane', 'Book Description', 4, 2026),
    Book(7, 'JAVASCRIPT', 'TONY', 'Book Description', 4, 2024)
]


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.post("/create-book")
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))


def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book
