"""
Script para hacer predicciones con el modelo entrenado.

Permite analizar una imagen individual y obtener la clasificación
de porción correcta vs. exceso.
"""

import os
import sys
import numpy as np
import tensorflow as tf
from tensorflow import keras
import cv2
import argparse
from PIL import Image

class PredictorPorciones:
    """Clase para hacer predicciones con el modelo entrenado."""
    
    def __init__(self, ruta_modelo='modelos/modelo_porciones.keras'):
        """
        Inicializa el predictor.
        
        Args:
            ruta_modelo: Ruta al modelo entrenado
        """
        self.ruta_modelo = ruta_modelo
        self.model = None
        self.img_size = (224, 224)
        self.classes = {0: 'Porción Correcta', 1: 'Exceso de Porción'}
        
        # Cargar modelo
        self.cargar_modelo()
    
    def cargar_modelo(self):
        """Carga el modelo entrenado."""
        try:
            print(f"Cargando modelo desde: {self.ruta_modelo}")
            self.model = keras.models.load_model(self.ruta_modelo)
            print("✓ Modelo cargado correctamente")
        except Exception as e:
            print(f"Error cargando el modelo: {str(e)}")
            sys.exit(1)
    
    def preprocesar_imagen(self, ruta_imagen):
        """
        Preprocesa una imagen para la predicción.
        
        Args:
            ruta_imagen: Ruta a la imagen a analizar
            
        Returns:
            numpy array: Imagen preprocesada
        """
        # Cargar imagen
        img = cv2.imread(ruta_imagen)
        
        if img is None:
            raise ValueError(f"No se pudo cargar la imagen: {ruta_imagen}")
        
        # Convertir BGR a RGB
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        # Redimensionar
        img = cv2.resize(img, self.img_size)
        
        # Normalizar
        img = img.astype(np.float32) / 255.0
        
        # Expandir dimensión para batch
        img = np.expand_dims(img, axis=0)
        
        # Preprocesar para MobileNetV2
        img_prep = tf.keras.applications.mobilenet_v2.preprocess_input(img * 255.0)
        
        return img_prep
    
    def predecir(self, ruta_imagen):
        """
        Hace una predicción sobre una imagen.
        
        Args:
            ruta_imagen: Ruta a la imagen a analizar
            
        Returns:
            dict: Diccionario con los resultados de la predicción
        """
        # Preprocesar imagen
        img_prep = self.preprocesar_imagen(ruta_imagen)
        
        # Hacer predicción
        prediccion = self.model.predict(img_prep, verbose=0)
        
        # Probabilidad de exceso
        prob_exceso = float(prediccion[0][0])
        prob_correcta = 1.0 - prob_exceso
        
        # Clase predicha
        clase_predicha = 1 if prob_exceso > 0.5 else 0
        nombre_clase = self.classes[clase_predicha]
        
        # Confianza
        confianza = prob_exceso if clase_predicha == 1 else prob_correcta
        
        resultado = {
            'clase': nombre_clase,
            'clase_codigo': clase_predicha,
            'probabilidad_correcta': prob_correcta,
            'probabilidad_exceso': prob_exceso,
            'confianza': confianza,
            'ruta_imagen': ruta_imagen
        }
        
        return resultado
    
    def imprimir_resultado(self, resultado):
        """Imprime los resultados de forma legible."""
        print("\n" + "=" * 50)
        print("RESULTADO DEL ANÁLISIS")
        print("=" * 50)
        print(f"\nImagen: {resultado['ruta_imagen']}")
        print(f"\nClasificación: {resultado['clase']}")
        print(f"Confianza: {resultado['confianza']:.2%}")
        print(f"\nProbabilidades:")
        print(f"  - Porción Correcta: {resultado['probabilidad_correcta']:.2%}")
        print(f"  - Exceso de Porción: {resultado['probabilidad_exceso']:.2%}")
        print("=" * 50 + "\n")


def main():
    """Función principal para ejecutar desde línea de comandos."""
    parser = argparse.ArgumentParser(
        description='Analizar una imagen de comida para determinar si la porción es correcta o excesiva'
    )
    parser.add_argument(
        'imagen',
        type=str,
        help='Ruta a la imagen a analizar'
    )
    parser.add_argument(
        '--modelo',
        type=str,
        default='modelos/modelo_porciones.keras',
        help='Ruta al modelo entrenado (default: modelos/modelo_porciones.keras)'
    )
    
    args = parser.parse_args()
    
    # Verificar que la imagen existe
    if not os.path.exists(args.imagen):
        print(f"Error: La imagen '{args.imagen}' no existe")
        sys.exit(1)
    
    # Crear predictor
    predictor = PredictorPorciones(ruta_modelo=args.modelo)
    
    # Hacer predicción
    resultado = predictor.predecir(args.imagen)
    
    # Imprimir resultado
    predictor.imprimir_resultado(resultado)
    
    return resultado


if __name__ == "__main__":
    main()

