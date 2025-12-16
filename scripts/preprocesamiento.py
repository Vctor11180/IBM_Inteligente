"""
Script de preprocesamiento de imágenes para el modelo de clasificación
de porciones de comida.

Este script carga las imágenes de las carpetas de entrenamiento y validación,
las redimensiona, normaliza y prepara para el entrenamiento.
"""

import os
import numpy as np
from PIL import Image
import cv2
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

class PreprocesadorImagenes:
    """Clase para preprocesar imágenes de comida."""
    
    def __init__(self, img_size=(224, 224)):
        """
        Inicializa el preprocesador.
        
        Args:
            img_size: Tupla (ancho, alto) para redimensionar imágenes. Default: (224, 224)
        """
        self.img_size = img_size
        self.classes = ['Porcion_correcta', 'Exceso_porcion']
        self.class_labels = {0: 'Porcion_correcta', 1: 'Exceso_porcion'}
        self.label_to_int = {'Porcion_correcta': 0, 'Exceso_porcion': 1}
    
    def cargar_imagen(self, ruta_imagen):
        """
        Carga y preprocesa una imagen individual.
        
        Args:
            ruta_imagen: Ruta completa a la imagen
            
        Returns:
            numpy array: Imagen preprocesada normalizada (0-1)
        """
        try:
            # Cargar imagen
            img = cv2.imread(ruta_imagen)
            
            if img is None:
                print(f"Error: No se pudo cargar la imagen {ruta_imagen}")
                return None
            
            # Convertir BGR a RGB
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            
            # Redimensionar
            img = cv2.resize(img, self.img_size)
            
            # Normalizar a [0, 1]
            img = img.astype(np.float32) / 255.0
            
            return img
            
        except Exception as e:
            print(f"Error procesando {ruta_imagen}: {str(e)}")
            return None
    
    def cargar_dataset(self, carpeta_base='entrenamiento'):
        """
        Carga todas las imágenes de las carpetas de entrenamiento.
        
        Args:
            carpeta_base: Carpeta base que contiene las subcarpetas de clases
            
        Returns:
            X: Array numpy con las imágenes
            y: Array numpy con las etiquetas
        """
        X = []
        y = []
        
        for clase in self.classes:
            carpeta_clase = os.path.join(carpeta_base, clase)
            
            if not os.path.exists(carpeta_clase):
                print(f"Advertencia: No se encontró la carpeta {carpeta_clase}")
                continue
            
            # Obtener etiqueta numérica
            label = self.label_to_int[clase]
            
            # Cargar todas las imágenes de esta clase
            archivos = os.listdir(carpeta_clase)
            archivos_imagen = [f for f in archivos if f.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp'))]
            
            print(f"Cargando {len(archivos_imagen)} imágenes de {clase}...")
            
            for archivo in archivos_imagen:
                ruta_completa = os.path.join(carpeta_clase, archivo)
                img = self.cargar_imagen(ruta_completa)
                
                if img is not None:
                    X.append(img)
                    y.append(label)
        
        X = np.array(X)
        y = np.array(y)
        
        print(f"\nDataset cargado:")
        print(f"  Total de imágenes: {len(X)}")
        print(f"  Forma de X: {X.shape}")
        print(f"  Clases: {np.unique(y, return_counts=True)}")
        
        return X, y
    
    def cargar_validacion(self, carpeta_base='validacion'):
        """
        Carga las imágenes de validación.
        
        Args:
            carpeta_base: Carpeta base que contiene las subcarpetas de validación
            
        Returns:
            X_val: Array numpy con las imágenes de validación
            y_val: Array numpy con las etiquetas de validación
        """
        # Mapeo de nombres de carpetas de validación a clases
        mapeo_validacion = {
            'Porcioncorrecta': 'Porcion_correcta',
            'Porcionexceso': 'Exceso_porcion'
        }
        
        X_val = []
        y_val = []
        
        for carpeta_val, clase in mapeo_validacion.items():
            carpeta_clase = os.path.join(carpeta_base, carpeta_val)
            
            if not os.path.exists(carpeta_clase):
                print(f"Advertencia: No se encontró la carpeta {carpeta_clase}")
                continue
            
            label = self.label_to_int[clase]
            
            archivos = os.listdir(carpeta_clase)
            archivos_imagen = [f for f in archivos if f.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp'))]
            
            print(f"Cargando {len(archivos_imagen)} imágenes de validación de {carpeta_val}...")
            
            for archivo in archivos_imagen:
                ruta_completa = os.path.join(carpeta_clase, archivo)
                img = self.cargar_imagen(ruta_completa)
                
                if img is not None:
                    X_val.append(img)
                    y_val.append(label)
        
        X_val = np.array(X_val)
        y_val = np.array(y_val)
        
        print(f"\nDataset de validación cargado:")
        print(f"  Total de imágenes: {len(X_val)}")
        print(f"  Forma de X_val: {X_val.shape}")
        print(f"  Clases: {np.unique(y_val, return_counts=True)}")
        
        return X_val, y_val
    
    def visualizar_imagenes(self, X, y, n_muestras=4):
        """
        Visualiza algunas imágenes del dataset.
        
        Args:
            X: Array de imágenes
            y: Array de etiquetas
            n_muestras: Número de muestras por clase a visualizar
        """
        fig, axes = plt.subplots(2, n_muestras, figsize=(15, 6))
        fig.suptitle('Muestras del Dataset', fontsize=16)
        
        for clase_idx, clase_nombre in self.class_labels.items():
            indices_clase = np.where(y == clase_idx)[0]
            
            if len(indices_clase) == 0:
                continue
            
            # Tomar n_muestras aleatorias
            indices_muestra = np.random.choice(indices_clase, min(n_muestras, len(indices_clase)), replace=False)
            
            for i, idx in enumerate(indices_muestra):
                img = X[idx]
                axes[clase_idx, i].imshow(img)
                axes[clase_idx, i].set_title(f'{clase_nombre}')
                axes[clase_idx, i].axis('off')
        
        plt.tight_layout()
        plt.savefig('documentacion/muestras_dataset.png', dpi=150, bbox_inches='tight')
        print("Imagen guardada en: documentacion/muestras_dataset.png")
        plt.close()


if __name__ == "__main__":
    # Ejemplo de uso
    print("=" * 50)
    print("PREPROCESAMIENTO DE IMÁGENES")
    print("=" * 50)
    
    # Crear preprocesador
    preprocesador = PreprocesadorImagenes(img_size=(224, 224))
    
    # Cargar dataset de entrenamiento
    print("\n1. Cargando dataset de entrenamiento...")
    X_train, y_train = preprocesador.cargar_dataset('entrenamiento')
    
    # Cargar dataset de validación
    print("\n2. Cargando dataset de validación...")
    X_val, y_val = preprocesador.cargar_validacion('validacion')
    
    # Visualizar algunas imágenes
    print("\n3. Visualizando muestras...")
    if len(X_train) > 0:
        preprocesador.visualizar_imagenes(X_train, y_train, n_muestras=4)
    
    # Guardar arrays preprocesados (opcional, para uso futuro)
    print("\n4. Guardando datos preprocesados...")
    os.makedirs('datos_preprocesados', exist_ok=True)
    np.save('datos_preprocesados/X_train.npy', X_train)
    np.save('datos_preprocesados/y_train.npy', y_train)
    np.save('datos_preprocesados/X_val.npy', X_val)
    np.save('datos_preprocesados/y_val.npy', y_val)
    print("   ✓ Datos guardados en 'datos_preprocesados/'")
    
    print("\n" + "=" * 50)
    print("PREPROCESAMIENTO COMPLETADO")
    print("=" * 50)

