"""
Script de testing para los endpoints del backend NutriLife

Este script prueba todos los endpoints para verificar que funcionen correctamente.
"""

import requests
import json
import os
import sys

# URL base de la API
BASE_URL = "http://localhost:5000/api"

def print_header(text):
    """Imprime un encabezado formateado"""
    print("\n" + "=" * 60)
    print(f"  {text}")
    print("=" * 60)

def print_result(success, message):
    """Imprime el resultado de una prueba"""
    status = "✅ PASS" if success else "❌ FAIL"
    print(f"{status}: {message}")

def test_health():
    """Prueba el endpoint /health"""
    print_header("TEST: GET /health")
    
    try:
        response = requests.get(f"{BASE_URL}/health", timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            print_result(True, f"Status code: {response.status_code}")
            print(f"   Response: {json.dumps(data, indent=2)}")
            
            # Verificar estructura de respuesta
            if "status" in data and "modelo_cargado" in data:
                print_result(True, "Estructura de respuesta correcta")
                if data["modelo_cargado"]:
                    print_result(True, "Modelo cargado correctamente")
                else:
                    print_result(False, "Modelo NO está cargado")
                return True
            else:
                print_result(False, "Estructura de respuesta incorrecta")
                return False
        else:
            print_result(False, f"Status code: {response.status_code}")
            print(f"   Response: {response.text}")
            return False
            
    except requests.exceptions.ConnectionError:
        print_result(False, "No se pudo conectar al servidor. ¿Está corriendo?")
        print("   Ejecuta: python backend/app.py")
        return False
    except Exception as e:
        print_result(False, f"Error: {str(e)}")
        return False

def test_calcular_imc():
    """Prueba el endpoint /calcular-imc"""
    print_header("TEST: POST /calcular-imc")
    
    test_cases = [
        {
            "name": "Usuario normal",
            "data": {
                "edad": 25,
                "peso": 70,
                "altura": 1.75,
                "actividad": "Moderada"
            }
        },
        {
            "name": "Usuario con sobrepeso",
            "data": {
                "edad": 35,
                "peso": 90,
                "altura": 1.70,
                "actividad": "Sedentario"
            }
        },
        {
            "name": "Usuario atlético",
            "data": {
                "edad": 28,
                "peso": 75,
                "altura": 1.80,
                "actividad": "Alta"
            }
        }
    ]
    
    all_passed = True
    
    for test_case in test_cases:
        print(f"\n  Caso: {test_case['name']}")
        try:
            response = requests.post(
                f"{BASE_URL}/calcular-imc",
                json=test_case["data"],
                headers={"Content-Type": "application/json"},
                timeout=5
            )
            
            if response.status_code == 200:
                data = response.json()
                print_result(True, f"Status code: {response.status_code}")
                
                # Verificar campos esenciales
                required_fields = ["imc", "categoria", "objetivo", "calorias"]
                missing_fields = [f for f in required_fields if f not in data]
                
                if not missing_fields:
                    print_result(True, "Todos los campos requeridos presentes")
                    print(f"   IMC: {data['imc']} - {data['categoria']}")
                    print(f"   Calorías: {data['calorias']} kcal")
                    print(f"   Objetivo: {data['objetivo']}")
                else:
                    print_result(False, f"Faltan campos: {missing_fields}")
                    all_passed = False
            else:
                print_result(False, f"Status code: {response.status_code}")
                print(f"   Response: {response.text}")
                all_passed = False
                
        except Exception as e:
            print_result(False, f"Error: {str(e)}")
            all_passed = False
    
    # Probar caso con datos faltantes (debe fallar)
    print(f"\n  Caso: Datos faltantes (debe fallar)")
    try:
        response = requests.post(
            f"{BASE_URL}/calcular-imc",
            json={"edad": 25},  # Faltan peso y altura
            headers={"Content-Type": "application/json"},
            timeout=5
        )
        
        if response.status_code == 400:
            print_result(True, "Correctamente rechazó datos incompletos (400)")
        else:
            print_result(False, f"Debería retornar 400, pero retornó {response.status_code}")
            all_passed = False
    except Exception as e:
        print_result(False, f"Error: {str(e)}")
        all_passed = False
    
    return all_passed

def test_analizar_imagen():
    """Prueba el endpoint /analizar-imagen"""
    print_header("TEST: POST /analizar-imagen")
    
    # Buscar una imagen de prueba en el proyecto
    imagen_paths = [
        "validacion/Porcioncorrecta/v1.jpg",
        "validacion/Porcionexceso/va.jpg",
        "entrenamiento/Porcion_correcta/1.jpg"
    ]
    
    imagen_path = None
    for path in imagen_paths:
        if os.path.exists(path):
            imagen_path = path
            break
    
    if not imagen_path:
        print_result(False, "No se encontró ninguna imagen de prueba")
        print("   Buscando en: validacion/, entrenamiento/")
        return False
    
    print(f"  Usando imagen: {imagen_path}")
    
    try:
        # Preparar datos
        with open(imagen_path, 'rb') as f:
            files = {'imagen': (os.path.basename(imagen_path), f, 'image/jpeg')}
            data = {
                'imc': 22.5,
                'categoria_imc': 'Normal',
                'calorias_objetivo': 2000,
                'objetivo': 'mantener peso'
            }
            
            response = requests.post(
                f"{BASE_URL}/analizar-imagen",
                files=files,
                data=data,
                timeout=30  # Más tiempo para procesar imagen
            )
            
        if response.status_code == 200:
            result = response.json()
            print_result(True, f"Status code: {response.status_code}")
            
            # Verificar estructura de respuesta
            if result.get("success") and "analisis" in result and "recomendacion" in result:
                print_result(True, "Estructura de respuesta correcta")
                
                analisis = result["analisis"]
                print(f"\n   📊 Análisis:")
                print(f"      Porción correcta: {analisis.get('porcion_correcta')}")
                print(f"      Confianza: {analisis.get('confianza', 0):.2%}")
                print(f"      Prob. Correcta: {analisis.get('probabilidad_correcta', 0):.2%}")
                print(f"      Prob. Exceso: {analisis.get('probabilidad_exceso', 0):.2%}")
                
                recomendacion = result["recomendacion"]
                print(f"\n   💡 Recomendación:")
                print(f"      Mensaje: {recomendacion.get('mensaje', 'N/A')}")
                print(f"      Calorías estimadas: {recomendacion.get('calorias_estimadas', 0)}")
                print(f"      Acción: {recomendacion.get('accion', 'N/A')}")
                
                return True
            else:
                print_result(False, "Estructura de respuesta incorrecta")
                print(f"   Response: {json.dumps(result, indent=2)}")
                return False
        else:
            print_result(False, f"Status code: {response.status_code}")
            print(f"   Response: {response.text}")
            return False
            
    except Exception as e:
        print_result(False, f"Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

def test_error_cases():
    """Prueba casos de error"""
    print_header("TEST: Casos de Error")
    
    all_passed = True
    
    # Probar sin imagen
    print("\n  Caso: Enviar sin imagen (debe fallar)")
    try:
        response = requests.post(
            f"{BASE_URL}/analizar-imagen",
            data={"imc": 22.5},
            timeout=5
        )
        
        if response.status_code == 400:
            print_result(True, "Correctamente rechazó petición sin imagen (400)")
        else:
            print_result(False, f"Debería retornar 400, pero retornó {response.status_code}")
            all_passed = False
    except Exception as e:
        print_result(False, f"Error: {str(e)}")
        all_passed = False
    
    return all_passed

def main():
    """Ejecuta todas las pruebas"""
    print("\n" + "=" * 60)
    print("  🧪 TESTING DE ENDPOINTS - NutriLife Backend")
    print("=" * 60)
    print(f"\n🌐 URL Base: {BASE_URL}")
    print("\n⚠️  Asegúrate de que el servidor esté corriendo:")
    print("   python backend/app.py")
    
    # Esperar 2 segundos para que el servidor esté listo
    import time
    print("\n⏳ Esperando 2 segundos para que el servidor esté listo...")
    time.sleep(2)
    print("✅ Comenzando pruebas...\n")
    
    results = {
        "health": False,
        "calcular_imc": False,
        "analizar_imagen": False,
        "error_cases": False
    }
    
    # Ejecutar pruebas
    results["health"] = test_health()
    results["calcular_imc"] = test_calcular_imc()
    results["analizar_imagen"] = test_analizar_imagen()
    results["error_cases"] = test_error_cases()
    
    # Resumen final
    print_header("RESUMEN DE PRUEBAS")
    
    total = len(results)
    passed = sum(results.values())
    
    for test_name, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"  {status}: {test_name}")
    
    print(f"\n  Total: {passed}/{total} pruebas pasadas")
    
    if passed == total:
        print("\n  🎉 ¡Todas las pruebas pasaron!")
        return 0
    else:
        print(f"\n  ⚠️  {total - passed} prueba(s) fallaron")
        return 1

if __name__ == "__main__":
    try:
        exit_code = main()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\n\n⚠️  Pruebas canceladas por el usuario")
        sys.exit(1)

