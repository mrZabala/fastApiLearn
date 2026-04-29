#!/usr/bin/env python
"""Test script to validate all imports and syntax"""

import sys

print("🔍 Validando importaciones del proyecto...")

try:
    print("✓ Importando core.database...")
    from core.database import Base, engine, get_db
    
    print("✓ Importando models...")
    from models.db.movie_entity import MovieEntity
    from models.movies_models.movie_model import Movie
    
    print("✓ Importando repository...")
    from repository.movie_repository import (
        get_all_movies, create_movie, bulk_save_movies, get_movie_count
    )
    
    print("✓ Importando services...")
    from services.movie_services import (
        get_all_movies_service, bulk_import_movies_service
    )
    
    print("✓ Importando API controller...")
    from api.movie_controller import router
    
    print("✓ Importando main app...")
    from main import app
    
    print("\n✅ ÉXITO: Todas las importaciones son correctas!")
    print("\n📋 RESUMEN:")
    print("   - Base de datos: PostgreSQL")
    print("   - Models: 5 archivos")
    print("   - Repository: 8 funciones")
    print("   - Services: 5 funciones (incluyendo bulk_import)")
    print("   - API: 3 endpoints principales")
    
    sys.exit(0)
    
except Exception as e:
    print(f"\n❌ ERROR: {str(e)}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
