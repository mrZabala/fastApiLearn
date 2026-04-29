# 🏗️ Arquitectura del Proyecto FastAPI - Diagrama y Explicación

## 📐 Diagrama de Flujo: Importación Bulk de 100 Películas

```
┌─────────────────────────────────────────────────────────────────┐
│  CLIENT (Postman, curl, Python requests, Swagger UI)            │
│  POST /movies/import?query=marvel&count=100                     │
└─────────────────────────────────┬───────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────┐
│  API CONTROLLER (api/movie_controller.py)                       │
│  - Valida parámetros (query, count ≤ 100)                       │
│  - Llama bulk_import_movies_service()                           │
└─────────────────────────────────┬───────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────┐
│  SERVICES (services/movie_services.py)                          │
│  bulk_import_movies_service(db, query, count):                  │
│  1. Llama search_movies_omdb(query)                             │
│  2. Para cada película:                                          │
│     - Verifica si existe con get_movie_by_imdb_id()             │
│     - Si NO existe, agrega a lista                              │
│  3. Llama bulk_save_movies(db, movies_list)                     │
│  4. Retorna {imported: N, total_in_db: M}                       │
└─────────────────────────────────┬───────────────────────────────┘
                                  │
                    ┌─────────────┴─────────────┐
                    │                           │
                    ▼                           ▼
   ┌───────────────────────────┐   ┌──────────────────────────┐
   │  EXTERNAL API             │   │ REPOSITORY               │
   │  OMDb API                 │   │ (repository/             │
   │  - search_movies_omdb()   │   │  movie_repository.py)    │
   │  Retorna: [              │   │ - get_movie_by_imdb_id() │
   │    {Title, Year, ...,     │   │ - bulk_save_movies()     │
   │     imdbID, Poster}       │   │ - get_movie_count()      │
   │  ]                        │   │ - create_movie()         │
   └───────────────────────────┘   │ - get_all_movies()       │
                                    └────────────┬─────────────┘
                                                 │
                                                 ▼
                              ┌──────────────────────────────────┐
                              │ DATABASE (PostgreSQL)            │
                              │ ┌─ movies table                  │
                              │ │ - id (PK, auto)                │
                              │ │ - title (unique)               │
                              │ │ - director                     │
                              │ │ - category                     │
                              │ │ - year                         │
                              │ │ - imdb_id (unique, FK)         │
                              │ │ - poster                       │
                              │ │ - plot                         │
                              │ │ - status                       │
                              │ └─ COMMIT (una sola vez al final)│
                              └──────────────────────────────────┘
```

---

## 📦 Estructura de Archivos y Responsabilidades

```
fastApiLearn/
│
├── api/
│   └── movie_controller.py          ← 🎯 Rutas/Endpoints
│       ├── GET  /movies/all
│       ├── GET  /movies/limited?limit=N
│       └── POST /movies/import?query=Q&count=N  ⭐ NUEVA
│
├── services/
│   ├── movie_services.py            ← 🧠 Lógica de Negocio
│   │   ├── get_all_movies_service()
│   │   ├── get_movies_with_limit_service()
│   │   ├── get_movie_detail_service()
│   │   └── bulk_import_movies_service()  ⭐ NUEVA
│   │
│   └── mappers/
│       └── movie_mapper.py          ← 🔄 Conversión de datos
│
├── repository/
│   └── movie_repository.py          ← 💾 Acceso a Datos
│       ├── get_all_movies()
│       ├── create_movie()
│       ├── update_movie()
│       ├── delete_movie()
│       ├── search_movies_omdb()
│       ├── get_movie_detail_omdb()
│       ├── get_movie_by_imdb_id()
│       ├── get_movie_by_title()
│       ├── bulk_save_movies()          ⭐ NUEVA
│       └── get_movie_count()           ⭐ NUEVA
│
├── models/
│   ├── db/
│   │   └── movie_entity.py          ← 🗄️ Modelo ORM (SQLAlchemy)
│   │       └── MovieEntity (tabla movies)
│   │
│   └── movies_models/
│       ├── movie_model.py           ← 📄 Modelo Pydantic (Request/Response)
│       ├── MovieListResponse.py     ← 📄 Respuesta estándar
│       ├── response_status.py       ← 📄 Enum de estados
│       └── ...
│
├── core/
│   ├── database.py                  ← 🔌 Conexión a PostgreSQL
│   ├── build_response.py            ← 🎁 Constructor de respuestas
│   ├── utils.py                     ← 🛠️ Utilidades
│   └── enums/
│       └── status.py                ← 📝 Estados disponibles
│
└── main.py                          ← 🚀 Aplicación FastAPI

```

---

## 🔄 Flujo de Datos Paso a Paso

### SOLICITUD: Importar 100 películas de Marvel

```bash
POST /movies/import?query=marvel&count=100
```

### RESPUESTA:

