"""
EJEMPLO: Cómo usar la función de importación bulk de 100 registros

Este script muestra cómo importar películas de OMDb usando el nuevo
endpoint POST /movies/import
"""

import requests
import json
from datetime import datetime

BASE_URL = "http://localhost:8000"

def bulk_import_movies(query: str, count: int = 100) -> dict:
    """
    Importar películas de OMDb en bulk
    
    Args:
        query: Término de búsqueda (ej: "marvel", "batman", "star wars")
        count: Cantidad de películas a importar (máx 100)
    
    Returns:
        dict con los resultados de la importación
    """
    endpoint = f"{BASE_URL}/movies/import"
    params = {
        "query": query,
        "count": min(count, 100)  # Asegura que no exceda 100
    }
    
    try:
        print(f"📡 Enviando solicitud de importación...")
        print(f"   Query: {query}")
        print(f"   Count: {params['count']}")
        
        response = requests.post(endpoint, params=params)
        response.raise_for_status()  # Lanza excepción si hay error HTTP
        
        result = response.json()
        return result
        
    except requests.exceptions.ConnectionError:
        return {
            "error": "No se puede conectar al servidor. ¿Está corriendo en http://localhost:8000?"
        }
    except Exception as e:
        return {"error": str(e)}


def get_all_movies() -> dict:
    """Obtener todas las películas"""
    try:
        response = requests.get(f"{BASE_URL}/movies/all")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}


def print_result(result: dict, title: str = ""):
    """Imprimir resultado de forma bonita"""
    print("\n" + "=" * 60)
    if title:
        print(f"📊 {title}")
    print("=" * 60)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    print("=" * 60 + "\n")


# ============================================================================
# EJEMPLOS DE USO
# ============================================================================

if __name__ == "__main__":
    print("🎬 EJEMPLO: Importación Bulk de Películas desde OMDb\n")
    
    # EJEMPLO 1: Importar 100 películas de Marvel
    print("📍 EJEMPLO 1: Importar 100 películas de Marvel")
    result1 = bulk_import_movies(query="marvel", count=100)
    print_result(result1, "Resultado Importación - Marvel")
    
    # EJEMPLO 2: Importar 50 películas de Batman
    print("📍 EJEMPLO 2: Importar 50 películas de Batman")
    result2 = bulk_import_movies(query="batman", count=50)
    print_result(result2, "Resultado Importación - Batman")
    
    # EJEMPLO 3: Importar 30 películas de Star Wars
    print("📍 EJEMPLO 3: Importar 30 películas de Star Wars")
    result3 = bulk_import_movies(query="star wars", count=30)
    print_result(result3, "Resultado Importación - Star Wars")
    
    # EJEMPLO 4: Obtener todas las películas
    print("📍 EJEMPLO 4: Obtener todas las películas guardadas")
    all_movies = get_all_movies()
    if "data" in all_movies:
        total = len(all_movies.get("data", []))
        print(f"✅ Total de películas en BD: {total}")
        print(f"   Status: {all_movies.get('status')}")
        print(f"   Message: {all_movies.get('message')}")
        
        # Mostrar primeras 3 películas
        if all_movies.get("data"):
            print(f"\n   Primeras 3 películas:")
            for i, movie in enumerate(all_movies.get("data", [])[:3], 1):
                print(f"      {i}. {movie.get('title')} ({movie.get('year')})")
    else:
        print_result(all_movies, "Error al obtener películas")


# ============================================================================
# SCRIPTS INDIVIDUALES QUE PUEDES USAR
# ============================================================================

# 📌 Script 1: Importar 100 películas de Marvel
print("\n" + "="*60)
print("COPY-PASTE: Script para importar 100 películas de Marvel")
print("="*60)
print("""
import requests

response = requests.post(
    "http://localhost:8000/movies/import",
    params={"query": "marvel", "count": 100}
)

print(response.json())
""")

# 📌 Script 2: Importar desde terminal con curl
print("\n" + "="*60)
print("COPY-PASTE: Comando curl para importar movies")
print("="*60)
print("""
# Importar 100 películas de Marvel
curl -X POST "http://localhost:8000/movies/import?query=marvel&count=100"

# Importar 50 películas de Batman
curl -X POST "http://localhost:8000/movies/import?query=batman&count=50"

# Importar 75 películas de Star Wars
curl -X POST "http://localhost:8000/movies/import?query=star%20wars&count=75"

# Obtener todas las películas
curl -X GET "http://localhost:8000/movies/all"
""")
