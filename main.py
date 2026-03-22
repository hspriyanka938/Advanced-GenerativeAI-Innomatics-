from fastapi import FastAPI, Query, status
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

books = [
    {"id": 1, "title": "Python Basics", "author": "John", "genre": "Tech", "is_available": True},
    {"id": 2, "title": "History of India", "author": "Raj", "genre": "History", "is_available": True},
    {"id": 3, "title": "Science 101", "author": "Amit", "genre": "Science", "is_available": False},
    {"id": 4, "title": "Fiction Story", "author": "Riya", "genre": "Fiction", "is_available": True},
    {"id": 5, "title": "AI Future", "author": "Elon", "genre": "Tech", "is_available": True},
    {"id": 6, "title": "World War", "author": "Sam", "genre": "History", "is_available": False}
]

borrow_records = []
record_counter = 1
queue = []

def find_book(book_id):
    for book in books:
        if book["id"] == book_id:
            return book
    return None

def calculate_due_date(days):
    return f"Return by Day {10 + days}"

class BorrowRequest(BaseModel):
    member_name: str = Field(min_length=2)
    book_id: int = Field(gt=0)
    borrow_days: int = Field(gt=0, le=30)
    member_id: str = Field(min_length=4)

@app.get("/")
def home():
    return {"message": "Welcome to City Public Library"}
