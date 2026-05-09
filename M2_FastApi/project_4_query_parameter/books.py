from fastapi import FastAPI

app = FastAPI()


BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]

# always rember endpoint path should be different otherwise  as fastapi run in chronological order
# as ot run top to bottom so will run the first one

@app.get("/")
async def first_api():            # async is option for fastapi python now directly handle this
    return {"message": "welcome to api building"}



@app.get("/books")
async def read_all_books():            # async is option for fastapi python now directly handle this
    return BOOKS



@app.get("/books/")                     # query paramenter
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return



# Get all books from a specific author using path or query parameters both
@app.get("/books/{books_author}/")
async def read_books_by_author_path(books_author: str,category:str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == books_author.casefold() and \
            book.get('category').casefold() == category.casefold():

            books_to_return.append(book)

    return books_to_return




