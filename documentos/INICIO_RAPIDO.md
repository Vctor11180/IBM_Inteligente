# 🚀 Inicio Rápido - NutriLife AI + Web3

## ✅ Iniciar Todo (Opción 1: Script Automático)

**Windows:**
```bash
iniciar_todo.bat
```

Esto abrirá:
- Backend en una ventana (http://localhost:5000)
- Frontend en otra ventana (http://localhost:8000)

---

## ✅ Iniciar Manualmente (Opción 2: Dos Terminales)

### Terminal 1 - Backend:

```powershell
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

### Terminal 2 - Frontend:

```powershell
cd frontend
python -m http.server 8000
```

**Deberías ver:**
```
Serving HTTP on :: port 8000 (http://[::]:8000/) ...
```

---

## 🌐 Abrir la Aplicación

Abre tu navegador en:
```
http://localhost:8000
```

---

## 🧪 Probar Funcionalidad Completa

### 1. Calcular IMC
- Ve a la calculadora de IMC
- Ingresa peso y altura
- Verifica que se muestren recomendaciones

### 2. Analizar Imagen (Con IPFS)
- Ve a "Analizar Comida"
- Sube una imagen
- Haz clic en "🔍 Analizar Comida"
- **Verifica que aparezca el cuadro azul de IPFS con CID**

### 3. Chatbot
- Usa el NutriBot
- Haz algunas preguntas nutricionales

---

## ✅ Verificación IPFS

Después de analizar una imagen, deberías ver:

1. **En el Frontend:**
   - Cuadro azul con 🌐 "Almacenado en IPFS"
   - CID (hash único)
   - Enlace para ver la imagen

2. **En el Backend (consola):**
   ```
   ✅ Archivo subido a IPFS. CID: QmXYZ123...
   ✅ Imagen subida a IPFS con CID: QmXYZ123...
   ```

3. **En Pinata (opcional):**
   - Ve a https://pinata.cloud
   - Inicia sesión
   - Ve a "Files"
   - Deberías ver tu imagen

---

## ⚠️ Problemas Comunes

### Error: "PINATA_JWT no configurado"
**Solución:** Verifica que `backend/.env` exista y tenga el JWT

### Error: "No module named 'flask'"
**Solución:** Activa el entorno virtual:
```bash
.venv\Scripts\Activate.ps1
pip install flask flask-cors python-dotenv requests
```

### El backend no inicia
**Solución:** Verifica que el puerto 5000 no esté en uso

### El frontend no carga
**Solución:** Verifica que el puerto 8000 no esté en uso

---

## 🎯 Estado Actual del Proyecto

✅ **Fase 1**: Modelo IA entrenado
✅ **Fase 2**: Backend API funcionando
✅ **Fase 3**: Frontend integrado
✅ **Fase 4**: IPFS integrado (Pinata)

⏳ **Fase 5**: Blockchain (pendiente)

