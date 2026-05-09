from fastapi import FastAPI, Body

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


@app.get("/books/{title_name}")        
async def read_one_book(parameter:str):
    for book in BOOKS:
        if book.get('title').casefold() == parameter.casefold():
            return book



@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break