from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean



Base = declarative_base()

class Todos(Base):
    __tablename__= 'todos_n'
    id          = Column(Integer,primary_key=True,index=True)
    title       = Column(String)
    description = Column(String)
    priority    = Column(Integer)
    complete    = Column(Boolean,default=False)

