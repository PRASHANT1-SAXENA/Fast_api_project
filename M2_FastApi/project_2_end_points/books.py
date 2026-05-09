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


@app.get("/")
async def first_api():            # async is option for fastapi python now directly handle this
    return {"message": "welcome to api building"}

@app.get("/api-endpoint")
async def second_api():            # async is option for fastapi python now directly handle this
    return {"message": "My name is prashant saxena"}


@app.get("/books")
async def read_all_books():            # async is option for fastapi python now directly handle this
    return BOOKS

# you must check api on swagger ui for better understanding
# on api endpoint docs like here http://127.0.0.1:8000/docs and you can override or disable this in production 