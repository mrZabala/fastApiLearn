# ⚾ MLB Stats API - FastAPI Project

## 📌 Overview

This project is a REST API built with **FastAPI** that provides **Major League Baseball (MLB) statistics**, including:

* 📊 Historical stats
* ⏱️ Time-based queries
* 🔴 Real-time data (planned)
* 📈 Player and team analytics

The goal of this project is to simulate a **real-world backend system** while progressively evolving the architecture into a **production-ready structure**.

---

## 🚀 Current Features

* Basic FastAPI setup
* Movie-based practice endpoints (temporary)
* Routing structure separation
* API endpoint testing and validation

---

## 🧠 Future Improvements

This project will evolve into a **4-layer architecture**, following best practices used in real-world backend systems.

### 🏗️ Planned Architecture

```
Models → Repository → Services → Controllers → Views
```

### 🔹 Layers Explanation

* **Models**

  * Define data structure and domain entities
  * Represent MLB data (players, teams, games, stats)

* **Repository**

  * Handle communication with the database
  * Responsible for CRUD operations

* **Services**

  * Business logic layer
  * Data processing, filtering, transformations

* **Controllers**

  * API endpoints
  * Handle requests and responses

* **Views**

  * Response formatting (JSON responses, schemas)

---

## ⚙️ Tech Stack

* **Python**
* **FastAPI**
* **Uvicorn**
* (Planned)

  * PostgreSQL
  * SQLAlchemy / ORM
  * WebSockets (for real-time data)

---

## 📡 External APIs

This project will integrate MLB data from public APIs such as:

👉 https://github.com/topics/mlb-stats-api

---

## 🔴 Future Features

* 📊 Player statistics (batting, pitching, etc.)
* 🏟️ Team performance tracking
* 📅 Game schedules and results
* 🔴 Real-time updates (if supported by API)
* 📈 Advanced filtering (by season, team, player)
* 🔐 Authentication & authorization
* ⚡ Caching for performance optimization

---

## 🧪 Learning Goals

This project is also part of a personal learning path:

```
FastAPI → Django
```

Focus areas:

* API design
* Clean architecture
* Separation of concerns
* Backend scalability

---

## 📂 Project Structure (Planned)

```
app/
├── controllers/
├── services/
├── repositories/
├── models/
├── schemas/
├── core/
└── main.py
```

---

## 🏁 Status

🚧 In progress — actively evolving from a simple structure to a scalable backend system.

---

## 💡 Notes

* Initial implementation may use in-memory data
* Database integration will be added progressively
* Architecture will be refactored as the project grows

---

## 🤝 Contributing

This is currently a personal learning project, but suggestions and improvements are always welcome.

---

## 📜 License

This project is for educational purposes.
