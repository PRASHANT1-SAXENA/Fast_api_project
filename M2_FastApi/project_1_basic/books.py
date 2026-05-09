from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def first_api():            # async is option for fastapi python now directly handle this
    return {"message": "welcome to api building"}

@app.get("/api-endpoint")
async def first_api():            # async is option for fastapi python now directly handle this
    return {"message": "My name is prashant saxena"}

