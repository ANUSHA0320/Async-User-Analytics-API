# User Management REST API with FastAPI

## 📌 Project Overview

This project demonstrates a **RESTful API built with FastAPI** for managing users.  
It includes features such as:

- Creating users
- Listing all users
- Fetching individual users by ID
- Input validation using Pydantic
- Asynchronous endpoints
- Background tasks (simulate sending welcome emails)
- Middleware for logging request processing time
- Frontend interface (HTML + JavaScript) to interact with API

This project is **perfect for learning full-stack API development** and can be deployed using **Docker**.

---

## 🛠️ Tech Stack

- **Backend:** Python, FastAPI  
- **Frontend:** HTML, JavaScript  
- **Validation:** Pydantic  
- **Async / Background Tasks:** FastAPI async endpoints  

---

## ⚡ Features

1. **Create User**  
   - POST `/users`  
   - Validates input fields (`name`, `email`, `age`)  
   - Sends a background welcome email (simulated)  
   - Returns unique user ID  

2. **Get User**  
   - GET `/users/{user_id}`  
   - Fetch details of a specific user by ID  

3. **List Users**  
   - GET `/users`  
   - Returns all users in the system  

4. **Middleware**  
   - Logs request processing time  

5. **Frontend Interface**  
   - Simple HTML + JavaScript page (`index.html`)  
   - Create users, list all users, get user by ID  
   - Validates input on the client side  

---

## 🚀 How to Run

### 1️⃣ Clone or Download Project

```bash
git clone <your-repo-url>
cd <project-folder>
pip install fastapi uvicorn pydantic email-validator
uvicorn main:app --reload
open html file