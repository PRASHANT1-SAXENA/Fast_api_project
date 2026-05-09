from typing import Annotated
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from fastapi import FastAPI , HTTPException, Depends,Path, APIRouter
from starlette import status
import a2Database_tables_Models as models
from a2Database_tables_Models import Todos
from a1Database_Connection__with_ORM import SessionLocal

# we will not pass the id as it is the primary key and it waill handle by sqlachemy as it made there itself, after increment.



router=APIRouter()

def get_db():
    db=SessionLocal()
    try:
        yield db

    finally:
        db.close()

class TodoRequest(BaseModel):
    title:str = Field(min_length=3)
    description:str =Field(min_length=3,max_length=100)
    priority:int = Field(gt=0,lt=6)
    complete:bool



@router.get("/")
async def check():
    return "all good upto here with code till not fetching data "




# @router.get("/show_data")
# async def read_all(db: Annotated[Session, Depends(get_db)]):
#     try:
#         return db.query(Todos).all()
#     except Exception:
#         raise HTTPException(status_code=500, detail="Not able to connect database")
    


db_dependency=Annotated[Session,Depends(get_db)]



@router.get("/todo/{todo_id}",status_code=status.HTTP_200_OK)
async def read_todo(db:db_dependency,todo_id:int=Path(gt=0)):
    todo_model=db.query(Todos).filter(Todos.id==todo_id).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404,detail="Todo not found")




@router.post("/todo",status_code=status.HTTP_201_CREATED)
async def create_todo(db:db_dependency,todo_request:TodoRequest):
    todo_model=Todos(**todo_request.model_dump())

    db.add(todo_model)
    db.commit()



# In FastAPI, parameter order matters because Python requires non-default parameters before or above default parameters.
@router.put("/todo/{todo_id}",status_code=status.HTTP_204_NO_CONTENT)
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


@router.delete("/todo/{todo_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(db:db_dependency,todo_id:int=Path(gt=0)):
    todo_model= db.query(Todos).filter(Todos.id==todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.query(Todos).filter(Todos.id==todo_id).delete()





    





    