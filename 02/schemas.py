#define pyndatic models for request and response validation to ensure incoming data has the correct structure and types

from pydantic import BaseModel

#base model for user creation

class UserCreate(BaseModel):
  name:str
  age:int
  location:str
  nid:int
  citizenship_number:int

class UserRead(BaseModel): #used to send respponses from the API
  id:int
  name:str
  age:int
  location:str
  nid:int
  citizenship_number:int

  class Config:
    orm_mode = True  #tells pydantic to accept  sqlalchemy orm objects