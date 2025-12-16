# 📚 Documentación del Proyecto NutriLife AI + Web3

Bienvenido a la documentación del proyecto NutriLife. Aquí encontrarás toda la información necesaria para entender y desarrollar la aplicación.

## 📖 Documentos Disponibles

### 1. **DOCUMENTACION_APLICACION.md**
Documentación completa de la aplicación. Incluye:
- Visión general del proyecto
- Arquitectura del sistema
- Funcionalidades principales
- Integración de IA y Web3
- Stack tecnológico
- Plan de desarrollo por fases
- Casos de uso
- Consideraciones de seguridad

👉 **Lee este documento primero** para tener una visión completa del proyecto.

---

### 2. **FASE1_ENTRENAMIENTO.md**
Documentación específica de la Fase 1: Entrenamiento del Modelo IA.
- Objetivos de la fase
- Checklist de tareas
- Descripción de datos disponibles
- Arquitectura del modelo
- Flujo de trabajo
- Métricas esperadas

---

## 🚀 Inicio Rápido

### Fase 1: Entrenamiento del Modelo (Actual)

1. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Preprocesar imágenes:**
   ```bash
   python scripts/preprocesamiento.py
   ```

3. **Entrenar modelo:**
   ```bash
   python scripts/entrenar_modelo.py
   ```

4. **Probar predicciones:**
   ```bash
   python scripts/predecir.py ruta/a/imagen.jpg
   ```

---

## 📂 Estructura del Proyecto

```
proyecto/
├── documentacion/          # Esta carpeta
│   ├── DOCUMENTACION_APLICACION.md
│   ├── FASE1_ENTRENAMIENTO.md
│   └── README.md
├── scripts/                # Scripts de entrenamiento
│   ├── preprocesamiento.py
│   ├── entrenar_modelo.py
│   ├── predecir.py
│   └── README.md
├── entrenamiento/          # Datos de entrenamiento
│   ├── Porcion_correcta/
│   └── Exceso_porcion/
├── validacion/            # Datos de validación
│   ├── Porcioncorrecta/
│   └── Porcionexceso/
├── modelos/               # Modelos entrenados (generados)
├── datos_preprocesados/   # Datos preprocesados (generados)
├── index.html             # Frontend
├── styles.css             # Estilos
└── requirements.txt       # Dependencias
```

---

## 📈 Estado del Proyecto

### Fase 1: Entrenamiento y Validación del Modelo IA ✅ (En Progreso)
- [x] Recopilación de datos de entrenamiento
- [x] Organización de carpetas
- [x] Documentación
- [x] Scripts de preprocesamiento
- [x] Scripts de entrenamiento
- [ ] Ejecutar entrenamiento
- [ ] Validar modelo
- [ ] Exportar modelo

### Fase 2: Backend API para IA 🚧 (Pendiente)
- [ ] Endpoint para análisis de imágenes
- [ ] Integración del modelo
- [ ] Cálculo de calorías
- [ ] Recomendaciones según IMC

### Fase 3: Integración Frontend-Backend 🚧 (Pendiente)
- [ ] Componente de subida de imágenes
- [ ] Visualización de resultados
- [ ] Conexión con API

### Fase 4: Integración Web3 - IPFS 🚧 (Pendiente)
- [ ] Configuración IPFS
- [ ] Subida de imágenes
- [ ] Almacenamiento de hashes

### Fase 5: Integración Web3 - Blockchain 🚧 (Pendiente)
- [ ] Smart Contract
- [ ] Tests del contrato
- [ ] Deployment
- [ ] Integración frontend

### Fase 6: Funcionalidades Avanzadas 🚧 (Pendiente)
- [ ] Historial de análisis
- [ ] Dashboard de progreso
- [ ] Sistema de recompensas

---

## 🛠️ Stack Tecnológico

### IA/ML
- TensorFlow/Keras
- OpenCV, PIL
- NumPy, Pandas
- Albumentations

### Frontend
- HTML5, CSS3, JavaScript

### Backend (Fases posteriores)
- Python/Flask
- Web3.py

### Web3 (Fases posteriores)
- IPFS
- Ethereum/Polygon
- Solidity
- MetaMask

---

## 📝 Notas Importantes

1. **Dataset Pequeño**: Actualmente tenemos 17 imágenes de entrenamiento y 9 de validación. Esto es suficiente para un prototipo, pero para producción se necesitarían más datos.

2. **Transfer Learning**: Usamos MobileNetV2 con transfer learning para aprovechar al máximo el dataset pequeño.

3. **Data Augmentation**: Esencial para mejorar el rendimiento con pocos datos.

4. **Web3**: La integración Web3 será implementada en fases posteriores (4 y 5).

---

## 🤝 Contribuciones

Este proyecto está en desarrollo activo. Consulta los documentos específicos de cada fase para más detalles.

---

## 📧 Contacto y Soporte

Para preguntas o sugerencias sobre el proyecto, consulta la documentación específica de cada fase o revisa los scripts comentados en el código.

---

**Última actualización**: Ver fecha en cada documento individual.

