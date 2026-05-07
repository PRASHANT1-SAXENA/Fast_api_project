from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()

# here we make a Class of Book for creating books taking parameters

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
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int






BOOKS = [
    Book(1, 'Computer Science Pro', 'codingwithroby', 'A very nice book!', 5, 2030),
    Book(2, 'Be Fast with FastAPI', 'codingwithroby', 'A great book!', 5, 2030),
    Book(3, 'Master Endpoints', 'codingwithroby', 'A awesome book!', 5, 2029),
    Book(4, 'HP1', 'Author 1', 'Book Description', 2, 2028),
    Book(5, 'HP2', 'Author 2', 'Book Description', 3, 2027),
    Book(6, 'HP3', 'Author 3', 'Book Description', 1, 2026)
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



# so here when we use post data can't put any type of validation so that why we need pydantic
# @app.post("/create-book")
# async def create_book(book_request=Body()):
#     BOOKS.append(book_request)




@app.post("/create-book")
async def create_book(book_request:BookRequest):
    print(type(book_request)) 
    new_book= (Book(**book_request.model_dump()))
    print(type(new_book))
    BOOKS.append(new_book)

"""if you are directly appending book_request so it give data will be correct but its 
    data type is of BookRequest and the previous are Book type as it dirctly create by 
     Book class so list is mix of two data type that why we need to use Book(**book_request.model_dump())"""