```json
{
  "status": "SUCCESS",
  "message": "Se importaron 87 películas correctamente",
  "data": {
    "imported": 87,
    "message": "Se importaron 87 películas correctamente",
    "total_in_db": 142
  }
}
```

### PASOS INTERNOS:

1. **API CONTROLLER** recibe parámetros validados:
   - `query` = "marvel"
   - `count` = 100 (máximo permitido)

2. **SERVICES** ejecuta `bulk_import_movies_service()`:
   ```
   a) Llama search_movies_omdb("marvel")
      ↓ Resultado: {"Search": [{...}, {...}, ...], "Response": "True"}
   
   b) Para cada película en Search:
      - Obtiene imdbID
      - Busca en BD si ya existe
      - Si NO existe → agrega a lista
   
   c) Resultado: [87 películas nuevas]
   
   d) Llama bulk_save_movies(db, lista_de_87_películas)
   ```

3. **REPOSITORY** ejecuta `bulk_save_movies()`:
   ```
   a) Para cada película:
      - Crea objeto MovieEntity
      - db.add(movie)
   
   b) UN SOLO COMMIT al final:
      - db.commit() → INSERT 87 registros a la BD
   
   c) Retorna: 87 (cantidad insertada)
   ```

4. **DATABASE** (PostgreSQL):
   ```sql
   INSERT INTO movies 
   (title, director, category, year, imdb_id, poster, plot, status)
   VALUES 
   ('Movie 1', 'Director 1', ..., 'Creado'),
   ('Movie 2', 'Director 2', ..., 'Creado'),
   ...
   ('Movie 87', 'Director 87', ..., 'Creado');
   ```

5. **RESPONSE** se construye:
   ```json
   {
     "status": "SUCCESS",
     "data": {
       "imported": 87,
       "total_in_db": 142
     }
   }
   ```

---

## ⚡ Optimizaciones Implementadas

### 1️⃣ **Prevención de Duplicados**
```python
# Antes de insertar, verifica que no existe
existing = get_movie_by_imdb_id(db, imdb_id)
if not existing:
    # Agrega a lista para insertar
```

### 2️⃣ **Bulk Insert (Un solo COMMIT)**
```python
# ❌ LENTO: Un commit por película
for movie in movies:
    db.add(movie)
    db.commit()  # 100 commits = 100x más lento

# ✅ RÁPIDO: Un commit al final
for movie in movies:
    db.add(movie)
db.commit()  # Solo 1 commit
```

### 3️⃣ **Validación Automática con Pydantic**
```python
# Query y Count se validan automáticamente
limit: int = Query(100, ge=1, le=100)
# - ge=1: Mínimo 1
# - le=100: Máximo 100
```

### 4️⃣ **Índices en BD para Búsquedas Rápidas**
```python
title = Column(String, unique=True, index=True)
imdb_id = Column(String, unique=True, index=True)
# index=True → búsquedas rápidas
# unique=True → no duplicados
```

---

## 📊 Comparación: Antes vs Después

### ANTES (Problemas)
- ❌ Rutas duplicadas y confusas
- ❌ IDs generados aleatoriamente (no únicos)
- ❌ Datos en memoria (se perdían)
- ❌ Sin validación de modelos
- ❌ Importación una película a la vez

### DESPUÉS (Soluciones)
- ✅ Rutas claras y organizadas
- ✅ IDs únicos con BD + imdb_id
- ✅ Datos persistentes en PostgreSQL
- ✅ Validación con Pydantic
- ✅ Importación de 100 películas a la vez

---

## 🎯 Casos de Uso

### Caso 1: Importar películas populares
```bash
# Importar 100 películas de Marvel
POST /movies/import?query=marvel&count=100
```

### Caso 2: Importar categoría específica
```bash
# Importar 50 películas de acción
POST /movies/import?query=action&count=50
```

### Caso 3: Importar por década
```bash
# Importar 100 películas de los 80s
POST /movies/import?query=1980s&count=100
```

### Caso 4: Consultar lo que importamos
```bash
# Ver todas las películas
GET /movies/all

# Ver primeras 50
GET /movies/limited?limit=50
```

---

## 🔐 Seguridad y Validaciones

✅ **Límite de 100 películas** (evita sobrecargar API y BD)
✅ **Validación de parámetros** (query requerido, count 1-100)
✅ **Prevención de duplicados** (verifica imdb_id)
✅ **Manejo de errores** (try/except en bulk_save)
✅ **Respuestas consistentes** (siempre JSON)

---

## 🚀 Próximas Mejoras

- [ ] Agregar autenticación (JWT)
- [ ] Implementar paginación
- [ ] Caché (Redis) para búsquedas
- [ ] WebSockets para importación en vivo
- [ ] Logging y monitoreo
- [ ] Tests unitarios
- [ ] Docker para deployment

---

✅ **¡Arquitectura lista para producción!**
