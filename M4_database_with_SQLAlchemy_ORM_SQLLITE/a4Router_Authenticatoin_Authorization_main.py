from fastapi import FastAPI
import a2Database_tables_Models as models
from a1Database_Connection__with_ORM import engine
from a5_Router_Authentication_Authorization import auth ,todos,admin




app = FastAPI()


models.Base.metadata.create_all(bind=engine) 

@app.get("/healthy")
async def health_check():
    return{'status':"Healthy"}

app.include_router(todos.router)
app.include_router(auth.router)
app.include_router(admin.router)

    





    