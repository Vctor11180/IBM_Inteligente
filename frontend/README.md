# 🎨 Frontend - NutriLife AI + Web3

Frontend de la aplicación NutriLife que permite a los usuarios calcular su IMC, analizar imágenes de comida con IA y recibir recomendaciones nutricionales.

## 📁 Estructura

```
frontend/
├── index.html      # Aplicación principal
└── styles.css      # Estilos
```

## 🚀 Cómo Usar

### Opción 1: Abrir directamente

Simplemente abre `index.html` en tu navegador. **Nota**: Para que funcione completamente, el backend debe estar corriendo.

### Opción 2: Servidor local (Recomendado)

```bash
# Desde la carpeta frontend:
python -m http.server 8000

# O desde la raíz del proyecto:
cd frontend
python -m http.server 8000
```

Luego abre: `http://localhost:8000`

## 🔧 Requisitos

- Backend corriendo en `http://localhost:5000`
- Navegador moderno (Chrome, Firefox, Edge, Safari)

## 📱 Funcionalidades

### 1. Calculadora de IMC
- Ingresa edad, peso, altura y nivel de actividad
- Calcula IMC automáticamente
- Genera plan nutricional personalizado

### 2. Análisis de Imágenes
- Sube imágenes de comida (clic o arrastrar)
- Analiza con modelo de IA
- Muestra si la porción es correcta o excesiva
- Recomendaciones personalizadas según IMC

### 3. NutriBot (Chatbot)
- Haz preguntas sobre nutrición
- Botón 📷 para analizar imágenes
- Preguntas frecuentes predefinidas

## 🎯 Características

- ✅ Diseño moderno y responsive
- ✅ Drag & drop para imágenes
- ✅ Vista previa de imágenes
- ✅ Estados de carga
- ✅ Manejo de errores
- ✅ Almacenamiento local (localStorage) para datos del IMC

## 📡 Conexión con Backend

El frontend se conecta automáticamente a:
- `http://localhost:5000/api/calcular-imc` - Cálculo de IMC
- `http://localhost:5000/api/analizar-imagen` - Análisis de imágenes

Para cambiar la URL del backend, edita la variable `API_URL` en `index.html`:

```javascript
const API_URL = "http://localhost:5000/api";
```

---

**Última actualización**: Ver fecha de modificación del archivo

