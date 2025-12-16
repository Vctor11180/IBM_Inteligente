"""
Servicio para manejar predicciones del modelo de IA
"""

import os
import sys
import numpy as np
import tensorflow as tf
from tensorflow import keras
from PIL import Image
import cv2
import io

class ModeloService:
    """Servicio para cargar y usar el modelo de clasificación de porciones"""
    
    def __init__(self, ruta_modelo=None):
        """
        Inicializa el servicio del modelo
        
        Args:
            ruta_modelo: Ruta al modelo entrenado. Si es None, usa la ruta por defecto
        """
        # Obtener ruta del proyecto (subir dos niveles desde este archivo)
        if ruta_modelo is None:
            base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            ruta_modelo = os.path.join(base_dir, 'modelos', 'modelo_porciones.keras')
        
        self.ruta_modelo = ruta_modelo
        self.modelo = None
        self.img_size = (224, 224)
        self.modelo_cargado_flag = False
        
        # Cargar modelo al inicializar
        self.cargar_modelo()
    
    def cargar_modelo(self):
        """Carga el modelo entrenado"""
        try:
            if os.path.exists(self.ruta_modelo):
                print(f"📦 Cargando modelo desde: {self.ruta_modelo}")
                self.modelo = keras.models.load_model(self.ruta_modelo)
                self.modelo_cargado_flag = True
                print("✅ Modelo cargado correctamente")
            else:
                print(f"⚠️ Advertencia: No se encontró el modelo en {self.ruta_modelo}")
                self.modelo_cargado_flag = False
        except Exception as e:
            print(f"❌ Error al cargar el modelo: {str(e)}")
            self.modelo_cargado_flag = False
            self.modelo = None
    
    def modelo_cargado(self):
        """Verifica si el modelo está cargado"""
        return self.modelo_cargado_flag and self.modelo is not None
    
    def preprocesar_imagen(self, imagen_file):
        """
        Preprocesa una imagen para la predicción
        
        Args:
            imagen_file: Archivo de imagen (FileStorage de Flask)
            
        Returns:
            numpy array: Imagen preprocesada y normalizada
        """
        try:
            # Leer imagen desde el archivo
            imagen_bytes = imagen_file.read()
            imagen_file.seek(0)  # Resetear posición del archivo
            
            # Convertir bytes a imagen
            imagen = Image.open(io.BytesIO(imagen_bytes))
            
            # Convertir a RGB si es necesario
            if imagen.mode != 'RGB':
                imagen = imagen.convert('RGB')
            
            # Convertir PIL a numpy array
            img_array = np.array(imagen)
            
            # Convertir a OpenCV formato (BGR)
            img_bgr = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
            
            # Redimensionar
            img_resized = cv2.resize(img_bgr, self.img_size)
            
            # Convertir BGR a RGB para TensorFlow
            img_rgb = cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB)
            
            # Normalizar a [0, 1]
            img_normalized = img_rgb.astype(np.float32) / 255.0
            
            # Expandir dimensión para batch
            img_batch = np.expand_dims(img_normalized, axis=0)
            
            # Preprocesar para MobileNetV2
            img_prep = tf.keras.applications.mobilenet_v2.preprocess_input(img_batch * 255.0)
            
            return img_prep
            
        except Exception as e:
            print(f"Error en preprocesamiento: {str(e)}")
            return None
    
    def predecir_imagen(self, imagen_file):
        """
        Hace una predicción sobre una imagen
        
        Args:
            imagen_file: Archivo de imagen (FileStorage de Flask)
            
        Returns:
            dict: Resultado de la predicción con probabilidades y clasificación
        """
        if not self.modelo_cargado():
            return None
        
        try:
            # Preprocesar imagen
            img_prep = self.preprocesar_imagen(imagen_file)
            
            if img_prep is None:
                return None
            
            # Hacer predicción
            prediccion = self.modelo.predict(img_prep, verbose=0)
            
            # Probabilidad de exceso (clase 1)
            prob_exceso = float(prediccion[0][0])
            prob_correcta = 1.0 - prob_exceso
            
            # Clase predicha (0: correcta, 1: exceso)
            porcion_correcta = prob_exceso < 0.5
            
            # Confianza (probabilidad de la clase predicha)
            confianza = prob_correcta if porcion_correcta else prob_exceso
            
            resultado = {
                'porcion_correcta': porcion_correcta,
                'probabilidad_correcta': prob_correcta,
                'probabilidad_exceso': prob_exceso,
                'confianza': confianza
            }
            
            return resultado
            
        except Exception as e:
            print(f"Error en predicción: {str(e)}")
            import traceback
            traceback.print_exc()
            return None

