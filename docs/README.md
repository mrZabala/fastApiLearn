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

* `GET /movies/all` → Get all movies from database
* `GET /movies/limited?limit=50` → Get movies with limit (max 100)
* **✨ `POST /movies/import?query=marvel&count=100` → Bulk import up to 100 movies from OMDb API**

### ✍️ Data Management

* `POST /movies` → Create a new movie
* `PUT /movies/{id}` → Update a movie

---

## ✨ NEW FEATURE: Bulk Import 100 Records

**Import up to 100 movies from OMDb API in a single request:**

```bash
POST /movies/import?query=marvel&count=100
```

**Returns:**
```json
{
  "status": "SUCCESS",
  "message": "Se importaron 87 películas correctamente",
  "data": {
    "imported": 87,
    "total_in_db": 142
  }
}
```

See `BULK_IMPORT_GUIDE.md` for complete documentation.

---

## 🚨 Issues Fixed ✅

* ✅ Duplicate routes resolved (`/movies/all` and `/movies/limited` instead of `/movies/movies/all`)
* ✅ Added unique IDs (using database auto-increment + imdb_id)
* ✅ Added database schema with proper fields
* ✅ Fixed syntax errors in `movie_services.py`
* ✅ Fixed imports and circular dependencies
* ✅ Added Pydantic validation with proper models
* ✅ Separated concerns properly (Models → Repository → Services → Controllers)
* ✅ Added bulk import functionality (100 records at once)

---

## 🧱 Architecture (Implemented) ✅

Models → Repository → Services → Controllers → Views

* **Models**: Data structure (Pydantic / ORM) ✅
* **Repository**: Data access layer (DB or external APIs) ✅
* **Services**: Business logic ✅
* **Controllers**: Route handling ✅
* **Views**: Response formatting ✅

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
