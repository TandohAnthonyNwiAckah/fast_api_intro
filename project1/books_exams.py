"""
Assignment

Here is your opportunity to keep learning!

1. Create a new API Endpoint that can fetch all books from a specific author using either Path Parameters or Query Parameters.

"""

from fastapi import FastAPI

app = FastAPI()

books_data = [
    {"author": "John", "book": "General Programming"},
    {"author": "Elizabeth", "book": "Discrete Math"},
    {"author": "Jane", "book": "General Math"},
    {"author": "Joseph", "book": "Electronics"},
    {"author": "John", "book": "General English"},
    {"author": "Jane", "book": "Artificial Intelligence"},
    {"author": "Mary", "book": "Data Science"},
    {"author": "John", "book": "Wireless Communication"},
    {"author": "Jane", "book": "General Art"},
    {"author": "Moses", "book": "Digital Signaling"},
]


@app.get("/fetch_book")
async def fetch_all_books(author: str):
    all_books = []
    for book in books_data:
        if book["author"].casefold() == author.casefold():
            all_books.append(book)
    return all_books
