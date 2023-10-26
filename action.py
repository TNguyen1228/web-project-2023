import base64
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import mysql.connector
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


host = "localhost"
user = "root"
password = ""
database = "sql_web"

app=FastAPI()

# Mount the "static" directory as a static folder to serve files
app.mount("/landing", StaticFiles(directory="web_deploy"), name="static")


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

@app.post("/register/")
async def add_user(user:userCreate):
    password=user.password.encode("utf-8")
    encoded=base64.b64encode(password)
    
    # Define the SQL query to insert user data
    insert_query = "INSERT INTO users (firstname, lastname, username, password, email) VALUES (%s, %s, %s, %s, %s)"

    # Execute the query
    cursor.execute(insert_query, (user.firstname, user.lastname, user.username, encoded, user.email))

    # Commit the changes to the database
    conn.commit()

@app.get("/")
async def read_root():
    return FileResponse("landing-page.html")
    