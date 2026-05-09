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

# Example :- but comment it other wise due to same link it will not run below one
# @app.get("/books/{title_name}")        # example of dynamic parameter
# async def read_one_book(title_name):
#     return {'title_name': title_name} 



# example of static parameter and as if it will match with dynamic parameter below so make
#  sure static one should be above other it consider it as dynamic paramenter
@app.get("/books/mybook")        
async def read_one_book(parameter:str):
    return {'message':"my faviorate book"}


# example of dynamic parameter

@app.get("/books/{title_name}")        
async def read_one_book(title_name:str):
    for book in BOOKS:
        if book.get('title').casefold() == title_name.casefold():
            return book