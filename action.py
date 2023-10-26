import base64
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import mysql.connector
from fastapi import FastAPI, Form
from pydantic import BaseModel


host = "localhost"
user = "root"
password = ""
database = "sql_web"

app=FastAPI()

# Mount the "static" directory as a static folder to serve files
app.mount("/static", StaticFiles(directory="static"))


try:
    conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
    )
    cursor=conn.cursor()
except Exception as e:
    print(f"Lỗi: {e}")

class userCreate(BaseModel):
    firstname: str
    lastname: str
    username: str
    password: str
    email: str | None = None

@app.post("/registered")
async def add_user(firstname: str = Form(...), 
                    lastname: str = Form(...),
                    username: str = Form(...),
                    password: str = Form(...),
                    email: str = Form(None)):
    password=password.encode("utf-8")
    encoded_password=base64.b64encode(password).decode("utf-8")
    # Execute the query
    cursor.execute(f"INSERT INTO users (firstname, lastname, username, password, email) VALUES ('{firstname}', '{lastname}', '{username}', '{encoded_password}' , '{email}')")

    # Commit the changes to the database
    conn.commit()
    return 

@app.get("/main")
async def read_root():
    return FileResponse("static/landing-page.html")

@app.get("/login")
async def login():
    return FileResponse("static/login-page.html")

@app.get("/register")
async def register():
    return FileResponse("static/register-page.html")