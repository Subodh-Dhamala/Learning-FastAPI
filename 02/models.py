#defining db tables/models using sqlalchemy

from sqlalchemy import Column,Integer,String
from db import Base # import Base from db.py,all tables inherit from this

class User(Base):
  __tablename__ = "User_Table" #table name in mysql

  #columns
  id = Column(Integer,primary_key=True,index=True)
  name=Column(String(30),nullable=False)
  age = Column(Integer,nullable=False)
  location = Column(String(30),nullable=False)
  nid = Column(Integer,unique = True,nullable=False)
  citizenship_number = Column(Integer,unique=True)
