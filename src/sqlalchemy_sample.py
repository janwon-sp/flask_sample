import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:////db/sample1.db", echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id   = Column(Integer(), primary_key=True)
    name = Column(String())
    age  = Column(Integer())