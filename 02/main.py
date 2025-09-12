from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models, schemas, crud
from db import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="District Admin User System")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Welcome to the District Administration User System"}

@app.post("/users/", response_model=schemas.UserRead)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_nid(db, user.nid)
    if db_user:
        raise HTTPException(status_code=400, detail="User with this NID already exists")
    return crud.create_user(db, user)

@app.get("/users/", response_model=list[schemas.UserRead])
def read_users(db: Session = Depends(get_db)):
    return crud.get_all_users(db)

@app.get("/users/{nid}", response_model=schemas.UserRead)
def read_user(nid: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_nid(db, nid)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.put("/users/{nid}", response_model=schemas.UserRead)
def update_user(nid: int, updated_user: schemas.UserCreate, db: Session = Depends(get_db)):
    user = crud.update_user(db, nid, updated_user)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.delete("/users/{nid}", response_model=schemas.UserRead)
def delete_user(nid: int, db: Session = Depends(get_db)):
    user = crud.delete_user(db, nid)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
