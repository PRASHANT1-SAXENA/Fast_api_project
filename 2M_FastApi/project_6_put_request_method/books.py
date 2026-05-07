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


@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book