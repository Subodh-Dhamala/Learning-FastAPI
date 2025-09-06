#You are the developer of a district administrative office. You want to save user data like nagrita, national identity number, age, name, and location, and you need to perform CRUD operations (Create, Read, Update, Delete). For the database, you can just use a simple data structure like a list.


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Root endpoint
@app.get('/')
def root():
  return {"message":"Welcome to the District Admininstration User System"}

class User(BaseModel):
  name:str
  age: int
  location: str
  nid: int
  citizenship_number: int

#Database as a list
user_db = []


#Creating user by POST
@app.post('/users')
def create_user(user:User): #using pyndatic for type validation from class 
  user_db.append(user)
  return {"message": f"{user.name} has registered!"}

#Reading the users list
@app.get('/users')
def read_all_users():
  return user_db


#Reading nid
@app.get('/users/{nid}')
def read_nid(nid:int):
  for user in user_db:
    if user.nid == nid:
      return user
    
  return{"message": "User not found!"}

#PUT request to update User- PUT means updating
@app.put('/users/{nid}')
def update(nid:int,updated_user:User):
  #enumerate()gives both the index and the item while looping
  for i, user in enumerate(user_db):
    if user.nid == nid:
      user_db[i]= updated_user
      return {"message": f"User {updated_user.name} has updated their details!"}
  return {"message":"User not found!"}

# DELETE request to delete user
@app.delete('/users/{nid}')
def delete(nid:int):
  for i,user in enumerate(user_db):
    if user.nid == nid:
      user_db.pop(i)
      return {"message": f"User {user.name} Deleted!"}
  return {"message":"User not found!"}
