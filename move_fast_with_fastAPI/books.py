from typing import Optional
from fastapi import FastAPI, Body, Path, Query, HTTPException
from pydantic import BaseModel, Field
from starlette import status

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: float
    published_date: int

    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date


class BookRequest(BaseModel):
    id: Optional[int] = Field(None, title='id is not needed')
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=200)
    rating: float = Field(gt=-1, lt=6)  # lớn hơn -1 bé hơn 6(gt, lt viết tắt greater than,less than )
    published_date: int = Field(gte=1900, lte=2100)

    class Config:
        json_schema_extra = {
            'example': {
                'title': 'A new book',
                'author': 'name author',
                'description': 'A new description of a book',
                'rating': 5.0,
                'published_date': 2029,
            }
        }


# Tạo danh sách BOOKS
BOOKS = [
    Book(
        1,
        "The Enchanted Forest",
        "Eleanor Woods",
        "A magical tale of courage and friendship set in a mysterious forest where myths come to life.",
        4.9,
        2021
    ),
    Book(
        2,
        "Beyond the Stars",
        "James Orion",
        "An epic journey of a young astronaut venturing into the unknown to discover the secrets of the universe.",
        4.7,
        2025
    ),
    Book(
        3,
        "Shadows of the Past",
        "Lila Harper",
        "A gripping mystery about a detective uncovering dark secrets in a seemingly idyllic small town.",
        4.8,
        2030
    ),
    Book(
        4,
        "Flavors of the World",
        "Chef Antonio Rossi",
        "A delightful culinary exploration of exotic recipes and the stories behind them from around the globe.",
        4.6,
        2030
    ),
    Book(
        5,
        "Chronicles of the Dragon King",
        "Marcus Flint",
        "A legendary fantasy saga of a warrior's quest to unite warring kingdoms and reclaim a lost throne.",
        4.85,
        2011
    ),
]


@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS


@app.get("/books/publish/", status_code=status.HTTP_200_OK)
async def read_books_published(published_date: int = Query(gt=2000, lte=2025)):
    books = []
    for i in range(len(BOOKS)):
        if BOOKS[i].published_date == published_date:
            books.append(BOOKS[i])
    return books


@app.get('/books/{id}', status_code=status.HTTP_200_OK)
async def read_book(id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == id:
            return book
    raise HTTPException(status_code=404, detail='Item not found')


@app.get('/books/', status_code=status.HTTP_200_OK)
async def read_book_by_rating(rating: float = Query(gt=0, lt=6)):
    books = []
    for book in BOOKS:
        if book.rating == rating:
            books.append(book)
    return books


@app.post('/books/create_book/', status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.dict())
    BOOKS.append(find_book_id(new_book))


def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    # if len(BOOKS) > 0:
    #     book.id = BOOKS[-1].id + 1
    # else:
    #     book.id = 1

    return book


@app.put('/books/update_book/',status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            book_changed = True
    if not book_changed:
        raise HTTPException(status_code=404, detail='Item not found')


@app.delete('/books/{id}/',status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(id: int = Path(gt=0)):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == id:
            BOOKS.pop(i)
            book_changed = True
            break
    if not book_changed:
        raise HTTPException(status_code=404, detail='Item not found')
