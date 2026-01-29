# 📝 Notes API – FastAPI Practice Project

This project is a **practice backend API** built with **FastAPI**, **SQLAlchemy**, and **SQLite**.

The main goal of this project is **educational**:  
to understand how a **real backend application** is structured, why each layer exists, and how data flows from an HTTP request to the database and back.

This is **not** a monolithic `main.py` example — it follows a **clean, scalable architecture** similar to what is used in real-world projects.

---

## 🚀 Features

- Create notes
- List all notes
- Get a note by ID
- Update a note
- Delete a note
- Persistent storage using SQLite
- Automatic API documentation (`/docs`)

---

## 🧱 Project Structure

app/
api/ # HTTP layer (routes)
services/ # Business logic
schemas/ # Data validation & serialization
db/ # Database & ORM models
core/ # App configuration
main.py # Application entry point

Each folder represents a **responsibility**, not just files.

---

## 🧠 Architecture Philosophy

This project follows a **layered architecture**, where:

- Each layer has **one responsibility**
- Layers do **not leak concerns**
- Code is easier to test, maintain, and extend

The general flow is:

Client → Route → Service → Database → Service → Route → Client


---

# 🔍 Layer-by-Layer Explanation (VERY IMPORTANT)

Below is the **most important part** of this README.

---

## 1️⃣ `main.py` – Application Entry Point

**What it is**
- The starting point of the application
- Creates the FastAPI app instance
- Registers routers
- Initializes database tables

**What it should do**
- App configuration
- Router registration
- Startup logic

**What it should NOT do**
- Business logic
- Database queries
- Data validation

📌 Think of `main.py` as:
> “The place where everything is wired together.”

---

## 2️⃣ `api/` – Routes (HTTP Layer)

**What it is**
- Defines HTTP endpoints (`GET`, `POST`, `PUT`, `DELETE`)
- Handles request/response lifecycle
- Extracts parameters from the request

**Responsibilities**
- Read request data
- Call the appropriate service function
- Return a response

**What it should NOT do**
- Business logic
- Database queries
- Complex rules

📌 Routes should be **thin**.

Example responsibility:
```text
“When someone calls POST /notes, what function should run?”

---

## 3️⃣ services/ – Business Logic Layer

**What it is**

-The brain of the application
-Contains all the rules of how the system behaves

**Responsibilities

Create, update, delete entities**

-Apply business rules
-Decide what happens when data exists or not
-Raise errors when rules are broken

**What it should NOT do**

-Parse HTTP requests
-Know about routes
-Know about JSON responses

📌 Services answer:

**“What should happen?”**

-This layer allows:
-Reuse of logic
-Easy testing
-Database replacement later

