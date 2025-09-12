FastAPI District Administration User System
Project Overview

This project is a FastAPI application for a district administrative office.
It allows CRUD operations (Create, Read, Update, Delete) for user data including:

Name

Age

Location

National Identity Number (NID)

Citizenship Number

The backend uses MySQL with SQLAlchemy ORM, and FastAPI serves the REST API.

Setup Instructions
1️⃣ Create Project Folder

Create a folder for your project:

Desktop/FastApi_Learning/02

2️⃣ Open Terminal in Project Root

Navigate to the project folder in Git Bash:

cd ~/Desktop/FastApi_Learning/02

3️⃣ Create Python Virtual Environment
python -m venv venv


This creates an isolated Python environment inside venv/.

4️⃣ Activate Virtual Environment

On Git Bash (Windows):

source venv/Scripts/activate


Your terminal prompt should show (venv) when activated.

5️⃣ Install Required Packages

Inside the activated virtual environment, install:

pip install fastapi uvicorn sqlalchemy pymysql pydantic


Installed packages:

fastapi → framework for building APIs

uvicorn → ASGI server to run FastAPI

sqlalchemy → ORM to interact with MySQL

pymysql → MySQL driver for SQLAlchemy

pydantic → data validation

Check installation:

pip list

6️⃣ Create Project Files

Inside the project folder, create these files:

db.py       → database connection
models.py   → SQLAlchemy tables (User)
schemas.py  → Pydantic models for request/response
crud.py     → CRUD functions
main.py     → FastAPI app and routes


Use:

touch db.py models.py schemas.py crud.py main.py

