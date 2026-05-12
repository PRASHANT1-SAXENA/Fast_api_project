from typing import Annotated
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette import status
from a2Database_tables_Models import Users
from a1Database_Connection__with_ORM import SessionLocal
from fastapi import FastAPI , HTTPException, Depends,Path, APIRouter
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from datetime import datetime, timedelta, timezone

"""IMP:- to make it hashed use this in one cmd:- "pip install passlib==1.7.4 bcrypt==4.0.1"
because some versions of Passlib / FastAPI auth tutorials have compatibility 
issues with newer bcrypt releases.
"""
from passlib.context import CryptContext # read above note before installing

"""Imp:- to make jwe we need to install >pip install "python-jose[cryptography]". """

from jose import jwt , JWTError


"""make Secret_key by own with some random app or from python  or give any name it does mater 
but if it is little unique and complex that it is better and just copy paste here.
Secret key should usually stay constant for your application environment, not change every
request or every startup and save in .env file like SECRET_KEY = "your-long-random-secure-key".
If secret changes frequently:
Old tokens break after Users get logged out Token verification fails """

SECRET_KEY = '197b2c37c391bed93fe80344fe73b806947a65e36206e05a1a23c2fa12702fe3'  
ALGORITHM = 'HS256'


"""so if use prefix. All api take /auth befor it api name like /auth/auth_all so if api is auth_all in 
that case it seem like redundancy so either remove prifix or remove auth_all from api name but tags are important to segregate in swagger platform"""

router = APIRouter(
    # prefix='/auth',   
    tags=['auth']
)



bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')  # auth/token is the api which i made below



class CreateUserRequest(BaseModel):  # note: we are not takind id just it is primary key in database made by itself
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    role: str
    phone_number:str


class Token(BaseModel):
    access_token: str
    token_type: str
    




@router.get("/auth/")
async def status_user():
    return {"user":"authenticate"}


def authenticate_user(username: str, password: str, db):
    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    return user



def create_access_token(username: str, user_id: int, role: str, expires_delta: timedelta):
    encode = {'sub': username, 'id': user_id, 'role': role}
    expires = datetime.now(timezone.utc) + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)





def get_db():
    db=SessionLocal()
    try:
        yield db

    finally:
        db.close()



db_dependency=Annotated[Session,Depends(get_db)]


async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):  # not an api but it is async uses where we want to use
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        user_id: int = payload.get('id')
        user_role: str = payload.get('role')
        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail='Could not validate user.')
        return {'username': username, 'id': user_id, 'user_role': user_role}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Could not validate user.')


@router.post("/auth_c",status_code=status.HTTP_201_CREATED)
async def create_user(db:db_dependency,
                      create_user_request: CreateUserRequest): # we can not  use User(**create_user_request) as we have hashed password database model and here we take simple password  so went to in differn format 
     create_user_model = Users(
        email=create_user_request.email,
        username=create_user_request.username,
        first_name=create_user_request.first_name,
        last_name=create_user_request.last_name,
        role=create_user_request.role,
        hashed_password=bcrypt_context.hash(create_user_request.password),     # IMP:- to make it hashed use this in one cmd:- "pip install passlib==1.7.4 bcrypt==4.0.1" because some versions of Passlib / FastAPI auth tutorials have compatibility issues with newer bcrypt releases.
        is_active=True,
        phone_number=create_user_request.phone_number)
     db.add(create_user_model)
     db.commit()


@router.get("/auth_show_all")
async def registered_user(db: db_dependency,status_code=status.HTTP_200_OK):
    return db.query(Users).all()


# pip install python-multipart

@router.post("/auth/token",response_model=Token)
async def login_for_access_token(form_data:Annotated[OAuth2PasswordRequestForm,Depends()],
                                 db:db_dependency):
    user = authenticate_user(form_data.username,form_data.password,db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail='Could not validate user.')
    
    token = create_access_token(user.username, user.id, user.role, timedelta(minutes=20))

    return {'access_token': token, 'token_type': 'bearer'}











