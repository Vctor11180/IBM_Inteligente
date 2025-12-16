"""
Endpoints de la API REST para NutriLife
"""

from flask import Blueprint, request, jsonify
import os
import sys

# Agregar el directorio padre al path para importar servicios
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.modelo_service import ModeloService
from services.nutricion_service import NutricionService

api_bp = Blueprint('api', __name__)

# Inicializar servicios
modelo_service = ModeloService()
nutricion_service = NutricionService()

@api_bp.route('/health', methods=['GET'])
def health():
    """Endpoint de salud - verifica que el servidor esté funcionando"""
    try:
        modelo_cargado = modelo_service.modelo_cargado()
        return jsonify({
            "status": "ok",
            "modelo_cargado": modelo_cargado,
            "version": "1.0.0"
        }), 200
    except Exception as e:
        return jsonify({
            "status": "error",
            "error": str(e)
        }), 500

@api_bp.route('/calcular-imc', methods=['POST'])
def calcular_imc():
    """
    Calcula el IMC y genera recomendaciones nutricionales
    
    Request body:
    {
        "edad": 25,
        "peso": 70,
        "altura": 1.75,
        "actividad": "Moderada"
    }
    """
    try:
        data = request.get_json()
        
        # Validar datos
        if not data:
            return jsonify({"error": "No se recibieron datos"}), 400
        
        edad = data.get('edad')
        peso = data.get('peso')
        altura = data.get('altura')
        actividad = data.get('actividad', 'Sedentario')
        
        if not all([edad, peso, altura]):
            return jsonify({"error": "Faltan datos requeridos (edad, peso, altura)"}), 400
        
        # Calcular IMC
        imc = peso / (altura ** 2)
        
        # Determinar categoría
        if imc < 18.5:
            categoria = "Bajo peso"
            objetivo = "Ganar peso de forma saludable"
        elif imc < 25:
            categoria = "Normal"
            objetivo = "Mantener peso saludable y equilibrio nutricional"
        elif imc < 30:
            categoria = "Sobrepeso"
            objetivo = "Perder peso de forma saludable"
        else:
            categoria = "Obesidad"
            objetivo = "Perder peso y mejorar la salud"
        
        # Calcular calorías diarias recomendadas (Fórmula de Harris-Benedict)
        # TMB (Tasa Metabólica Basal) - Hombre
        tmb = 88.362 + (13.397 * peso) + (4.799 * altura * 100) - (5.677 * edad)
        
        # Factor de actividad
        factores = {
            "Sedentario": 1.2,
            "Ligera": 1.375,
            "Moderada": 1.55,
            "Alta": 1.725
        }
        factor = factores.get(actividad, 1.2)
        
        calorias = int(tmb * factor)
        
        # Ajustar según objetivo
        if categoria == "Bajo peso":
            calorias += 300
        elif categoria in ["Sobrepeso", "Obesidad"]:
            calorias -= 500
        
        # Generar recomendaciones nutricionales
        recomendaciones = nutricion_service.generar_recomendaciones(imc, categoria, calorias)
        
        return jsonify({
            "imc": round(imc, 2),
            "categoria": categoria,
            "objetivo": objetivo,
            "calorias": calorias,
            **recomendaciones
        }), 200
        
    except Exception as e:
        return jsonify({
            "error": "Error al calcular IMC",
            "mensaje": str(e)
        }), 500

@api_bp.route('/analizar-imagen', methods=['POST'])
def analizar_imagen():
    """
    Analiza una imagen de comida usando el modelo de IA
    
    Request:
    - Form data con campo 'imagen' (archivo)
    - JSON con datos del usuario:
      {
        "imc": 22.5,
        "categoria_imc": "Normal",
        "calorias_objetivo": 2000,
        "objetivo": "mantener peso"
      }
    """
    try:
        # Verificar que se envió una imagen
        if 'imagen' not in request.files:
            return jsonify({
                "success": False,
                "error": "No se recibió ninguna imagen",
                "codigo": "NO_IMAGE"
            }), 400
        
        imagen_file = request.files['imagen']
        
        if imagen_file.filename == '':
            return jsonify({
                "success": False,
                "error": "Nombre de archivo vacío",
                "codigo": "EMPTY_FILENAME"
            }), 400
        
        # Obtener datos del usuario (pueden venir en form data o JSON)
        datos_usuario = {}
        if request.form:
            datos_usuario = {
                'imc': float(request.form.get('imc', 22.5)),
                'categoria_imc': request.form.get('categoria_imc', 'Normal'),
                'calorias_objetivo': int(request.form.get('calorias_objetivo', 2000)),
                'objetivo': request.form.get('objetivo', 'mantener peso')
            }
        else:
            # Intentar obtener de JSON
            datos_json = request.get_json(silent=True) or {}
            datos_usuario = {
                'imc': float(datos_json.get('imc', 22.5)),
                'categoria_imc': datos_json.get('categoria_imc', 'Normal'),
                'calorias_objetivo': int(datos_json.get('calorias_objetivo', 2000)),
                'objetivo': datos_json.get('objetivo', 'mantener peso')
            }
        
        # Analizar imagen con el modelo
        resultado_analisis = modelo_service.predecir_imagen(imagen_file)
        
        if not resultado_analisis:
            return jsonify({
                "success": False,
                "error": "Error al procesar la imagen",
                "codigo": "PROCESSING_ERROR"
            }), 500
        
        # Generar recomendaciones basadas en el análisis y datos del usuario
        recomendaciones = nutricion_service.generar_recomendacion_porcion(
            resultado_analisis,
            datos_usuario['imc'],
            datos_usuario['calorias_objetivo'],
            datos_usuario['objetivo']
        )
        
        return jsonify({
            "success": True,
            "analisis": {
                "porcion_correcta": resultado_analisis['porcion_correcta'],
                "confianza": round(resultado_analisis['confianza'], 4),
                "probabilidad_correcta": round(resultado_analisis['probabilidad_correcta'], 4),
                "probabilidad_exceso": round(resultado_analisis['probabilidad_exceso'], 4)
            },
            "recomendacion": recomendaciones,
            "detalles": {
                "tipo_alimento": "Comida analizada",
                "gramos_estimados": recomendaciones.get('gramos_estimados', 0)
            }
        }), 200
        
    except Exception as e:
        import traceback
        return jsonify({
            "success": False,
            "error": "Error al analizar imagen",
            "mensaje": str(e),
            "codigo": "SERVER_ERROR"
        }), 500

