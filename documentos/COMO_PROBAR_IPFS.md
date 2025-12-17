# 🧪 Cómo Probar la Subida a IPFS

## ✅ Pasos para Probar

### 1. Asegúrate de que el Backend esté corriendo

**Terminal 1 - Backend:**
```bash
# Activa el entorno virtual
.venv\Scripts\Activate.ps1

# Inicia el backend
python backend/app.py
```

**Deberías ver:**
```
🚀 Iniciando NutriLife Backend API
📡 Servidor corriendo en: http://localhost:5000
```

---

### 2. Inicia el Frontend (en otra terminal)

**Terminal 2 - Frontend:**
```bash
cd frontend
python -m http.server 8000
```

---

### 3. Abre la Aplicación

Abre tu navegador en:
```
http://localhost:8000
```

---

### 4. Sube una Imagen

1. Ve a la sección "Analizar Comida"
2. Haz clic en el área de subida o arrastra una imagen
3. Haz clic en "🔍 Analizar Comida"
4. Espera a que termine el análisis

---

### 5. Verifica que se Subió a IPFS

Después del análisis, deberías ver:

✅ **Si se subió correctamente:**
- Un cuadro azul con el icono 🌐
- Título: "Almacenado en IPFS"
- Un CID (hash único, ejemplo: `QmXYZ123...`)
- Un enlace "🔗 Ver imagen en IPFS →"

✅ **En la consola del backend deberías ver:**
```
✅ Archivo subido a IPFS. CID: QmXYZ123...
```

---

### 6. Verifica en Pinata

1. Ve a https://pinata.cloud
2. Inicia sesión
3. Ve a "Files"
4. Deberías ver tu imagen con el nombre que subiste

---

## ⚠️ Si NO se Sube

### Síntomas:
- No aparece el cuadro azul de IPFS
- No hay CID en los resultados

### Posibles Causas:

1. **Error en el backend** (revisa la consola):
   - Puede decir: "⚠️ No se pudo subir la imagen a IPFS"
   - Revisa los errores en la terminal del backend

2. **JWT de Pinata incorrecto**:
   - Verifica que `backend/.env` tenga el JWT correcto
   - Revisa que el JWT no haya expirado

3. **Error de conexión**:
   - Verifica tu conexión a internet
   - Pinata puede estar temporalmente fuera de servicio

---

## 🔍 Debugging

### Ver logs del backend:

En la terminal donde corre el backend, deberías ver mensajes como:
```
✅ Imagen subida a IPFS con CID: QmXYZ...
```

O errores como:
```
❌ Error al subir a Pinata: 400
Respuesta: {"error":"..."}
```

### Probar directamente con el script de test:

```bash
# Activa .venv
.venv\Scripts\Activate.ps1

# Ejecuta el test
python backend/test_ipfs.py
```

Este script prueba:
1. Si la conexión con Pinata funciona
2. Si se puede subir una imagen de prueba

---

## ✅ Verificación Exitosa

Si todo funciona, deberías ver:

**En el Frontend:**
```
🌐 Almacenado en IPFS
CID: QmXyZ123abc...
🔗 Ver imagen en IPFS →
```

**En el Backend (consola):**
```
✅ Archivo subido a IPFS. CID: QmXyZ123abc...
✅ Imagen subida a IPFS con CID: QmXyZ123abc...
```

**En Pinata (web):**
- Tu imagen aparece en la lista de archivos
- Puedes verla haciendo clic en el enlace del CID

---

## 📝 Nota

Si el análisis funciona pero IPFS falla, el análisis **SIGUE FUNCIONANDO**. Solo no se guardará en IPFS, pero verás el resultado del análisis de todas formas.

