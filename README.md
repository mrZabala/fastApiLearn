# 🚀 Weso API (FastAPI Learning Project)

A simple REST API built with FastAPI as part of my backend learning journey.
This project focuses on understanding API design, routing, and basic CRUD operations using Python.

---

## 📌 Project Status

🟡 In progress — currently learning and improving structure and best practices.

---

## 🧠 Purpose

This project was created to:

* Learn how to build APIs using FastAPI
* Understand routing, path params, and query params
* Practice CRUD operations
* Prepare for more advanced frameworks like Django and Odoo

---

## ⚙️ Tech Stack

* Python 3.13
* FastAPI
* Uvicorn

---

## 📂 Current Features

### 🏠 Home

* `GET /` → Basic endpoint returning a welcome message

### 🎬 Movies Endpoints

* `GET /movies` → Get all movies
* `GET /movies/id/{id}` → Get movie by ID
* `GET /movies/{query}` → Search by title or director
* `GET /movies/year/{year}` → Get movies by year
* `GET /movies?category=&year=` → Filter movies by category and year

### ✍️ Data Management

* `POST /movies` → Create a new movie
* `PUT /movies/{id}` → Update a movie

---

## 🚨 Known Issues / Limitations

* Duplicate routes may cause conflicts (`/movies/{query}` vs `/movies/{title}`)
* IDs are randomly generated once (not unique per record)
* Data is stored in memory (no database yet)
* No validation using Pydantic models
* No separation of concerns (everything in one file)

---

## 🧱 Planned Improvements (Next Steps)

This project will evolve into a more structured backend using a layered architecture:

### 🧩 Architecture (Planned)

Models → Repository → Services → Controllers → Views

* **Models**: Data structure (Pydantic / ORM)
* **Repository**: Data access layer (DB or external APIs)
* **Services**: Business logic
* **Controllers**: Route handling
* **Views**: Response formatting

---

## 🔮 Future Features

* ✅ Refactor into modular structure (folders)
* ✅ Add Pydantic models for validation
* ✅ Implement proper ID generation
* ✅ Add database (PostgreSQL)
* ✅ Error handling & status codes
* ✅ Authentication (JWT)
* ✅ Integration with external APIs (MLB Stats API)
* ✅ Real-time data (WebSockets)

---

## ⚾ Future Project Direction

This project will evolve into a **Baseball (MLB) Stats API**, where I will:

* Fetch real MLB data from external APIs
* Display player and team statistics
* Implement filters by season, team, and performance
* Add real-time game tracking (if possible)

---

## ▶️ How to Run

1. Create virtual environment:

```bash
python -m venv venv
```

2. Activate environment (Windows PowerShell):

```bash
venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install fastapi uvicorn --no-cache-dir
```

4. Run the server:

```bash
uvicorn main:app --reload
```

5. Open in browser:

```text
http://127.0.0.1:8000/docs
```

---

## 📚 What I'm Learning

* API design principles
* REST structure
* FastAPI fundamentals
* Backend architecture concepts
* Preparing for Django & Odoo development

---

## 💡 Notes

This is a learning project, so the focus is on improving step by step rather than perfection.

---

## 📌 Author

Eliezer Peña
Junior FullStack Developer (Learning Phase 🚀)

---
