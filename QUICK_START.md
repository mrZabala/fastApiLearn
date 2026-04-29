# 🚀 QUICK START - Comenzar en 5 minutos

## 1️⃣ Verificar Requisitos

```bash
# Verificar Python 3.11+
python --version

# Verificar PostgreSQL esté corriendo
# (Default: localhost:5432, usuario: postgres, contraseña: 1234)
```

## 2️⃣ Activar Entorno Virtual

```bash
venv\Scripts\activate
```

## 3️⃣ Instalar Dependencias

```bash
pip install fastapi uvicorn sqlalchemy httpx -q
```

## 4️⃣ Ejecutar Servidor

```bash
uvicorn main:app --reload
```

Deberías ver:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete
```

## 5️⃣ Probar Endpoints

### Opción A: Usando Swagger UI (Recomendado para principiantes)

1. Abre en navegador: http://localhost:8000/docs
2. Haz clic en "Try it out"
3. Completa parámetros
4. Haz clic en "Execute"

### Opción B: Usando curl

```bash
# Importar 100 películas de Marvel
curl -X POST "http://localhost:8000/movies/import?query=marvel&count=100"

# Importar 50 películas de Batman
curl -X POST "http://localhost:8000/movies/import?query=batman&count=50"

# Ver todas las películas
curl "http://localhost:8000/movies/all"

# Ver primeras 20 películas
curl "http://localhost:8000/movies/limited?limit=20"
```

### Opción C: Usando Python

```python
import requests

# Importar 100 películas de Star Wars
response = requests.post(
    "http://localhost:8000/movies/import",
    params={"query": "star wars", "count": 100}
)

print(response.json())
```

---

## 📊 Respuestas Esperadas

### ✅ Importación Exitosa

```json
{
  "status": "SUCCESS",
  "message": "",
  "data": {
    "imported": 87,
    "message": "Se importaron 87 películas correctamente",
    "total_in_db": 87
  }
}
```

### ✅ Obtener todas las películas

```json
{
  "status": "SUCCESS",
  "message": "Se encontraron 87 películas",
  "data": [
    {
      "id": 1,
      "title": "The Avengers",
      "director": "Joss Whedon",
      "category": "movie",
      "year": 2012,
      "status": "Creado",
      "imdb_id": "tt0848228",
      "poster": "https://...",
      "plot": "Earth's mightiest..."
    },
    ...
  ]
}
```

---

## 🔥 Casos de Uso Prácticos

### Caso 1: Importar películas de acción
```bash
curl -X POST "http://localhost:8000/movies/import?query=action&count=100"
```

### Caso 2: Importar comedias
```bash
curl -X POST "http://localhost:8000/movies/import?query=comedy&count=50"
```

### Caso 3: Importar películas clásicas
```bash
curl -X POST "http://localhost:8000/movies/import?query=classic%20films&count=100"
```

### Caso 4: Ver estadísticas
```bash
curl "http://localhost:8000/movies/all" | python -m json.tool | head -20
```

---

## 📚 Documentación Completa

Después de Quick Start, lee:

1. **`BULK_IMPORT_GUIDE.md`** - Guía detallada de importación
2. **`ARCHITECTURE.md`** - Cómo funciona internamente
3. **`CAMBIOS_REALIZADOS.md`** - Qué se arregló

---

## 🛠️ Troubleshooting

### ❌ Error: "Connection refused"
→ Asegúrate que PostgreSQL esté corriendo

### ❌ Error: "No movies found"
→ Normal, importa primero con POST /movies/import

### ❌ Error: "Database does not exist"
→ Crea la BD: `createdb -U postgres movies_db`

### ❌ Error: "Módulo no encontrado"
→ Reinstala dependencias:
```bash
pip install fastapi uvicorn sqlalchemy httpx --force-reinstall
```

---

## ✨ Próximos Pasos

1. ✅ **Importa datos** → POST /movies/import?query=marvel&count=100
2. ✅ **Consulta datos** → GET /movies/all
3. ✅ **Lee la arquitectura** → ARCHITECTURE.md
4. ✅ **Experimenta** → Prueba otros queries

---

## 🎯 Script Rápido (Copy-Paste)

Guardalo como `run_demo.py` y ejecuta con `python run_demo.py`:

```python
import requests
import json
import time

BASE_URL = "http://localhost:8000"

print("🎬 DEMO: Bulk Import de Películas")
print("=" * 60)

# Importar Marvel
print("\n1️⃣ Importando 100 películas de Marvel...")
r1 = requests.post(f"{BASE_URL}/movies/import", params={"query": "marvel", "count": 100})
print(f"   ✅ Importadas: {r1.json()['data']['imported']}")

# Importar Batman
print("2️⃣ Importando 50 películas de Batman...")
r2 = requests.post(f"{BASE_URL}/movies/import", params={"query": "batman", "count": 50})
print(f"   ✅ Importadas: {r2.json()['data']['imported']}")

# Ver todas
print("3️⃣ Obteniendo todas las películas...")
r3 = requests.get(f"{BASE_URL}/movies/all")
total = len(r3.json()['data'])
print(f"   ✅ Total en BD: {total}")

# Mostrar primeras 3
print("\n📋 Primeras 3 películas:")
for i, movie in enumerate(r3.json()['data'][:3], 1):
    print(f"   {i}. {movie['title']} ({movie['year']})")

print("\n" + "=" * 60)
print("✅ ¡Demo completado!")
```

Luego ejecuta:
```bash
python run_demo.py
```

---

## 🎉 ¡Listo!

Ya puedes:
- ✅ Importar 100 películas de una vez
- ✅ Consultar películas guardadas
- ✅ Evitar duplicados automáticamente
- ✅ Usar arquitectura profesional

**¡Diviértete aprendiendo! 🚀**
