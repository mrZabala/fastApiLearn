#!/usr/bin/env python3
"""Limpiar caché de Python"""

import os
import shutil
import sys

def clean_pycache(directory="."):
    """Eliminar todos los __pycache__ y *.pyc"""
    count = 0
    
    for root, dirs, files in os.walk(directory):
        # Eliminar __pycache__
        if "__pycache__" in dirs:
            pycache_path = os.path.join(root, "__pycache__")
            try:
                shutil.rmtree(pycache_path)
                print(f"✓ Eliminado: {pycache_path}")
                count += 1
            except Exception as e:
                print(f"✗ Error: {e}")
        
        # Eliminar .pyc
        for file in files:
            if file.endswith(".pyc"):
                pyc_path = os.path.join(root, file)
                try:
                    os.remove(pyc_path)
                    print(f"✓ Eliminado: {pyc_path}")
                    count += 1
                except Exception as e:
                    print(f"✗ Error: {e}")
    
    return count

if __name__ == "__main__":
    print("🧹 Limpiando caché de Python...")
    count = clean_pycache()
    print(f"\n✅ Se eliminaron {count} archivos de caché")
