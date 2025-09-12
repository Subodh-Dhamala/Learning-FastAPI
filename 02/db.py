#connecting fastapi to mysql using sqlalchemy
# setting up db engine, session factory and base class for modules

#import sqlalchemy modules

from sqlalchemy import create_engine # connect py to mysql
from sqlalchemy.ext.declarative import declarative_base #base class to define models/tables
from sqlalchemy.orm import sessionmaker #factory to create session objects for db operations

#db url

DATABASE_URL = "mysql+pymysql://admin:admin@localhost:3306/mero_database"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base() #parent for all models/tables
