#!/usr/bin/env python3
"""Validar sintaxis de todos los archivos principales"""

import py_compile
import sys

files_to_check = [
    "api/movie_controller.py",
    "services/movie_services.py",
    "repository/movie_repository.py",
    "models/db/movie_entity.py",
    "models/movies_models/movie_model.py",
    "core/database.py",
    "main.py"
]

print("🔍 Validando sintaxis Python...")
print("=" * 60)

errors = []
for file in files_to_check:
    try:
        py_compile.compile(file, doraise=True)
        print(f"✅ {file}")
    except py_compile.PyCompileError as e:
        print(f"❌ {file}")
        errors.append((file, str(e)))

print("=" * 60)

if errors:
    print(f"\n⚠️  Se encontraron {len(errors)} errores:\n")
    for file, error in errors:
        print(f"Archivo: {file}")
        print(f"Error: {error}\n")
    sys.exit(1)
else:
    print("\n✅ ÉXITO: Todos los archivos tienen sintaxis correcta")
    sys.exit(0)
