#!/usr/bin/env python3
"""Debug imports"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.getcwd())

print("🔍 Verificando imports...")
print("=" * 60)

try:
    print("1. Importando repository...")
    from repository import movie_repository
    print(f"   ✓ Funciones disponibles en movie_repository:")
    functions = [x for x in dir(movie_repository) if not x.startswith('_')]
    for func in functions:
        print(f"     - {func}")
    
    print("\n2. Verificando bulk_save_movies...")
    if hasattr(movie_repository, 'bulk_save_movies'):
        print("   ✓ bulk_save_movies existe")
    else:
        print("   ✗ bulk_save_movies NO existe")
    
    print("\n3. Importando services...")
    from services import movie_services
    print("   ✓ movie_services importado")
    
    print("\n4. Verificando funciones en services...")
    functions = [x for x in dir(movie_services) if not x.startswith('_') and callable(getattr(movie_services, x))]
    for func in functions:
        print(f"   - {func}")
    
    print("\n✅ ÉXITO: Todos los imports funcionan correctamente")
    
except Exception as e:
    print(f"\n❌ ERROR: {str(e)}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
