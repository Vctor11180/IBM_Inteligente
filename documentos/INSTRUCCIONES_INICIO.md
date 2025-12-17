# 🚀 Instrucciones para Iniciar el Proyecto

## ⚠️ IMPORTANTE: Necesitas DOS Terminales

El backend y el frontend deben correr **AL MISMO TIEMPO** en **TERMINALES SEPARADAS**.

---

## ✅ Paso a Paso

### 1. Terminal 1 - Backend (MANTENER ABIERTA)

```powershell
# Activa el entorno virtual
.venv\Scripts\Activate.ps1

# Inicia el backend
python backend/app.py
```

**⚠️ NO CIERRES ESTA TERMINAL** - El backend debe seguir corriendo.

**Deberías ver:**
```
✅ Modelo cargado correctamente
📡 Servidor corriendo en: http://localhost:5000
 * Running on http://127.0.0.1:5000
```

---

### 2. Terminal 2 - Frontend (NUEVA TERMINAL)

**Abre una NUEVA terminal de PowerShell** (mantén la primera abierta)

```powershell
# Ve a la carpeta del proyecto
cd D:\PROYECTOS\ia_web3

# Ve a la carpeta frontend
cd frontend

# Inicia el servidor frontend
python -m http.server 8000
```

**⚠️ NO CIERRES ESTA TERMINAL TAMPOCO** - El frontend debe seguir corriendo.

**Deberías ver:**
```
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

---

### 3. Abre el Navegador

Abre tu navegador en:
```
http://localhost:8000
```

---

## 🔄 Resumen Visual

```
Terminal 1 (Backend)          Terminal 2 (Frontend)         Navegador
────────────────────          ─────────────────────         ──────────
.venv activado                cd frontend                   http://localhost:8000
python backend/app.py    →    python -m http.server 8000 →   ✅ App funcionando
     ↓                               ↓
[Corriendo...]              [Corriendo...]
     ↓                               ↓
http://localhost:5000       http://localhost:8000
```

---

## ✅ Verificación

Si todo está bien:

1. ✅ Terminal 1 muestra: "Servidor corriendo en: http://localhost:5000"
2. ✅ Terminal 2 muestra: "Serving HTTP on 0.0.0.0 port 8000"
3. ✅ Navegador muestra la aplicación NutriLife
4. ✅ Puedes usar la calculadora de IMC
5. ✅ Puedes analizar imágenes

---

## ❌ Errores Comunes

### Error: "Error al conectar con el servidor"
**Causa:** El backend no está corriendo o lo cerraste.

**Solución:**
1. Verifica que la Terminal 1 tenga el backend corriendo
2. Debe mostrar "Servidor corriendo en: http://localhost:5000"
3. Si lo cerraste (Ctrl+C), inícialo de nuevo

### Error: "ModuleNotFoundError: No module named 'dotenv'"
**Causa:** No estás en el entorno virtual.

**Solución:**
```powershell
# Asegúrate de activar el .venv primero
.venv\Scripts\Activate.ps1

# Luego inicia el backend
python backend/app.py
```

### Error: "Address already in use"
**Causa:** El puerto ya está en uso.

**Solución:**
1. Cierra la terminal que tiene el proceso corriendo
2. O cambia el puerto en el código

---

## 🎯 Estado Correcto

**Cuando todo está funcionando, deberías tener:**

✅ 2 terminales abiertas (una para backend, una para frontend)  
✅ Backend corriendo en http://localhost:5000  
✅ Frontend corriendo en http://localhost:8000  
✅ Navegador mostrando la aplicación  

---

## 💡 Tip

Puedes usar el script automatizado:
```powershell
.\iniciar_todo.bat
```

Este script abre ambas terminales automáticamente, pero es mejor usar terminales separadas para ver los logs de cada servicio.

