from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': "Author One", 'category': "science"},
    {'title': 'Title Two', 'author': "Author Two", 'category': "science"},
    {'title': 'Title Three', 'author': "Author Three", 'category': "math"},
    {'title': 'Title Four', 'author': "Author Four", 'category': "history"},
    {'title': 'Title Five', 'author': "Author Two", 'category': "natural"},
    {'title': 'Title Six', 'author': "Author Two", 'category': "math"},
]


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.get("/books/title/{book_title}/")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book


@app.get("/books/")
async def read_category_by_query(category: str):
    books = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books.append(book)

    return books


'''
Lấy tất cả sách từ 1 tác giả cụ thể bằng cách sử dụng đường dẫn hoặc tham số truy vấn
'''


@app.get('/books/by_author/')
# @app.get('/books/by_author/{author}')
async def read_books_by_author_path(author: str):
    books = []
    for i in range(len(BOOKS)):
        if BOOKS[i].get('author').casefold() == author.casefold():
            books.append(BOOKS[i])
    return books


@app.get("/books/author/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    books = []
    for book in BOOKS:
        if (book.get('author').casefold() == book_author.casefold() and
                book.get('category').casefold() == category.casefold()):
            books.append(book)
    return books


@app.post("/books/create_book/")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)


@app.put("/books/update_book/")
async def update_book(update_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == update_book.get('title').casefold():
            BOOKS[i] = update_book


@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break
