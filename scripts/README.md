# 📁 Scripts de Entrenamiento - Fase 1

Este directorio contiene los scripts necesarios para entrenar el modelo de clasificación de porciones de comida.

## 📋 Scripts Disponibles

### 1. `preprocesamiento.py`
Preprocesa las imágenes del dataset de entrenamiento y validación.

**Uso:**
```bash
python scripts/preprocesamiento.py
```

**Funcionalidades:**
- Carga imágenes de las carpetas `entrenamiento/` y `validacion/`
- Redimensiona imágenes a 224x224
- Normaliza los valores de píxeles
- Guarda los datos preprocesados en `datos_preprocesados/`
- Genera visualización de muestras

**Output:**
- `datos_preprocesados/X_train.npy`
- `datos_preprocesados/y_train.npy`
- `datos_preprocesados/X_val.npy`
- `datos_preprocesados/y_val.npy`
- `documentacion/muestras_dataset.png`

---

### 2. `entrenar_modelo.py`
Entrena el modelo de clasificación usando Transfer Learning con MobileNetV2.

**Uso:**
```bash
python scripts/entrenar_modelo.py
```

**Funcionalidades:**
- Construye modelo basado en MobileNetV2
- Aplica data augmentation
- Entrena el modelo con early stopping
- Evalúa el modelo en el conjunto de validación
- Genera gráficos de entrenamiento
- Guarda el mejor modelo

**Output:**
- `modelos/mejor_modelo.h5` (mejor modelo durante entrenamiento)
- `modelos/modelo_porciones` (modelo final)
- `documentacion/historial_entrenamiento.png`
- `documentacion/matriz_confusion.png`

---

### 3. `predecir.py`
Hace predicciones sobre imágenes individuales usando el modelo entrenado.

**Uso:**
```bash
# Analizar una imagen
python scripts/predecir.py ruta/a/imagen.jpg

# Especificar modelo personalizado
python scripts/predecir.py ruta/a/imagen.jpg --modelo modelos/mi_modelo
```

**Ejemplo:**
```bash
python scripts/predecir.py validacion/Porcioncorrecta/v1.jpg
```

**Output:**
- Muestra en consola:
  - Clasificación (Porción Correcta / Exceso)
  - Probabilidades
  - Confianza

---

## 🔄 Flujo de Trabajo Recomendado

```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Preprocesar imágenes
python scripts/preprocesamiento.py

# 3. Entrenar modelo
python scripts/entrenar_modelo.py

# 4. Probar predicciones
python scripts/predecir.py validacion/Porcioncorrecta/v1.jpg
```

---

## 📊 Estructura Esperada de Carpetas

```
proyecto/
├── entrenamiento/
│   ├── Porcion_correcta/
│   └── Exceso_porcion/
├── validacion/
│   ├── Porcioncorrecta/
│   └── Porcionexceso/
├── scripts/
│   ├── preprocesamiento.py
│   ├── entrenar_modelo.py
│   └── predecir.py
├── modelos/              # (se crea automáticamente)
├── datos_preprocesados/  # (se crea automáticamente)
└── documentacion/        # (se crea automáticamente)
```

---

## ⚙️ Configuración

### Hiperparámetros del Modelo

En `entrenar_modelo.py` puedes ajustar:
- `img_size`: Tamaño de las imágenes (default: 224x224)
- `epochs`: Número de épocas (default: 50)
- `batch_size`: Tamaño del batch (default: 4)
- `learning_rate`: Tasa de aprendizaje (default: 0.0001)

### Data Augmentation

En `entrenar_modelo.py` puedes modificar los parámetros de augmentation en `crear_data_augmentation()`:
- `rotation_range`: Rango de rotación
- `width_shift_range`: Desplazamiento horizontal
- `height_shift_range`: Desplazamiento vertical
- `zoom_range`: Rango de zoom
- `horizontal_flip`: Volteo horizontal

---

## 🐛 Solución de Problemas

### Error: "No se encontraron datos preprocesados"
**Solución:** Ejecuta primero `preprocesamiento.py`

### Error: "CUDA out of memory"
**Solución:** Reduce el `batch_size` en `entrenar_modelo.py`

### Error: "No se pudo cargar la imagen"
**Solución:** Verifica que la ruta de la imagen sea correcta y que el formato sea compatible (jpg, jpeg, png)

---

## 📈 Métricas Esperadas

Con el dataset actual (17 imágenes entrenamiento, 9 validación):
- **Accuracy**: > 70% (aceptable con pocos datos)
- **Precision**: > 65%
- **Recall**: > 65%
- **F1-Score**: > 65%

**Nota:** Estas métricas mejorarán significativamente con más datos de entrenamiento.

---

## 🔗 Referencias

- [TensorFlow Documentation](https://www.tensorflow.org/)
- [Keras Transfer Learning Guide](https://www.tensorflow.org/tutorials/images/transfer_learning)
- [MobileNetV2 Paper](https://arxiv.org/abs/1801.04381)

