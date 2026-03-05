#==================================
#I built a RESTful user management API using FastAPI.
#The API supports creating users, retrieving users, and listing users.
#Input validation is handled using Pydantic models, and asynchronous endpoints improve request handling efficiency.
#I implemented middleware to log request processing time and background tasks to simulate sending welcome emails.
#A simple HTML and JavaScript frontend consumes the API using fetch calls, demonstrating frontend-backend integration.

from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
import time
import asyncio
from typing import List
from uuid import uuid4

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------
# In-memory database
# -----------------------
fake_db = {}

# -----------------------
# Pydantic Models
# -----------------------
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: int


class UserResponse(BaseModel):
    id: str
    name: str
    email: EmailStr
    age: int


# -----------------------
# Home endpoint
# -----------------------
@app.get("/")
def home():
    return {"message": "User API is running"}


# -----------------------
# Middleware
# -----------------------
@app.middleware("http")
async def log_requests(request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    print(f"Request processed in {process_time:.4f} seconds")
    return response


# -----------------------
# Background Task
# -----------------------
def send_welcome_email(email: str):
    print(f"Sending welcome email to {email}")


# -----------------------
# Create User
# -----------------------
@app.post("/users", response_model=UserResponse)
async def create_user(user: UserCreate, background_tasks: BackgroundTasks):

    await asyncio.sleep(1)  # simulate database delay

    user_id = str(uuid4())

    fake_db[user_id] = {
        "id": user_id,
        "name": user.name,
        "email": user.email,
        "age": user.age
    }

    background_tasks.add_task(send_welcome_email, user.email)

    return fake_db[user_id]


# -----------------------
# Get User
# -----------------------
@app.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: str):

    if user_id not in fake_db:
        raise HTTPException(status_code=404, detail="User not found")

    return fake_db[user_id]


# -----------------------
# List Users
# -----------------------
@app.get("/users", response_model=List[UserResponse])
async def list_users():
    return list(fake_db.values())