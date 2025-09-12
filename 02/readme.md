# FastAPI District Administration User System

## Project Overview

This project is a **FastAPI** application designed for a district administrative office.  
It supports **CRUD operations** (Create, Read, Update, Delete) for managing user data, including:

- **Name**  
- **Age**  
- **Location**  
- **National Identity Number (NID)**  
- **Citizenship Number**

The backend is powered by **MySQL** with **SQLAlchemy ORM**, and **FastAPI** serves the REST API.

---

## Setup Instructions

### 1️⃣ Create Project Folder
Create a dedicated folder for your project:

```bash
mkdir -p ~/Desktop/FastApi_Learning/02
2️⃣ Navigate to Project Root
Open your terminal and move to the project folder using Git Bash:
bashcd ~/Desktop/FastApi_Learning/02
3️⃣ Set Up Python Virtual Environment
Create an isolated Python environment:
bashpython -m venv venv
This will generate a venv/ folder in your project directory.
4️⃣ Activate Virtual Environment
Activate the virtual environment in Git Bash (Windows):
bashsource venv/Scripts/activate
You’ll see (venv) in your terminal prompt when activated.
5️⃣ Install Required Packages
With the virtual environment activated, install the necessary packages:
bashpip install fastapi uvicorn sqlalchemy pymysql pydantic
Installed Packages:

fastapi: Core framework for building APIs
uvicorn: ASGI server to run FastAPI
sqlalchemy: ORM for MySQL database interactions
pymysql: MySQL driver for SQLAlchemy
pydantic: Data validation and serialization

Verify the installation:
bashpip list
6️⃣ Create Project Files
Create the following files in the project folder:

db.py: Database connection setup
models.py: SQLAlchemy ORM table definitions (e.g., User)
schemas.py: Pydantic models for request/response validation
crud.py: CRUD operation functions
main.py: FastAPI app and API routes

Run this command to create the files:
bashtouch db.py models.py schemas.py crud.py main.py

Database Setup

Launch MySQL (via command line or MySQL Workbench).
Create a database for the project:

sqlCREATE DATABASE subodh;

Verify the database was created:

sqlSHOW DATABASES;
Make a note of the database name; you’ll need it in db.py for the connection.

File Descriptions

db.py
Manages the database connection using SQLAlchemy.
Includes engine, SessionLocal, and Base objects for database operations.
models.py
Defines SQLAlchemy ORM tables, such as the User table.
Each class maps to a database table.
schemas.py
Contains Pydantic models for validating API requests and responses.
Ensures consistent and correct data structures.
crud.py
Implements CRUD functions:

create_user: Adds a new user
get_all_users: Retrieves all users
get_user_by_nid: Fetches a single user by NID
update_user: Updates an existing user
delete_user: Deletes a user


main.py
Initializes the FastAPI app and defines API routes.
Connects CRUD functions to endpoints and uses dependency injection for database sessions.


Running the Application

Ensure the virtual environment is activated:

bashsource venv/Scripts/activate

Start the FastAPI server with auto-reload for development:

bashuvicorn main:app --reload

Access the interactive API documentation in your browser:

texthttp://127.0.0.1:8000/docs
You can test all API endpoints directly from the Swagger UI.

API Endpoints








































MethodEndpointDescriptionGET/Root endpoint, shows API statusPOST/users/Create a new userGET/users/Retrieve all usersGET/users/{nid}Retrieve a user by NIDPUT/users/{nid}Update a user by NIDDELETE/users/{nid}Delete a user by NID

Notes

Ensure the MySQL server is running before launching the API.
Use unique NID values for each user to avoid conflicts.
FastAPI’s Swagger UI at /docs provides an interactive interface to test endpoints.