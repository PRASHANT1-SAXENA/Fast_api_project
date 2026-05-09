from typing import Annotated
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from fastapi import FastAPI , HTTPException, Depends,Path
from starlette import status
import a2Database_tables_Models as models
from a2Database_tables_Models import Todos
from a1Database_Connection__with_ORM import engine ,SessionLocal



app = FastAPI()

models.Base.metadata.create_all(bind=engine) 
"""this command models.Base.metadata.create_all(bind=engine) it will create your todos.db file
 here
if you change something in  model in database2_table_models.py you need to delete it and run it 
again later you will learn how to handle this situatin without deleting this file
"""


"""
after creating todos.db file here install sqllite  on computer by just downloading and in c drive an set evinoment path of 
you system then on cmd sqlite3 todos.db after making the todos.db file this cmd will mimic you table 
in your database which you installed.
"""


def get_db():
    db=SessionLocal()
    try:
        yield db

    finally:
        db.close()


"""yield is a built-in keyword in Python. Like: if, for, return Main use: yield turns a 
function into a generator. Difference: return Ends function completely.yield
Pauses function and can resume later."""




"""Depends() in FastAPI is used for dependency injection.
Main purpose: It tells FastAPI: “Run this function first, and give me its result.
What happens:
Calls get_db()-> Creates DB session-> Passes session to route-> Closes session after request
"""

"""
Annotated in Python adds extra metadata/instructions to a type hint.
structure :- Annotated[type, extra_info]
example age: Annotated[int, "Must be positive"]
old style:- db: Session = Depends(get_db)
new style:- db: Annotated[Session, Depends(get_db)]

Why use it?
It lets you say:-“This variable is this type, plus extra behavior.”
"""


"""Normal function:
def test():
    print("A")
    print("B")

Runs fully: A → B → End
With yield:
def test():
    print("A")
    yield "value"
    print("B")

Execution:
First call: Prints A-> Pause until Returns values:-> Later resume: Prints B Ends
"""

@app.get("/")
async def check():
    return "all good upto here with code till not fetching data "


""" Bellow api  will work when you have install sqllite properly in system and have that todos table 
which is send by todos.db with this command on cmd sqlite3 todos.db and you must have this todos.db file 
for this cmd just check on cmd when sqlite is running then give this cmd only .schema
"""


# @app.get("/show_data")
# async def read_all(db: Annotated[Session, Depends(get_db)]):
#     try:
#         return db.query(Todos).all()
#     except Exception:
#         raise HTTPException(status_code=500, detail="Not able to connect database")
    


db_dependency=Annotated[Session,Depends(get_db)]



@app.get("/todo/{todo_id}",status_code=status.HTTP_200_OK)
async def read_todo(db:db_dependency,todo_id:int=Path(gt=0)):
    todo_model=db.query(Todos).filter(Todos.id==todo_id).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404,detail="Todo not found")


# we will not pass the id as it is the primary key and it waill handle by sqlachemy as it made there itself, after increment.
class TodoRequest(BaseModel):
    title:str = Field(min_length=3)
    description:str =Field(min_length=3,max_length=100)
    priority:int = Field(gt=0,lt=6)
    complete:bool


@app.post("/todo",status_code=status.HTTP_201_CREATED)
async def create_todo(db:db_dependency,todo_request:TodoRequest):
    todo_model=Todos(**todo_request.model_dump())

    db.add(todo_model)
    db.commit()



# In FastAPI, parameter order matters because Python requires non-default parameters before or above default parameters.
@app.put("/todo/{todo_id}",status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(db:db_dependency,
                      todo_request:TodoRequest,     # In FastAPI, parameter order matters because Python requires non-default parameters before default parameters. if todo_request below todo_id then is show error
                      todo_id:int = Path(gt=0)):
    todo_model=db.query(Todos).filter(Todos.id==todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    todo_model.title=todo_request.title
    todo_model.description=todo_request.description
    todo_model.priority=todo_request.priority
    todo_model.complete=todo_request.complete

    db.add(todo_model)
    db.commit()


@app.delete("/todo/{todo_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(db:db_dependency,todo_id:int=Path(gt=0)):
    todo_model= db.query(Todos).filter(Todos.id==todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.query(Todos).filter(Todos.id==todo_id).delete()


""" After this we have made a5_Routers_Authentication&Authoization folder in the 
same directory and also make files there use it here """




    





    