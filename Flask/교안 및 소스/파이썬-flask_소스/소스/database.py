from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

engine  = create_engine('sqlite:///:memory:', echo=True)
session_factory = sessionmaker(autocommit = False, autoflush = False, bind = engine)
db_session = scoped_session(session_factory)

Base = declarative_base()

def init_db():
    import model
    Base.metadata.create_all(engine)
