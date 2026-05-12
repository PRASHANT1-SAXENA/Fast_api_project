from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



# for SQLITE:- sqlite:///./todos.db
SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'  # for development only as it is file base local db not like mysql or postgress which server based


# for PostgreSQL:-
POSTGRESQL_DATABASE_URL = "postgresql://user:password@localhost/dbname"

# MySQL:-
MYSQL_DATABASE_URL = "mysql+pymysql://user:password@localhost/dbname"

# Structure:-
# database_type://username:password@host:port/database_name
# example :- postgresql://admin:1234@localhost:5432/mydb

engine = create_engine(SQLALCHEMY_DATABASE_URL,connect_args={'check_same_thread':False})   # false make it different threat use handle different request

# Anology:- engine is a road connect  and session maker is vehicle which use for changing and all 
# Analogy:- thread is like a better whish has assigned for defferent tasks in case of check_same_thread is faslse




SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

"""In SQLAlchemy, autoflush automatically sends pending session changes
   to the database before running a query, without permanently saving them.

Important:
  --flush()--
  Sends changes to DB temporarily
  Not permanent

  --commit()--
  Permanently saves changes

"""

