"""
Script para verificar qué está instalado y dónde
"""

import sys
import os

print("=" * 60)
print("VERIFICACIÓN DE INSTALACIÓN")
print("=" * 60)

print(f"\n📍 Python ejecutable: {sys.executable}")
print(f"📍 Usando .venv: {'.venv' in sys.executable}")

print("\n📦 Verificando dependencias...\n")

dependencias = [
    'flask',
    'flask_cors',
    'tensorflow',
    'numpy',
    'cv2',
    'PIL'
]

for dep in dependencias:
    try:
        if dep == 'flask_cors':
            module = __import__('flask_cors')
        elif dep == 'cv2':
            module = __import__('cv2')
        elif dep == 'PIL':
            module = __import__('PIL')
        else:
            module = __import__(dep)
        
        # Obtener versión si existe
        version = getattr(module, '__version__', 'instalado')
        ubicacion = os.path.dirname(module.__file__)
        
        print(f"✅ {dep:15} - Versión: {version}")
        print(f"   Ubicación: {ubicacion}")
    except ImportError:
        print(f"❌ {dep:15} - NO INSTALADO")
    print()

print("=" * 60)
print("\n💡 Si alguna dependencia muestra ❌, instálala con:")
print("   pip install <nombre_paquete>")
print("\n💡 Si estás en .venv y no se instala ahí:")
print("   python -m pip install <nombre_paquete>")
print("=" * 60)

