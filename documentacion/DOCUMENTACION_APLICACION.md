# 📋 Documentación de la Aplicación: NutriLife AI + Web3

## 🎯 Visión General del Proyecto

**NutriLife** es una aplicación web inteligente que combina Inteligencia Artificial (IA) y tecnología Web3 para proporcionar recomendaciones nutricionales personalizadas basadas en el análisis de imágenes de alimentos y el Índice de Masa Corporal (IMC) del usuario.

### Propósito Principal
- Analizar imágenes de comida subidas por el usuario
- Calcular si la porción es adecuada o excesiva según el IMC individual
- Proporcionar recomendaciones nutricionales personalizadas
- Utilizar tecnologías Web3 para descentralización y transparencia

---

## 🏗️ Arquitectura del Sistema

### Componentes Principales

```
┌─────────────────────────────────────────────────────────────┐
│                    FRONTEND (Web App)                        │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │ Calculadora  │  │  Análisis    │  │ NutriBot     │      │
│  │     IMC      │  │  de Imágenes │  │   Chat       │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└───────────────────────┬──────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│              BACKEND API (Python/Flask)                      │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │  Endpoint    │  │  Integración │  │  Almacenamiento│    │
│  │  IMC Calc    │  │     IA       │  │   Web3/IPFS  │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└───────────────────────┬──────────────────────────────────────┘
                        │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│  Modelo IA   │ │  Blockchain  │ │  IPFS Storage│
│  (TensorFlow │ │  (Smart      │ │  (Imágenes   │
│  / PyTorch)  │ │  Contracts)  │ │  descentral.)│
└──────────────┘ └──────────────┘ └──────────────┘
```

---

## 🔧 Funcionalidades Principales

### 1. **Calculadora de IMC** ✅ (Implementado)
- **Entrada**: Edad, peso, altura, nivel de actividad física
- **Salida**: 
  - IMC calculado
  - Clasificación (bajo peso, normal, sobrepeso, obesidad)
  - Calorías diarias recomendadas
  - Plan nutricional personalizado (desayuno, almuerzo, cena, snacks)

### 2. **Análisis de Imágenes con IA** 🚧 (Por Implementar)
- **Entrada**: Imagen de comida subida por el usuario
- **Proceso**:
  1. Modelo de IA clasifica la imagen (porción correcta vs. exceso)
  2. Identifica el tipo de alimento
  3. Estima la cantidad/porción en gramos
  4. Calcula calorías aproximadas
- **Salida**:
  - Análisis de si la porción es adecuada según IMC del usuario
  - Recomendaciones específicas para ajustar la porción
  - Información nutricional detallada

### 3. **NutriBot (Chatbot Inteligente)** 🚧 (Parcialmente Implementado)
- Asistente conversacional para consultas nutricionales
- Integración con modelo de lenguaje (GPT/LLM)
- Soporte para preguntas sobre nutrición
- Capacidad de análisis de imágenes conversacional

### 4. **Integración Web3** 🚧 (Por Implementar)
- **Almacenamiento Descentralizado (IPFS)**:
  - Guardar imágenes de análisis en IPFS
  - Crear hashes únicos para cada imagen analizada
- **Blockchain (Smart Contracts)**:
  - Registro inmutable de historial nutricional
  - Sistema de tokens/recompensas por logros nutricionales
  - Transparencia y trazabilidad de datos
  - Ownership de datos por parte del usuario

---

## 🤖 Componente de Inteligencia Artificial

### Modelo de Clasificación de Porciones

#### Datos de Entrenamiento
```
entrenamiento/
├── Porcion_correcta/    (9 imágenes) ✅
│   ├── 1.jpg
│   ├── 2.jpg
│   └── ...
└── Exceso_porcion/      (8 imágenes) ✅
    ├── a.jpg
    ├── b.jpg
    └── ...
```

#### Datos de Validación
```
validacion/
├── Porcioncorrecta/     (5 imágenes) ✅
│   ├── v1.jpg
│   └── ...
└── Porcionexceso/       (4 imágenes) ✅
    ├── va.jpg
    └── ...
```

### Pipeline de IA

1. **Preprocesamiento de Imágenes**:
   - Redimensionamiento (224x224 o 512x512)
   - Normalización de píxeles
   - Data augmentation (rotaciones, brillo, contraste)

2. **Modelo Base**:
   - Opción A: Transfer Learning con ResNet50/VGG16
   - Opción B: Modelo personalizado CNN
   - Opción C: Vision Transformer (ViT)

3. **Clasificación**:
   - Binary Classification: Porción Correcta (0) vs. Exceso (1)
   - Output: Probabilidad de clase + confianza

4. **Análisis Adicional** (Fase 2):
   - Detección de objetos (identificar tipos de alimentos)
   - Estimación de volumen/porción
   - Cálculo de calorías aproximadas

### Stack Tecnológico de IA
- **Framework**: TensorFlow/Keras o PyTorch
- **Procesamiento**: OpenCV, PIL/Pillow
- **Data Augmentation**: Albumentations
- **Model Deployment**: TensorFlow Serving o ONNX Runtime

