from fastapi import FastAPI, Body, Path, Query    # Body is class use to make a body while creating means in post method and Path is used to validate path parameter and Query is used to validate Query parameter
from fastapi import HTTPException
from pydantic import BaseModel,Field
from typing import Optional
from starlette import status        # explicitly providing code as every time api success it give 200 but in post it should be 201 which is for created

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
    id: Optional[int] = None    # As mention if you are using Optional in pydantic2 need to use None
    title: str = Field(min_length=3)
    author: str =Field(min_length=1)
    description: str=Field(min_length=1,max_length=100)
    rating: int = Field(gt=-1, lt=6)  # gt means greater than and lt means less than
    published_date: int

    # can also define model_config which show in swager in plase of example

    model_config={
        "json_schema_extra":{
            "example": {
                "title": "A new book",
                "author": "prashant saxena",
                "description":"A new description of a book",
                "rating": 5,
                "published_date": 40
            }
        }
    }


# other way in place of None use field
# class BookRequest(BaseModel):
#     id: Optional[int] = Field(description="Id is not required for creation ",default=None)   # as none is compalsory in pydantic2 and description can you read on swarger UI of flaskApi in id drop down
#     author: str =Field(min_length=1)
#     description: str=Field(min_length=1,max_length=100)
#     rating: int = Field(gt=-1, lt=6)  # gt means greater than and lt means less than
#     published_date: int




BOOKS = [
    Book(1, 'Computer Science Pro', 'codingwithroby', 'A very nice book!', 5, 2030),
    Book(2, 'Be Fast with FastAPI', 'codingwithroby', 'A great book!', 5, 2030),
    Book(3, 'Master Endpoints', 'codingwithroby', 'A awesome book!', 5, 2029),
    Book(4, 'HP1', 'Author 1', 'Book Description', 2, 2028),
    Book(5, 'HP2', 'Author 2', 'Book Description', 3, 2027),
    Book(6, 'HP3', 'Author 3', 'Book Description', 1, 2026)
]



@app.get("/",status_code=status.HTTP_200_OK())
async def first_api():            # async is option for fastapi python now directly handle this
    return {"message": "welcome to api building"}

@app.get("/api-endpoint",status_code=status.HTTP_200_OK())
async def second_api():            # async is option for fastapi python now directly handle this
    return {"message": "My name is prashant saxena"}


@app.get("/books",status_code=status.HTTP_200_OK())
async def read_all_books():            # async is option for fastapi python now directly handle this
    return BOOKS



# so here when we use post data can't put any type of validation so that why we need pydantic
# @app.post("/create-book")
# async def create_book(book_request=Body()):
#     BOOKS.append(book_request)




@app.post("/create-book",status_code=status.HTTP_201_CREATED)
async def create_book(book_request:BookRequest):
    print(type(book_request)) 
    new_book= (Book(**book_request.model_dump()))
    print(type(new_book))
    BOOKS.append(find_book_id(new_book))  #but there should be increment in id if new book is going to insert so we neet to make funciton for that

# so there should be increment in id if new book is going to insert

def find_book_id(book:Book):   # don't use async here as it need to run as this file run
    if len(BOOKS)>0:
        book.id= BOOKS[-1].id+1
    else:
        book.id=1

    return book


# other way of above function
# def find_book_id(book:Book):   # don't use async here as it need to run as this file run
#     book.id=1 if len(BOOKS) ==0 else BOOKS[-1].id +1
#     return book



# using of Path for validating path parameter
@app.get("/books/{book_id}")        
async def read_one_book(book_id:int=Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
        
    raise HTTPException(status_code=404,detail="Item not found")
        



@app.put("/books/update_book",status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book:BookRequest):
    book_change=False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            book_change=True
    
    if not book_change:
        raise HTTPException(status_code=404, detail='book not found')




# using of Query for validating Query parameter
@app.get("/books/")                     # query paramenter
async def read_book_by_rating(book_rating: int=Query(gt=0,lt=6)):
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return



"""if you are directly appending book_request so it give data will be correct but its 
    data type is of BookRequest and the previous are Book type as it dirctly create by 
     Book class so list is mix of two data type that why we need to use Book(**book_request.model_dump())"""


