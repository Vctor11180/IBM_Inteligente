# 🚀 Backend API - NutriLife AI + Web3

Backend Flask para la aplicación NutriLife que integra el modelo de IA entrenado y proporciona endpoints REST para análisis nutricional.

## 📁 Estructura

```
backend/
├── app.py                      # Aplicación principal Flask
├── routes/
│   └── api.py                 # Endpoints de la API
├── services/
│   ├── modelo_service.py      # Servicio de predicción con IA
│   └── nutricion_service.py   # Cálculos nutricionales y recomendaciones
├── utils/                      # Utilidades (por ahora vacío)
└── requirements.txt           # Dependencias del backend
```

## 🚀 Inicio Rápido

### 1. Instalar dependencias

Las dependencias principales (TensorFlow, NumPy, OpenCV) ya están instaladas en el proyecto.
Solo necesitas instalar Flask y Flask-CORS:

```bash
pip install flask flask-cors
```

O desde el directorio del proyecto:

```bash
pip install -r backend/requirements.txt
```

### 2. Ejecutar el servidor

Desde el directorio raíz del proyecto:

```bash
python backend/app.py
```

O desde el directorio backend:

```bash
cd backend
python app.py
```

El servidor iniciará en: `http://localhost:5000`

## 📡 Endpoints Disponibles

### GET `/api/health`

Verifica el estado del servidor y si el modelo está cargado.

**Ejemplo de respuesta**:
```json
{
  "status": "ok",
  "modelo_cargado": true,
  "version": "1.0.0"
}
```

---

### POST `/api/calcular-imc`

Calcula el IMC y genera recomendaciones nutricionales.

**Request Body** (JSON):
```json
{
  "edad": 25,
  "peso": 70,
  "altura": 1.75,
  "actividad": "Moderada"
}
```

**Response** (200 OK):
```json
{
  "imc": 22.86,
  "categoria": "Normal",
  "objetivo": "Mantener peso saludable y equilibrio nutricional",
  "calorias": 2200,
  "desayuno": {
    "descripcion": "Yogurt natural con frutas frescas y granola",
    "calorias": 550,
    "proteinas": 25
  },
  "almuerzo": { ... },
  "cena": { ... },
  "snacks": ["Frutas frescas variadas", ...],
  "tips": ["💧 Bebe al menos 2 litros de agua", ...]
}
```

---

### POST `/api/analizar-imagen`

Analiza una imagen de comida usando el modelo de IA.

**Request**: Form-data con:
- `imagen`: Archivo de imagen (JPG, PNG, JPEG)
- `imc`: (opcional) IMC del usuario (float)
- `categoria_imc`: (opcional) Categoría IMC (string)
- `calorias_objetivo`: (opcional) Calorías objetivo diarias (int)
- `objetivo`: (opcional) Objetivo ("mantener peso", "perder peso", "ganar peso")

**Response** (200 OK):
```json
{
  "success": true,
  "analisis": {
    "porcion_correcta": true,
    "confianza": 0.8542,
    "probabilidad_correcta": 0.8542,
    "probabilidad_exceso": 0.1458
  },
  "recomendacion": {
    "mensaje": "Porción adecuada para tu objetivo calórico...",
    "calorias_estimadas": 450,
    "gramos_estimados": 350,
    "accion": "continuar",
    "calorias_diarias_objetivo": 2000,
    "calorias_restantes_aproximadas": 1550
  },
  "detalles": {
    "tipo_alimento": "Comida analizada",
    "gramos_estimados": 350
  }
}
```

**Response Error** (400/500):
```json
{
  "success": false,
  "error": "Descripción del error",
  "codigo": "ERROR_CODE"
}
```

## 🧪 Probar los Endpoints

### Con curl

**Health check**:
```bash
curl http://localhost:5000/api/health
```

**Calcular IMC**:
```bash
curl -X POST http://localhost:5000/api/calcular-imc \
  -H "Content-Type: application/json" \
  -d '{"edad": 25, "peso": 70, "altura": 1.75, "actividad": "Moderada"}'
```

**Analizar imagen**:
```bash
curl -X POST http://localhost:5000/api/analizar-imagen \
  -F "imagen=@ruta/a/imagen.jpg" \
  -F "imc=22.5" \
  -F "calorias_objetivo=2000" \
  -F "objetivo=mantener peso"
```

### Con Python (requests)

```python
import requests

# Health check
response = requests.get('http://localhost:5000/api/health')
print(response.json())

# Calcular IMC
data = {
    "edad": 25,
    "peso": 70,
    "altura": 1.75,
    "actividad": "Moderada"
}
response = requests.post('http://localhost:5000/api/calcular-imc', json=data)
print(response.json())

# Analizar imagen
with open('ruta/a/imagen.jpg', 'rb') as f:
    files = {'imagen': f}
    data = {
        'imc': 22.5,
        'calorias_objetivo': 2000,
        'objetivo': 'mantener peso'
    }
    response = requests.post('http://localhost:5000/api/analizar-imagen', 
                           files=files, data=data)
    print(response.json())
```

## ⚙️ Configuración

### Variables de Entorno

Puedes crear un archivo `.env` (no incluido en git) con:

```
FLASK_ENV=development
FLASK_DEBUG=True
MODELO_PATH=modelos/modelo_porciones.keras
MAX_UPLOAD_SIZE=10485760  # 10MB en bytes
```

### Puerto

Por defecto el servidor corre en el puerto 5000. Para cambiar:

```python
# En app.py, línea final:
app.run(debug=True, host='0.0.0.0', port=5000)  # Cambiar 5000 por otro puerto
```

## 🔍 Solución de Problemas

### Error: "No se encontró el modelo"

Asegúrate de que el modelo esté en `modelos/modelo_porciones.keras`. Si está en otra ubicación, modifica la ruta en `services/modelo_service.py`.

### Error: "ModuleNotFoundError: No module named 'flask'"

Instala Flask:
```bash
pip install flask flask-cors
```

### Error de CORS

El backend ya tiene CORS configurado. Si sigues teniendo problemas, verifica que el frontend esté haciendo peticiones a `http://localhost:5000`.

### Error al cargar el modelo

Verifica que TensorFlow esté instalado correctamente:
```bash
python -c "import tensorflow as tf; print(tf.__version__)"
```

## 📝 Notas

- El modelo se carga automáticamente al iniciar el servidor
- Las imágenes se procesan en memoria, no se guardan en disco
- El tamaño máximo de archivo es 10MB (configurable)
- El servidor corre en modo debug por defecto (cambiar en producción)

## 🔗 Integración con Frontend

El frontend ya está configurado para usar `http://localhost:5000` como API_URL.

Para conectar:
1. Inicia el backend: `python backend/app.py`
2. Abre el frontend (`index.html`) en un navegador
3. El frontend se conectará automáticamente al backend

---

**Última actualización**: Ver fecha de modificación del archivo

