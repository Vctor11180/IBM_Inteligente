"""
Aplicación principal del backend Flask para NutriLife AI + Web3

Inicia el servidor Flask con todos los endpoints configurados.
"""

from flask import Flask
from flask_cors import CORS
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# Importar blueprints
from routes.api import api_bp

def create_app():
    """Crea y configura la aplicación Flask"""
    app = Flask(__name__)
    
    # Configuración CORS para permitir peticiones del frontend
    CORS(app, origins=[
        "http://localhost:3000", 
        "http://127.0.0.1:5500", 
        "http://localhost:8000",
        "http://127.0.0.1:8000",
        "file://"
    ])
    
    # Configuración
    app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024  # 10MB máximo para archivos
    app.config['UPLOAD_FOLDER'] = 'uploads'
    
    # Crear carpeta de uploads si no existe
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    
    # Registrar blueprints
    app.register_blueprint(api_bp, url_prefix='/api')
    
    # Ruta raíz
    @app.route('/')
    def index():
        return {
            "message": "NutriLife AI + Web3 API",
            "version": "1.0.0",
            "status": "running"
        }
    
    return app

if __name__ == '__main__':
    app = create_app()
    print("=" * 60)
    print("🚀 Iniciando NutriLife Backend API")
    print("=" * 60)
    print("📡 Servidor corriendo en: http://localhost:5000")
    print("📚 Documentación API: http://localhost:5000/api/health")
    print("=" * 60)
    app.run(debug=True, host='0.0.0.0', port=5000)

