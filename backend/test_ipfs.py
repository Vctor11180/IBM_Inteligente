"""
Script para probar la conexión y subida a IPFS usando Pinata
"""

import os
import sys
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

from services.ipfs_service import ipfs_service


def test_conexion():
    """Prueba la conexión con Pinata"""
    print("=" * 60)
    print("🧪 Test de Conexión con Pinata IPFS")
    print("=" * 60)
    
    jwt = os.getenv('PINATA_JWT')
    if not jwt:
        print("❌ Error: PINATA_JWT no configurado en .env")
        return False
    
    print(f"✅ JWT encontrado: {jwt[:20]}...")
    
    # Verificar conexión
    print("\n🔍 Verificando conexión con Pinata...")
    if ipfs_service.verificar_conexion():
        print("✅ Conexión exitosa con Pinata")
        return True
    else:
        print("❌ Error: No se pudo conectar con Pinata")
        print("   Verifica que tu JWT sea correcto")
        return False


def test_subida_imagen():
    """Prueba subir una imagen de ejemplo a IPFS"""
    print("\n" + "=" * 60)
    print("🧪 Test de Subida de Imagen a IPFS")
    print("=" * 60)
    
    # Buscar una imagen de prueba en la carpeta de validación
    import io
    
    # Intentar con una imagen de validación
    imagen_paths = [
        'validacion/Porcioncorrecta/v1.jpg',
        'validacion/Porcionexceso/va.jpg',
        'entrenamiento/Porcion_correcta/1.jpg'
    ]
    
    imagen_path = None
    for path in imagen_paths:
        if os.path.exists(path):
            imagen_path = path
            break
    
    if not imagen_path:
        print("⚠️ No se encontró imagen de prueba")
        print("   Creando imagen de prueba...")
        # Crear una imagen simple de prueba
        from PIL import Image
        img = Image.new('RGB', (100, 100), color='red')
        img_bytes = io.BytesIO()
        img.save(img_bytes, format='PNG')
        img_bytes.seek(0)
        archivo = img_bytes
        nombre = 'test.png'
    else:
        print(f"📸 Usando imagen de prueba: {imagen_path}")
        archivo = open(imagen_path, 'rb')
        nombre = os.path.basename(imagen_path)
    
    try:
        # Subir imagen
        print("\n⬆️ Subiendo imagen a IPFS...")
        resultado = ipfs_service.subir_archivo(archivo, nombre)
        
        if resultado:
            print("\n✅ ¡Imagen subida exitosamente!")
            print(f"   CID: {resultado['cid']}")
            print(f"   URL: {resultado['url']}")
            print(f"   Tamaño: {resultado.get('tamanio', 'N/A')} bytes")
            print(f"\n🔗 Puedes ver la imagen en: {resultado['url']}")
            return True
        else:
            print("\n❌ Error: No se pudo subir la imagen")
            return False
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        if isinstance(archivo, io.BytesIO):
            archivo.close()


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("🚀 Iniciando Tests de IPFS")
    print("=" * 60)
    
    # Test 1: Conexión
    conexion_ok = test_conexion()
    
    if conexion_ok:
        # Test 2: Subida
        subida_ok = test_subida_imagen()
        
        if subida_ok:
            print("\n" + "=" * 60)
            print("✅ Todos los tests pasaron exitosamente")
            print("=" * 60)
        else:
            print("\n" + "=" * 60)
            print("⚠️ Test de conexión OK, pero falló la subida")
            print("=" * 60)
    else:
        print("\n" + "=" * 60)
        print("❌ Revisa tu configuración de Pinata")
        print("=" * 60)

