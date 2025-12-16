# 🍃 NutriLife AI + Web3

Aplicación web inteligente que combina Inteligencia Artificial y tecnología Web3 para proporcionar recomendaciones nutricionales personalizadas basadas en el análisis de imágenes de alimentos y el Índice de Masa Corporal (IMC) del usuario.

## 🚀 Inicio Rápido

### Opción 1: Script Automático (Windows)

```bash
iniciar_app.bat
```

Esto iniciará automáticamente el backend y el frontend.

### Opción 2: Manual

**Paso 1: Inicia el Backend**

```bash
python backend/app.py
```

Espera a ver:
```
🚀 Iniciando NutriLife Backend API
📡 Servidor corriendo en: http://localhost:5000
```

**Paso 2: Inicia el Frontend (en otra terminal)**

```bash
cd frontend
python -m http.server 8000
```

**Paso 3: Abre en el navegador**

Abre: **http://localhost:8000**

---

## 📋 Requisitos

- Python 3.8+
- TensorFlow 2.10+
- Flask 2.2+
- Navegador moderno

### Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 🎯 Funcionalidades

### ✅ Fase 1: Entrenamiento del Modelo IA
- Modelo de clasificación de porciones entrenado
- Clasifica entre "porción correcta" y "exceso"

### ✅ Fase 2: Backend API
- API REST con Flask
- Endpoints para cálculo de IMC y análisis de imágenes
- Integración con modelo de IA

### ✅ Fase 3: Frontend Integrado
- Calculadora de IMC
- Análisis de imágenes de comida
- Chatbot NutriBot
- Recomendaciones personalizadas

### 🚧 Fase 4-6: Web3 (Pendiente)
- IPFS para almacenamiento descentralizado
- Blockchain para historial inmutable

---

## 📁 Estructura del Proyecto

```
ia_web3/
├── backend/           # API Flask
│   ├── app.py
│   ├── routes/
│   └── services/
├── frontend/          # Aplicación web
│   ├── index.html
│   └── styles.css
├── scripts/           # Scripts de entrenamiento
├── modelos/           # Modelos entrenados
├── entrenamiento/     # Datos de entrenamiento
├── validacion/        # Datos de validación
└── documentacion/     # Documentación completa
```

---

## 🔧 Solución de Problemas

### Error: "Error al conectar con el servidor"

**Solución**: Asegúrate de que el backend esté corriendo:
```bash
python backend/app.py
```

### Error: "Failed to fetch"

**Solución**: No uses `file:///`. Usa un servidor local:
```bash
cd frontend
python -m http.server 8000
```

### Ver más problemas

Consulta `frontend/SOLUCION_ERRORES.md` para más detalles.

---

## 📚 Documentación

- `documentacion/` - Documentación completa del proyecto
- `documentacion/fase1/` - Fase 1: Entrenamiento IA
- `documentacion/fase2/` - Fase 2: Backend API
- `documentacion/fase3/` - Fase 3: Integración Frontend
- `frontend/README.md` - Documentación del frontend
- `backend/README.md` - Documentación del backend

---

## 🎓 Uso

1. **Calcula tu IMC** (recomendado primero):
   - Ve a "Calculadora IMC"
   - Ingresa tus datos
   - Haz clic en "Calcular mi IMC"

2. **Analiza una comida**:
   - Ve a "📷 Analizar Comida"
   - Sube una imagen (arrastra o clic)
   - Haz clic en "🔍 Analizar Comida"
   - Ve los resultados

3. **Usa el Chatbot**:
   - Ve a "NutriBot"
   - Haz preguntas sobre nutrición
   - O usa el botón 📷 para analizar imágenes

---

## 🔗 Tecnologías

- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: Python, Flask
- **IA/ML**: TensorFlow, Keras, MobileNetV2
- **Procesamiento**: OpenCV, PIL

---

## 📝 Estado del Proyecto

- ✅ Fase 1: Modelo IA entrenado
- ✅ Fase 2: Backend API funcionando
- ✅ Fase 3: Frontend integrado
- 🚧 Fase 4: IPFS (Pendiente)
- 🚧 Fase 5: Blockchain (Pendiente)
- 🚧 Fase 6: Funcionalidades avanzadas (Pendiente)

---

## 📧 Contacto

Para más información, consulta la documentación en `documentacion/`.

---

**Versión**: 1.0.0  
**Última actualización**: Diciembre 2025

