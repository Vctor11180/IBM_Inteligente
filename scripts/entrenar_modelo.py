"""
Script para entrenar el modelo de clasificación de porciones de comida.

Usa Transfer Learning con MobileNetV2 para clasificar entre:
- Porción correcta (0)
- Exceso de porción (1)
"""

import os
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau, ModelCheckpoint
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns

# Configurar para evitar warnings y usar GPU si está disponible
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
physical_devices = tf.config.list_physical_devices('GPU')
if len(physical_devices) > 0:
    print(f"GPU disponible: {physical_devices[0]}")
    tf.config.experimental.set_memory_growth(physical_devices[0], True)
else:
    print("Usando CPU")

class EntrenadorModelo:
    """Clase para entrenar el modelo de clasificación."""
    
    def __init__(self, img_size=(224, 224), num_classes=2):
        """
        Inicializa el entrenador.
        
        Args:
            img_size: Tamaño de las imágenes
            num_classes: Número de clases (2: correcta, exceso)
        """
        self.img_size = img_size
        self.num_classes = num_classes
        self.model = None
        self.history = None
    
    def construir_modelo(self):
        """
        Construye el modelo usando Transfer Learning con MobileNetV2.
        
        Returns:
            Model: Modelo compilado de Keras
        """
        print("\n" + "=" * 50)
        print("CONSTRUYENDO MODELO")
        print("=" * 50)
        
        # Base model: MobileNetV2 pre-entrenado (sin las capas finales)
        base_model = MobileNetV2(
            input_shape=(*self.img_size, 3),
            include_top=False,
            weights='imagenet'
        )
        
        # Congelar las capas base inicialmente (opcional: descongelar después)
        base_model.trainable = False
        
        # Construir el modelo completo
        inputs = keras.Input(shape=(*self.img_size, 3))
        
        # Preprocesamiento (normalización para MobileNetV2)
        x = tf.keras.applications.mobilenet_v2.preprocess_input(inputs)
        
        # Base model
        x = base_model(x, training=False)
        
        # Pooling global
        x = layers.GlobalAveragePooling2D()(x)
        
        # Dropout para regularización
        x = layers.Dropout(0.3)(x)
        
        # Capa densa intermedia
        x = layers.Dense(128, activation='relu')(x)
        x = layers.Dropout(0.3)(x)
        
        # Capa de salida (clasificación binaria)
        outputs = layers.Dense(1, activation='sigmoid')(x)
        
        # Crear modelo
        model = keras.Model(inputs, outputs)
        
        # Compilar modelo
        model.compile(
            optimizer=keras.optimizers.Adam(learning_rate=0.0001),
            loss='binary_crossentropy',
            metrics=['accuracy']
        )
        
        print("\nModelo construido:")
        model.summary()
        
        self.model = model
        return model
    
    def crear_data_augmentation(self):
        """
        Crea un generador de datos con augmentation.
        
        Returns:
            ImageDataGenerator: Generador con augmentation
        """
        return ImageDataGenerator(
            rotation_range=20,
            width_shift_range=0.2,
            height_shift_range=0.2,
            shear_range=0.2,
            zoom_range=0.2,
            horizontal_flip=True,
            fill_mode='nearest'
        )
    
    def entrenar(self, X_train, y_train, X_val, y_val, epochs=50, batch_size=8):
        """
        Entrena el modelo.
        
        Args:
            X_train: Imágenes de entrenamiento
            y_train: Etiquetas de entrenamiento
            X_val: Imágenes de validación
            y_val: Etiquetas de validación
            epochs: Número de épocas
            batch_size: Tamaño del batch
        """
        print("\n" + "=" * 50)
        print("INICIANDO ENTRENAMIENTO")
        print("=" * 50)
        
        if self.model is None:
            self.construir_modelo()
        
        # Crear directorio para modelos
        os.makedirs('modelos', exist_ok=True)
        
        # Callbacks
        callbacks = [
            EarlyStopping(
                monitor='val_loss',
                patience=10,
                restore_best_weights=True,
                verbose=1
            ),
            ReduceLROnPlateau(
                monitor='val_loss',
                factor=0.5,
                patience=5,
                min_lr=1e-7,
                verbose=1
            ),
            ModelCheckpoint(
                'modelos/mejor_modelo.h5',
                monitor='val_accuracy',
                save_best_only=True,
                verbose=1
            )
        ]
        
        # Data augmentation solo para entrenamiento
        datagen = self.crear_data_augmentation()
        
        # Entrenar modelo
        print(f"\nEntrenando con {len(X_train)} imágenes de entrenamiento...")
        print(f"Validando con {len(X_val)} imágenes...")
        
        # Preprocesar imágenes para MobileNetV2
        X_train_prep = tf.keras.applications.mobilenet_v2.preprocess_input(X_train * 255.0)
        X_val_prep = tf.keras.applications.mobilenet_v2.preprocess_input(X_val * 255.0)
        
        # Entrenar con data augmentation
        self.history = self.model.fit(
            datagen.flow(X_train_prep, y_train, batch_size=batch_size),
            steps_per_epoch=len(X_train) // batch_size,
            epochs=epochs,
            validation_data=(X_val_prep, y_val),
            callbacks=callbacks,
            verbose=1
        )
        
        print("\n✓ Entrenamiento completado")
    
    def graficar_historial(self):
        """Grafica el historial de entrenamiento."""
        if self.history is None:
            print("No hay historial de entrenamiento para graficar")
            return
        
        fig, axes = plt.subplots(1, 2, figsize=(15, 5))
        
        # Accuracy
        axes[0].plot(self.history.history['accuracy'], label='Train Accuracy')
        axes[0].plot(self.history.history['val_accuracy'], label='Val Accuracy')
        axes[0].set_title('Model Accuracy')
        axes[0].set_xlabel('Epoch')
        axes[0].set_ylabel('Accuracy')
        axes[0].legend()
        axes[0].grid(True)
        
        # Loss
        axes[1].plot(self.history.history['loss'], label='Train Loss')
        axes[1].plot(self.history.history['val_loss'], label='Val Loss')
        axes[1].set_title('Model Loss')
        axes[1].set_xlabel('Epoch')
        axes[1].set_ylabel('Loss')
        axes[1].legend()
        axes[1].grid(True)
        
        plt.tight_layout()
        os.makedirs('documentacion', exist_ok=True)
        plt.savefig('documentacion/historial_entrenamiento.png', dpi=150, bbox_inches='tight')
        print("Gráfico guardado en: documentacion/historial_entrenamiento.png")
        plt.close()
    
    def evaluar(self, X_val, y_val):
        """
        Evalúa el modelo y muestra métricas detalladas.
        
        Args:
            X_val: Imágenes de validación
            y_val: Etiquetas de validación
        """
        print("\n" + "=" * 50)
        print("EVALUANDO MODELO")
        print("=" * 50)
        
        # Preprocesar
        X_val_prep = tf.keras.applications.mobilenet_v2.preprocess_input(X_val * 255.0)
        
        # Predecir
        y_pred_proba = self.model.predict(X_val_prep)
        y_pred = (y_pred_proba > 0.5).astype(int).flatten()
        
        # Métricas
        print("\nClassification Report:")
        print(classification_report(y_val, y_pred, 
                                    target_names=['Porcion Correcta', 'Exceso']))
        
        # Matriz de confusión
        cm = confusion_matrix(y_val, y_pred)
        plt.figure(figsize=(8, 6))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                    xticklabels=['Porcion Correcta', 'Exceso'],
                    yticklabels=['Porcion Correcta', 'Exceso'])
        plt.title('Matriz de Confusión')
        plt.ylabel('Real')
        plt.xlabel('Predicho')
        plt.tight_layout()
        os.makedirs('documentacion', exist_ok=True)
        plt.savefig('documentacion/matriz_confusion.png', dpi=150, bbox_inches='tight')
        print("\nMatriz de confusión guardada en: documentacion/matriz_confusion.png")
        plt.close()
        
        # Accuracy
        test_loss, test_acc = self.model.evaluate(X_val_prep, y_val, verbose=0)
        print(f"\nTest Accuracy: {test_acc:.4f}")
        print(f"Test Loss: {test_loss:.4f}")
    
    def guardar_modelo(self, ruta='modelos/modelo_final.keras'):
        """
        Guarda el modelo entrenado.
        
        Args:
            ruta: Ruta donde guardar el modelo (debe tener extensión .keras o .h5)
        """
        if self.model is None:
            print("No hay modelo para guardar")
            return
        
        # Asegurar que tiene extensión
        if not (ruta.endswith('.keras') or ruta.endswith('.h5')):
            ruta = ruta + '.keras'
        
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        self.model.save(ruta)
        print(f"\n✓ Modelo guardado en: {ruta}")


