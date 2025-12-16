# 📚 Fase 2: Backend API para IA

## 📋 Objetivo

Crear una API REST con Flask que integre el modelo de clasificación entrenado en la Fase 1, permitiendo recibir imágenes desde el frontend, analizarlas y retornar recomendaciones nutricionales basadas en el IMC del usuario.

## 🎯 Checklist de la Fase 2

- [x] Crear estructura del backend Flask ✅
- [x] Configurar endpoint `/analizar-imagen` ✅
- [x] Integrar modelo entrenado (modelo_porciones.keras) ✅
- [x] Implementar preprocesamiento de imágenes en tiempo real ✅
- [x] Calcular calorías estimadas basadas en análisis ✅
- [x] Generar recomendaciones según IMC del usuario ✅
- [x] Configurar CORS para comunicación con frontend ✅
- [x] Agregar manejo de errores ✅
- [x] Crear endpoint `/calcular-imc` (compatible con frontend existente) ✅
- [x] Script de testing creado ✅ (`backend/test_endpoints.py`)
- [ ] Ejecutar testing de endpoints ⏳ (ver `TESTING_ENDPOINTS.md`)
- [x] Documentación de API ✅

## 🏗️ Arquitectura del Backend

```
Backend Flask API
├── app.py                    # Aplicación principal
├── routes/
│   └── api.py               # Endpoints de la API
├── services/
│   ├── modelo_service.py    # Servicio de predicción con IA
│   └── nutricion_service.py # Cálculos nutricionales
├── utils/
│   └── image_utils.py       # Utilidades para procesar imágenes
└── config.py                # Configuración
```

## 🔧 Stack Tecnológico

- **Framework**: Flask 2.2+
- **IA**: TensorFlow/Keras (modelo entrenado)
- **Procesamiento**: OpenCV, PIL/Pillow
- **API**: Flask-RESTful o endpoints simples
- **CORS**: flask-cors
- **Validación**: Validación de archivos de imagen

## 📡 Endpoints a Implementar

### 1. POST `/analizar-imagen`

**Descripción**: Analiza una imagen de comida y retorna si la porción es correcta o excesiva, junto con recomendaciones.

**Request**:
```json
{
  "imagen": "<base64_encoded_image> o <File>",
  "imc": 22.5,
  "categoria_imc": "Normal",
  "calorias_objetivo": 2000,
  "objetivo": "mantener peso"
}
```

**Response (Éxito)**:
```json
{
  "success": true,
  "analisis": {
    "porcion_correcta": true,
    "confianza": 0.85,
    "probabilidad_correcta": 0.85,
    "probabilidad_exceso": 0.15
  },
  "recomendacion": {
    "mensaje": "Porción adecuada para tu objetivo calórico",
    "calorias_estimadas": 450,
    "accion": "continuar"
  },
  "detalles": {
    "tipo_alimento": "Pollo con arroz y verduras",
    "gramos_estimados": 350
  }
}
```

**Response (Error)**:
```json
{
  "success": false,
  "error": "Descripción del error",
  "codigo": "ERROR_CODE"
}
```

### 2. GET `/health`

**Descripción**: Verifica que el servidor y el modelo estén funcionando.

**Response**:
```json
{
  "status": "ok",
  "modelo_cargado": true,
  "version": "1.0.0"
}
```

## 🔄 Flujo de Trabajo

```
1. Frontend envía imagen + datos del usuario (IMC, calorías objetivo)
   ↓
2. Backend recibe y valida la imagen
   ↓
3. Preprocesa la imagen (redimensionar, normalizar)
   ↓
4. Modelo IA hace predicción (porción correcta/exceso)
   ↓
5. Calcula calorías estimadas (basado en porción y tipo de comida)
   ↓
6. Compara con objetivo calórico del usuario
   ↓
7. Genera recomendaciones personalizadas
   ↓
8. Retorna JSON con resultados al frontend
```

## 💻 Estructura de Código

### app.py (Aplicación Principal)
```python
from flask import Flask
from flask_cors import CORS
from routes.api import api_bp

app = Flask(__name__)
CORS(app)  # Permitir peticiones del frontend

app.register_blueprint(api_bp)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

### services/modelo_service.py
- Cargar modelo entrenado
- Preprocesar imágenes
- Hacer predicciones
- Retornar probabilidades

### services/nutricion_service.py
- Calcular calorías estimadas
- Comparar con objetivo del usuario
- Generar recomendaciones según IMC

## 📝 Validaciones Necesarias

1. **Validar formato de imagen**: JPG, PNG, JPEG
2. **Validar tamaño**: Máximo 10MB
3. **Validar IMC**: Rango válido (10-50)
4. **Validar calorías objetivo**: Rango válido (800-5000)
5. **Manejo de errores**: Try-catch en todas las operaciones

## 🔐 Seguridad

- Validar tipos de archivo
- Limitar tamaño de archivos
- Sanitizar inputs
- Manejo seguro de errores (no exponer detalles internos)

## 🧪 Testing

- Probar endpoint con imágenes válidas
- Probar con imágenes inválidas
- Probar con diferentes valores de IMC
- Verificar respuestas JSON correctas
- Probar CORS funcionando

## 📊 Integración con Frontend

El frontend ya tiene una estructura básica. Necesitamos:

1. Modificar `index.html` para añadir componente de subida de imágenes
2. Conectar con el endpoint `/analizar-imagen`
3. Mostrar resultados del análisis
4. Integrar con la calculadora de IMC existente

## ⏭️ Siguiente Fase

Una vez completada la Fase 2, pasaremos a la **Fase 3: Integración Frontend-Backend** donde conectaremos completamente la interfaz con la API.

## 📂 Archivos a Crear

```
backend/
├── app.py
├── config.py
├── routes/
│   └── api.py
├── services/
│   ├── __init__.py
│   ├── modelo_service.py
│   └── nutricion_service.py
├── utils/
│   ├── __init__.py
│   └── image_utils.py
└── requirements.txt (o usar el general)
```

