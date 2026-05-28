from sqlalchemy import create_engine
from sqlalchemy import orm, sessionmaker, declarative_base

db = create_engine('sqlite:///banco.db')


