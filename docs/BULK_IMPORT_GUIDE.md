# 📚 GUÍA DE IMPORTACIÓN BULK (100 REGISTROS)

## ✨ Nueva Función Agregada: `POST /movies/import`

Esta nueva funcionalidad te permite **importar hasta 100 películas** de OMDb en una sola operación.

---

## 🚀 Cómo Usar

### 1️⃣ **Endpoint REST**

```
POST /movies/import?query=marvel&count=100
```

### 2️⃣ **Parámetros**

| Parámetro | Tipo | Rango | Default | Descripción |
|-----------|------|-------|---------|-------------|
| `query` | string | - | REQUERIDO | Término de búsqueda en OMDb (ej: "marvel", "batman", "star wars") |
| `count` | integer | 1-100 | 100 | Cantidad de películas a importar |

### 3️⃣ **Ejemplos de Uso**

```bash
# Importar 100 películas de Marvel
curl -X POST "http://localhost:8000/movies/import?query=marvel&count=100"

# Importar 50 películas de Batman
curl -X POST "http://localhost:8000/movies/import?query=batman&count=50"

# Importar 30 películas de Star Wars
curl -X POST "http://localhost:8000/movies/import?query=star%20wars&count=30"
```

### 4️⃣ **Respuesta Exitosa**

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

### 5️⃣ **Características Principales**

✅ **Evita Duplicados**: No importa películas que ya existen en BD
✅ **Bulk Insert**: Inserta múltiples registros eficientemente
✅ **Límite de 100**: Máximo 100 registros por operación
✅ **Validación**: Verifica campos e imdb_id
✅ **Reporte**: Retorna cantidad importada y total en BD

---

## 🔧 Campos Guardados por Película

```python
{
    "id": int,                    # Primary key (auto-generado)
    "title": str,                 # Nombre de la película
    "director": str,              # Director
    "category": str,              # Género (Type en OMDb)
    "year": int,                  # Año de lanzamiento
    "imdb_id": str,               # ID único de OMDb (PREVIENE DUPLICADOS)
    "poster": str,                # URL del póster
    "plot": str,                  # Sinopsis/descripción
    "status": str                 # Estado (Creado/Editado/Eliminado)
}
```

---

## 📊 Otros Endpoints Disponibles

### 📖 Obtener todas las películas
```bash
GET /movies/all
```

### 🔎 Obtener películas con límite
```bash
GET /movies/limited?limit=50
```

---

## 💾 Código Fuente (Cómo Funciona)

### Archivo: `services/movie_services.py`

```python
async def bulk_import_movies_service(db, query: str, count: int = 100):
    """Importar múltiples películas de OMDb en una sola operación"""
    if count > 100:
        count = 100
    
    # 1. Buscar películas en OMDb
    data = await search_movies_omdb(query)
    
    # 2. Filtrar películas que NO existen en BD
    movies_to_import = []
    for item in data.get("Search", [])[:count]:
        existing = get_movie_by_imdb_id(db, item.get("imdbID"))
        if not existing:
            movies_to_import.append({...})
    
    # 3. Guardar todas de una vez (bulk insert)
    saved_count = bulk_save_movies(db, movies_to_import)
    
    return {
        "imported": saved_count,
        "message": f"Se importaron {saved_count} películas correctamente",
        "total_in_db": get_movie_count(db)
    }
```

### Archivo: `repository/movie_repository.py`

```python
def bulk_save_movies(db: Session, movies_list: list):
    """Guardar múltiples películas a la vez"""
    count = 0
    for movie_data in movies_list:
        try:
            movie = MovieEntity(**movie_data)
            db.add(movie)
            count += 1
        except Exception:
            continue  # Continúa si hay error en una película
    
    db.commit()  # Solo un commit al final (más eficiente)
    return count
```

---

## 🐛 Posibles Respuestas

### ✅ Éxito
```json
{
  "status": "SUCCESS",
  "data": {
    "imported": 100,
    "message": "Se importaron 100 películas correctamente",
    "total_in_db": 150
  }
}
```

### ⚠️ Todas ya existen
```json
{
  "status": "EMPTY",
  "data": {
    "imported": 0,
    "message": "Todas las películas ya existen en la BD"
  }
}
```

### ❌ No encontradas
```json
{
  "status": "EMPTY",
  "data": {
    "imported": 0,
    "message": "No se encontraron películas"
  }
}
```

---

## ⚙️ Cómo Ejecutar el Servidor

```bash
# 1. Activar venv
venv\Scripts\activate

# 2. Instalar dependencias (si no las tienes)
pip install fastapi uvicorn sqlalchemy httpx

# 3. Asegúrate que PostgreSQL esté corriendo
# (Base de datos: movies_db, Usuario: postgres, Contraseña: 1234)

# 4. Ejecutar servidor
uvicorn main:app --reload

# 5. Acceder a Swagger UI
http://localhost:8000/docs
```

---

## 📝 Notas Importantes

- **OMDb API Key**: `8a90e22f` (Incluida en el proyecto)
- **Límite de Búsqueda**: OMDb retorna máximo 10 resultados por página
- **Prevención de Duplicados**: Usa `imdb_id` como clave única
- **Transacciones**: Usa un solo `commit()` para eficiencia
- **Base de Datos**: PostgreSQL (obligatoria para esta versión)

---

## 🎯 Ejemplo Práctico Completo

```python
# Usando el cliente de FastAPI/Requests
import requests

# Importar 100 películas de Marvel
response = requests.post(
    "http://localhost:8000/movies/import",
    params={
        "query": "marvel",
        "count": 100
    }
)

print(response.json())
# {
#   "status": "SUCCESS",
#   "data": {"imported": 87, ...}
# }

# Obtener todas las películas
response = requests.get("http://localhost:8000/movies/all")
print(f"Total de películas: {len(response.json()['data'])}")
```

---

✅ **¡Listo!** Tu proyecto ahora puede importar 100 registros de OMDb con un solo request.
