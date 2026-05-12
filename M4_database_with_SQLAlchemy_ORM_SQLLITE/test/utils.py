from sqlalchemy import create_engine, text
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker
import a2Database_tables_Models as models
from a4Router_Authenticatoin_Authorization_main import app
from fastapi.testclient import TestClient
from a2Database_tables_Models import Todos
import pytest




SQLALCHEMY_DATABASE_URL = "sqlite:///./testdb.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL,
                       connect_args={'check_same_thread':False},
                       poolclass=StaticPool
                       ) 

models.Base.metadata.create_all(bind=engine)

TestingSessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)




def override_get_db():
    db=TestingSessionLocal()
    try:
        yield db

    finally:
        db.close()


def override_get_current_user():
    return {'username': 'prashant','id':1,'user_role':"admin"}


