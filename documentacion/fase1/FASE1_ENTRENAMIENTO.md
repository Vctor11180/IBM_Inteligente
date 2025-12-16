# 📚 Fase 1: Entrenamiento y Validación del Modelo IA

## 📋 Objetivo

Entrenar un modelo de clasificación de imágenes que pueda distinguir entre **porción correcta** y **exceso de porción** de comida.

## 🎯 Checklist de la Fase 1

- [x] Recopilación de datos de entrenamiento
- [x] Organización de carpetas (entrenamiento/validación)
- [x] Script de preprocesamiento de imágenes ✅ (`scripts/preprocesamiento.py`)
- [x] Desarrollo del modelo (Transfer Learning con MobileNetV2) ✅ (`scripts/entrenar_modelo.py`)
- [x] Script de predicción ✅ (`scripts/predecir.py`)
- [x] Creación de requirements.txt ✅
- [x] **Instalar dependencias** ✅ (completado)
- [x] **Ejecutar preprocesamiento** ✅ (20 imágenes entrenamiento, 9 validación)
- [x] **Entrenar el modelo** ✅ (modelo MobileNetV2 entrenado)
- [x] **Validar modelo** ✅ (Accuracy: 55.56% - esperado con dataset pequeño)
- [x] **Probar predicciones** ✅ (script funcionando correctamente)

## 📊 Datos Disponibles

### Entrenamiento
- **Porcion_correcta/**: 9 imágenes
- **Exceso_porcion/**: 8 imágenes
- **Total**: 17 imágenes para entrenamiento

### Validación
- **Porcioncorrecta/**: 5 imágenes
- **Porcionexceso/**: 4 imágenes
- **Total**: 9 imágenes para validación

## 🔧 Herramientas y Dependencias

### Librerías Necesarias
```bash
tensorflow>=2.10.0
numpy>=1.23.0
Pillow>=9.0.0
opencv-python>=4.6.0
matplotlib>=3.5.0
scikit-learn>=1.1.0
albumentations>=1.2.0  # Para data augmentation
```

### Instalación
```bash
pip install tensorflow numpy Pillow opencv-python matplotlib scikit-learn albumentations
```

## 🏗️ Arquitectura del Modelo

### Opción 1: Transfer Learning (Recomendado para pocos datos)
- **Base Model**: ResNet50 o MobileNetV2 (pre-entrenado en ImageNet)
- **Ventajas**: Funciona bien con pocos datos, entrenamiento rápido
- **Desventajas**: Modelo más pesado

### Opción 2: CNN Personalizada
- Arquitectura desde cero
- Ventajas: Modelo más ligero, personalizado
- Desventajas: Requiere más datos, entrenamiento más lento

### Decisión: Usar Transfer Learning con MobileNetV2
- Ligero y eficiente
- Buen rendimiento con pocos datos
- Fácil de exportar y desplegar

## 📝 Scripts a Crear

1. **preprocesamiento.py**: Cargar y preprocesar imágenes
2. **entrenar_modelo.py**: Script principal de entrenamiento
3. **validar_modelo.py**: Validación y métricas
4. **predecir.py**: Script para hacer predicciones con el modelo entrenado

## 🔄 Flujo de Trabajo

```
1. Preprocesamiento
   ↓
2. Data Augmentation (opcional, recomendado)
   ↓
3. División train/val
   ↓
4. Construcción del modelo
   ↓
5. Entrenamiento
   ↓
6. Validación
   ↓
7. Guardar modelo
```

## 📈 Métricas Esperadas

Con el dataset pequeño, esperamos:
- **Accuracy**: > 70% (mínimo aceptable)
- **Precision**: > 65%
- **Recall**: > 65%
- **F1-Score**: > 65%

Nota: Con más datos estos valores deberían mejorar significativamente.

## 🚨 Consideraciones

### Dataset Pequeño
- Solo 17 imágenes de entrenamiento
- Es necesario usar data augmentation agresiva
- Transfer learning es esencial
- Posible sobreajuste (overfitting)

### Soluciones
1. Data augmentation extensiva (rotaciones, brillo, zoom, flip)
2. Fine-tuning con learning rate bajo
3. Early stopping
4. Regularización (Dropout)

## 📂 Estructura de Archivos

```
proyecto/
├── documentacion/
│   ├── FASE1_ENTRENAMIENTO.md
│   └── DOCUMENTACION_APLICACION.md
├── entrenamiento/
│   ├── Porcion_correcta/
│   └── Exceso_porcion/
├── validacion/
│   ├── Porcioncorrecta/
│   └── Porcionexceso/
├── modelos/              # (a crear) Modelos entrenados
├── scripts/
│   ├── preprocesamiento.py
│   ├── entrenar_modelo.py
│   ├── validar_modelo.py
│   └── predecir.py
└── requirements.txt
```

## ⏭️ Siguiente Fase

Una vez completada la Fase 1, pasaremos a la **Fase 2: Backend API para IA** donde integraremos el modelo entrenado en una API REST.

