# 📚 Fase 4: Integración Web3 - IPFS

## 📋 Objetivo

Implementar almacenamiento descentralizado usando IPFS (InterPlanetary File System) para guardar las imágenes analizadas, permitiendo:
- Almacenamiento descentralizado de imágenes
- Inmutabilidad de los datos
- Ownership del usuario sobre sus datos
- Hashes únicos (CID) para cada imagen
- Integración con la blockchain (para Fase 5)

## 🎯 Checklist de la Fase 4

- [x] Configurar cliente IPFS ✅
- [x] Elegir servicio IPFS (Pinata, Infura, o nodo local) ✅ (Pinata)
- [x] Implementar función de subida a IPFS ✅
- [x] Guardar hash IPFS (CID) en el backend ✅
- [x] Modificar endpoint `/analizar-imagen` para subir a IPFS ✅
- [x] Integrar en frontend para mostrar imágenes desde IPFS ✅
- [x] Manejar errores de IPFS ✅
- [x] Documentación de uso ✅
- [ ] Crear endpoint para recuperar imágenes desde IPFS (opcional, no necesario)

## 🌐 ¿Qué es IPFS?

IPFS (InterPlanetary File System) es un sistema de almacenamiento distribuido que:
- Almacena archivos de forma descentralizada
- Cada archivo tiene un hash único (CID - Content Identifier)
- Los archivos son inmutables (no se pueden modificar sin cambiar el hash)
- No depende de un servidor central

**Ver explicación detallada:** `EXPLICACION_IPFS_PINATA.md`

## 🔧 Opciones de Implementación

### Opción 1: Pinata (Recomendado para empezar)
- **Ventajas**: Fácil de usar, API simple, gratis hasta cierto límite
- **Desventajas**: Requiere cuenta, servicio centralizado (gateway)
- **Mejor para**: Prototipos y desarrollo

### Opción 2: Infura IPFS
- **Ventajas**: Similar a Pinata, buen servicio
- **Desventajas**: Requiere cuenta
- **Mejor para**: Desarrollo y producción

### Opción 3: Nodo IPFS Local
- **Ventajas**: Totalmente descentralizado, sin dependencias externas
- **Desventajas**: Más complejo de configurar, requiere mantenimiento
- **Mejor para**: Producción avanzada

### Decisión: Empezar con Pinata
- Más fácil de implementar
- API simple y bien documentada
- Gratis para empezar
- Podemos cambiar a nodo local después

## 📡 Estructura de Implementación

### Backend

1. **Servicio IPFS** (`backend/services/ipfs_service.py`):
   - Configuración de cliente IPFS
   - Función para subir archivos
   - Función para obtener archivos (opcional)

2. **Modificar endpoint `/analizar-imagen`**:
   - Después de analizar la imagen, subirla a IPFS
   - Guardar el CID (hash) en la respuesta
   - Opcional: guardar en base de datos

3. **Nuevo endpoint `/obtener-imagen/:cid`** (opcional):
   - Recuperar imagen desde IPFS usando CID
   - Retornar imagen o URL

### Frontend

1. **Mostrar CID después del análisis**:
   - Mostrar el hash IPFS en los resultados
   - Enlace para ver la imagen en IPFS gateway

2. **Opcional: Guardar historial**:
   - Guardar análisis con sus CIDs en localStorage
   - Mostrar historial de análisis

## 💻 Implementación Técnica

### Instalación de Dependencias

```bash
pip install ipfshttpclient
# O para Pinata:
pip install requests  # Ya instalado
```

### Ejemplo de Código - Pinata

```python
import requests
import json

def subir_a_pinata(archivo, api_key, api_secret):
    url = "https://api.pinata.cloud/pinning/pinFileToIPFS"
    
    headers = {
        'pinata_api_key': api_key,
        'pinata_secret_api_key': api_secret
    }
    
    files = {'file': archivo}
    
    response = requests.post(url, files=files, headers=headers)
    if response.status_code == 200:
        result = response.json()
        return result['IpfsHash']  # CID
    else:
        raise Exception(f"Error subiendo a Pinata: {response.text}")
```

### Ejemplo de Código - IPFS Local

```python
import ipfshttpclient

client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001')

def subir_a_ipfs(archivo):
    result = client.add(archivo)
    return result['Hash']  # CID
```

## 📊 Flujo de Trabajo

```
1. Usuario sube imagen
   ↓
2. Backend analiza imagen con IA
   ↓
3. Backend sube imagen a IPFS
   ↓
4. IPFS retorna CID (hash único)
   ↓
5. Backend guarda CID junto con análisis
   ↓
6. Retorna análisis + CID al frontend
   ↓
7. Frontend muestra resultados + CID
   ↓
8. (Fase 5) CID se guarda en blockchain
```

## 🔐 Seguridad y Privacidad

- **Encriptación**: Las imágenes pueden encriptarse antes de subir a IPFS
- **Acceso**: Por defecto, cualquier persona con el CID puede ver la imagen
- **Control**: El usuario puede decidir qué compartir
- **Privacidad**: Considerar encriptación para datos sensibles

## 📝 Estructura de Datos

### Respuesta del endpoint `/analizar-imagen` (actualizada)

```json
{
  "success": true,
  "analisis": {
    "porcion_correcta": true,
    "confianza": 0.85,
    ...
  },
  "recomendacion": {
    ...
  },
  "ipfs": {
    "cid": "QmXYZ...",
    "url": "https://gateway.pinata.cloud/ipfs/QmXYZ...",
    "timestamp": 1234567890
  }
}
```

## 🧪 Testing

- Probar subida de imágenes a IPFS
- Verificar que el CID se guarda correctamente
- Probar recuperación de imágenes desde IPFS
- Verificar que las imágenes se pueden ver en el gateway

## ⏭️ Siguiente Fase

Una vez completada la Fase 4, pasaremos a la **Fase 5: Integración Web3 - Blockchain** donde guardaremos los CIDs y análisis en la blockchain.

## 📂 Archivos a Crear/Modificar

```
backend/
├── services/
│   ├── ipfs_service.py     # Nuevo servicio IPFS
│   └── ...
├── routes/
│   └── api.py              # Modificar endpoint analizar-imagen
└── config.py               # Configuración (API keys, etc.)

frontend/
└── index.html              # Mostrar CID en resultados
```

## 🔑 Configuración Necesaria

Para usar Pinata, necesitarás:
1. Crear cuenta en https://pinata.cloud
2. Obtener API Key y Secret API Key
3. Configurar en variables de entorno o archivo de configuración

---

**Nota**: Esta fase es independiente del modelo de IA, así que podemos implementarla mientras mejoramos el modelo después.