---

## 🌐 Integración Web3

### 1. Almacenamiento IPFS

**Propósito**: Guardar imágenes de análisis de forma descentralizada

**Flujo**:
```
Usuario sube imagen 
  → Backend procesa imagen 
  → Sube a IPFS (Pinata, Infura, o IPFS local)
  → Obtiene hash IPFS (CID)
  → Guarda hash en blockchain/metadata
```

**Ventajas**:
- Descentralización
- Inmutabilidad
- Ownership del usuario sobre sus datos
- No hay servidor central que pueda caer

### 2. Blockchain (Ethereum/Polygon)

**Smart Contract Funcionalidades**:
- **Registro de Análisis**: Guardar hash IPFS + IMC + resultado del análisis
- **Historial Nutricional**: Línea de tiempo de todos los análisis
- **Sistema de Recompensas**: Tokens NFT o ERC-20 por logros nutricionales
- **Permisos**: El usuario controla quién puede ver sus datos

**Ejemplo de Estructura de Datos en Blockchain**:
```solidity
struct AnalisisNutricional {
    address usuario;
    string ipfsHash;        // Hash de la imagen en IPFS
    uint256 timestamp;
    uint256 imc;
    bool porcionCorrecta;
    uint256 caloriasEstimadas;
    string recomendaciones;
}
```

### 3. Wallet Integration

**Requisitos**:
- Conexión de wallet (MetaMask, WalletConnect)
- Firma de transacciones para guardar datos
- Visualización de historial en blockchain

---

## 🔄 Flujo Completo de la Aplicación

### Escenario: Usuario sube imagen de comida

```
1. Usuario inicia sesión/conecta wallet Web3
   ↓
2. Usuario ingresa sus datos (peso, altura, edad, actividad)
   ↓
3. Sistema calcula IMC y establece rangos objetivos
   ↓
4. Usuario sube imagen de comida
   ↓
5. Imagen se preprocesa (resize, normalize)
   ↓
6. Modelo IA clasifica:
   - ¿Porción correcta o exceso?
   - Tipo de alimento
   - Cantidad estimada
   ↓
7. Sistema compara con IMC del usuario:
   - "Tu IMC es X, necesitas Y calorías diarias"
   - "Esta porción tiene Z calorías"
   - "Es adecuada/excesiva para tu objetivo"
   ↓
8. Imagen se sube a IPFS → se obtiene hash
   ↓
9. Hash + análisis se guarda en blockchain (smart contract)
   ↓
10. Usuario recibe feedback visual:
    - Imagen analizada con anotaciones
    - Recomendaciones personalizadas
    - Opción de ver historial en blockchain
```

---

## 📊 Estructura de Datos

### Perfil de Usuario (Frontend/Backend)
```json
{
  "edad": 25,
  "peso": 70,
  "altura": 1.75,
  "actividad": "Moderada",
  "imc": 22.86,
  "categoriaIMC": "Normal",
  "caloriasObjetivo": 2200,
  "walletAddress": "0x..."
}
```

### Análisis de Imagen (Respuesta del Modelo)
```json
{
  "porcionCorrecta": true,
  "confianza": 0.92,
  "tipoAlimento": "Pollo con arroz y verduras",
  "caloriasEstimadas": 450,
  "gramos": 350,
  "recomendacion": "Porción adecuada para tu objetivo calórico",
  "alimentos": [
    {"nombre": "Pollo", "gramos": 150, "calorias": 250},
    {"nombre": "Arroz", "gramos": 100, "calorias": 130},
    {"nombre": "Verduras", "gramos": 100, "calorias": 70}
  ]
}
```

### Registro en Blockchain
```json
{
  "usuario": "0x1234...",
  "timestamp": 1234567890,
  "ipfsHash": "QmXYZ...",
  "imc": 22.86,
  "analisis": {
    "porcionCorrecta": true,
    "calorias": 450
  }
}
```

---

## 🛠️ Stack Tecnológico Completo

### Frontend
- HTML5, CSS3, JavaScript (Vanilla o Framework)
- Web3.js o Ethers.js (conexión blockchain)
- IPFS-HTTP-Client (subida a IPFS)

### Backend
- Python 3.8+
- Flask/FastAPI (API REST)
- TensorFlow/PyTorch (modelo IA)
- OpenCV, PIL (procesamiento imágenes)
- web3.py (interacción blockchain)

### IA/ML
- TensorFlow/Keras o PyTorch
- TensorFlow Serving (deployment)
- NumPy, Pandas
- Matplotlib (visualización)

### Web3
- IPFS (Pinata, Infura, o nodo local)
- Ethereum/Polygon blockchain
- Solidity (smart contracts)
- Hardhat/Truffle (desarrollo contracts)
- MetaMask (wallet)

### Infraestructura
- Google Colab (entrenamiento inicial)
- Render/Railway/Heroku (deployment backend)
- Vercel/Netlify (deployment frontend)

---

## 📈 Plan de Desarrollo por Fases

