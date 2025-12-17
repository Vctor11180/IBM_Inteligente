"""
Servicio para interactuar con IPFS usando Pinata
"""

import os
import json
import requests
from typing import Optional, Dict
from flask import current_app


class IPFSService:
    """Servicio para subir archivos a IPFS usando Pinata"""
    
    def __init__(self, jwt_token: Optional[str] = None):
        """
        Inicializa el servicio IPFS
        
        Args:
            jwt_token: JWT token de Pinata. Si es None, intenta obtenerlo de variables de entorno
        """
        # Intentar obtener JWT de variable de entorno si no se proporciona
        if jwt_token is None:
            jwt_token = os.getenv('PINATA_JWT')
        
        self.jwt_token = jwt_token
        self.pinata_base_url = "https://api.pinata.cloud"
        
        if not self.jwt_token:
            print("⚠️ Advertencia: PINATA_JWT no configurado. Las imágenes no se subirán a IPFS.")
    
    def subir_archivo(self, archivo, nombre_archivo: str = None) -> Optional[Dict]:
        """
        Sube un archivo a IPFS usando Pinata
        
        Args:
            archivo: Archivo a subir (FileStorage de Flask o BytesIO)
            nombre_archivo: Nombre del archivo (opcional)
            
        Returns:
            dict con 'cid' y 'url' si es exitoso, None si falla
        """
        if not self.jwt_token:
            print("❌ Error: JWT token no configurado")
            return None
        
        try:
            url = f"{self.pinata_base_url}/pinning/pinFileToIPFS"
            
            headers = {
                'Authorization': f'Bearer {self.jwt_token}'
            }
            
            # Preparar el archivo para subir
            files = {'file': archivo}
            
            # Metadatos opcionales (como JSON string)
            pinata_metadata = {
                'name': nombre_archivo or 'imagen_analizada',
                'keyvalues': {
                    'tipo': 'analisis_comida',
                    'app': 'nutrilife'
                }
            }
            
            pinata_options = {
                'cidVersion': 1
            }
            
            data = {
                'pinataMetadata': json.dumps(pinata_metadata),
                'pinataOptions': json.dumps(pinata_options)
            }
            
            # Realizar la petición
            response = requests.post(
                url,
                files=files,
                data=data,
                headers=headers,
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                cid = result.get('IpfsHash')
                
                if cid:
                    print(f"✅ Archivo subido a IPFS. CID: {cid}")
                    
                    # URL del gateway de Pinata para acceder al archivo
                    url_gateway = f"https://gateway.pinata.cloud/ipfs/{cid}"
                    
                    return {
                        'cid': cid,
                        'url': url_gateway,
                        'tamanio': result.get('PinSize', 0),
                        'timestamp': result.get('Timestamp', '')
                    }
                else:
                    print("❌ Error: No se recibió CID en la respuesta")
                    return None
            else:
                print(f"❌ Error al subir a Pinata: {response.status_code}")
                print(f"Respuesta: {response.text}")
                return None
                
        except requests.exceptions.Timeout:
            print("❌ Error: Timeout al conectar con Pinata")
            return None
        except requests.exceptions.RequestException as e:
            print(f"❌ Error en la petición a Pinata: {str(e)}")
            return None
        except Exception as e:
            print(f"❌ Error inesperado al subir a IPFS: {str(e)}")
            import traceback
            traceback.print_exc()
            return None
    
    def verificar_conexion(self) -> bool:
        """
        Verifica si la conexión con Pinata funciona
        
        Returns:
            True si la conexión es exitosa, False en caso contrario
        """
        if not self.jwt_token:
            return False
        
        try:
            url = f"{self.pinata_base_url}/data/testAuthentication"
            headers = {'Authorization': f'Bearer {self.jwt_token}'}
            
            response = requests.get(url, headers=headers, timeout=10)
            return response.status_code == 200
        except:
            return False
    
    def obtener_url_imagen(self, cid: str) -> str:
        """
        Obtiene la URL para acceder a una imagen en IPFS usando el CID
        
        Args:
            cid: CID (hash) de la imagen en IPFS
            
        Returns:
            URL completa para acceder a la imagen
        """
        return f"https://gateway.pinata.cloud/ipfs/{cid}"


# Instancia global del servicio
ipfs_service = IPFSService()