if __name__ == "__main__":
    print("=" * 60)
    print("ENTRENAMIENTO DEL MODELO DE CLASIFICACIÓN DE PORCIONES")
    print("=" * 60)
    
    # 1. Cargar datos preprocesados
    print("\n1. Cargando datos preprocesados...")
    try:
        X_train = np.load('datos_preprocesados/X_train.npy')
        y_train = np.load('datos_preprocesados/y_train.npy')
        X_val = np.load('datos_preprocesados/X_val.npy')
        y_val = np.load('datos_preprocesados/y_val.npy')
        print("   ✓ Datos cargados correctamente")
    except FileNotFoundError:
        print("   ✗ No se encontraron datos preprocesados.")
        print("   Por favor, ejecuta primero: python scripts/preprocesamiento.py")
        exit(1)
    
    # 2. Crear y entrenar modelo
    print("\n2. Creando entrenador...")
    entrenador = EntrenadorModelo(img_size=(224, 224), num_classes=2)
    
    print("\n3. Construyendo modelo...")
    entrenador.construir_modelo()
    
    print("\n4. Iniciando entrenamiento...")
    entrenador.entrenar(
        X_train, y_train,
        X_val, y_val,
        epochs=50,
        batch_size=4  # Batch pequeño por el dataset pequeño
    )
    
    # 5. Evaluar modelo
    print("\n5. Evaluando modelo...")
    entrenador.evaluar(X_val, y_val)
    
    # 6. Graficar historial
    print("\n6. Generando gráficos...")
    entrenador.graficar_historial()
    
    # 7. Guardar modelo final
    print("\n7. Guardando modelo...")
    entrenador.guardar_modelo('modelos/modelo_porciones.keras')
    
    print("\n" + "=" * 60)
    print("ENTRENAMIENTO COMPLETADO EXITOSAMENTE")
    print("=" * 60)