### Fase 1: Entrenamiento y Validación del Modelo IA ✅ (En Progreso)
- [x] Recopilación de datos de entrenamiento
- [x] Organización de carpetas (entrenamiento/validación)
- [ ] Script de preprocesamiento de imágenes
- [ ] Desarrollo del modelo (CNN o Transfer Learning)
- [ ] Entrenamiento del modelo
- [ ] Validación con conjunto de test
- [ ] Exportación del modelo (SavedModel/ONNX)

### Fase 2: Backend API para IA
- [ ] Endpoint para análisis de imágenes (`/analizar-imagen`)
- [ ] Integración del modelo entrenado
- [ ] Preprocesamiento en tiempo real
- [ ] Cálculo de calorías basado en análisis
- [ ] Recomendaciones según IMC

### Fase 3: Integración Frontend-Backend
- [ ] Componente de subida de imágenes
- [ ] Visualización de resultados del análisis
- [ ] Conexión con API backend
- [ ] Feedback visual (anotaciones en imagen)

### Fase 4: Integración Web3 - IPFS
- [ ] Configuración de cliente IPFS
- [ ] Subida de imágenes a IPFS
- [ ] Almacenamiento de hashes
- [ ] Visualización de imágenes desde IPFS

### Fase 5: Integración Web3 - Blockchain
- [ ] Desarrollo de Smart Contract
- [ ] Tests del contrato
- [ ] Deployment a testnet (Goerli/Polygon Mumbai)
- [ ] Integración frontend (conexión wallet)
- [ ] Guardado de análisis en blockchain

### Fase 6: Funcionalidades Avanzadas
- [ ] Historial de análisis (desde blockchain)
- [ ] Dashboard de progreso nutricional
- [ ] Sistema de recompensas (tokens/NFTs)
- [ ] Comparación temporal (evolución del usuario)

---

## 🎯 Casos de Uso Específicos

### Caso 1: Usuario con IMC Normal quiere mantener peso
- **Input**: IMC 22, objetivo "mantener peso", imagen de plato
- **Proceso**: IA determina porción correcta/exceso
- **Output**: "Porción adecuada de 450 cal. Perfecto para tu objetivo de 2000 cal/día"

### Caso 2: Usuario con sobrepeso quiere perder peso
- **Input**: IMC 28, objetivo "perder peso", imagen de plato grande
- **Proceso**: IA detecta exceso, calcula calorías
- **Output**: "Porción excesiva (750 cal). Para tu objetivo de 1500 cal/día, reduce a 60% de esta porción"

### Caso 3: Usuario quiere ganar masa muscular
- **Input**: IMC 20, objetivo "ganar peso", imagen de plato pequeño
- **Proceso**: IA detecta porción pequeña
- **Output**: "Porción insuficiente (300 cal). Para tu objetivo de 2800 cal/día, aumenta un 40% más de proteína"

---

## 🔐 Consideraciones de Seguridad y Privacidad

### Privacidad de Datos
- Las imágenes se almacenan en IPFS con encriptación opcional
- Solo el usuario (wallet owner) puede acceder a su historial
- Smart contracts implementan permisos (onlyOwner)

### Validación
- Validación de formato de imagen en frontend y backend
- Límites de tamaño de archivo
- Sanitización de inputs

### Blockchain
- Uso de testnet para desarrollo
- Gas optimization en smart contracts
- Consideración de costos de transacción

---

## 📝 Próximos Pasos Inmediatos

1. **Entrenar el Modelo IA**:
   - Crear script de entrenamiento en Python
   - Usar datos de `entrenamiento/` y `validacion/`
   - Guardar modelo entrenado

2. **Desarrollar Backend API**:
   - Endpoint para recibir imágenes
   - Integrar modelo entrenado
   - Retornar análisis JSON

3. **Integrar en Frontend**:
   - Añadir componente de upload de imágenes
   - Mostrar resultados del análisis
   - Conectar con backend

4. **Implementar Web3**:
   - Configurar IPFS
   - Desarrollar smart contract básico
   - Conectar wallet en frontend

---

## 📚 Recursos y Referencias

### IA/ML
- TensorFlow Documentation
- Transfer Learning Guide
- Food Image Recognition Datasets

### Web3
- IPFS Documentation
- Solidity Documentation
- Web3.js/Ethers.js Guides
- MetaMask Integration

### Nutrición
- Fórmulas de cálculo IMC
- Tablas calóricas de alimentos
- Guías nutricionales (OMS, FDA)

---

## 🤝 Contribuciones y Notas

Este documento es un blueprint vivo que se actualizará conforme avance el desarrollo del proyecto.

**Última actualización**: [Fecha]

**Autor**: Equipo NutriLife

---

## ✅ Checklist de Implementación

- [x] Documentación de aplicación
- [ ] Entrenamiento modelo IA
- [ ] Backend API básico
- [ ] Integración frontend-backend
- [ ] Integración IPFS
- [ ] Smart contracts
- [ ] Integración blockchain frontend
- [ ] Testing completo
- [ ] Deployment producción

