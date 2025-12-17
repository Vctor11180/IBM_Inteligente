# 🔧 Solución Rápida - Error flask_cors

## Problema
```
ModuleNotFoundError: No module named 'flask_cors'
```

Esto pasa porque estás usando un entorno virtual (.venv) pero las dependencias no están instaladas ahí.

## ✅ Solución (2 pasos)

### Paso 1: Activa el entorno virtual

En PowerShell:
```powershell
.venv\Scripts\Activate.ps1
```

O si tienes problemas de permisos:
```powershell
& .venv/Scripts/Activate.ps1
```

**IMPORTANTE**: Debes ver `(.venv)` al inicio de tu línea de comando.

### Paso 2: Instala las dependencias EN EL .venv

**IMPORTANTE**: El backend necesita TensorFlow. Instala todo:

```powershell
python -m pip install flask flask-cors tensorflow numpy Pillow opencv-python requests
```

**Nota**: Usa `python -m pip` para asegurar que se instale en el .venv correcto.
TensorFlow es grande (~500MB), puede tardar varios minutos.

O todas las dependencias:
```powershell
python -m pip install -r requirements.txt
```

## 🚀 Ahora inicia el backend

**Terminal 1 - Backend:**
```powershell
# Asegúrate de que estás en el entorno virtual (debe decir (.venv))
python backend/app.py
```

**Terminal 2 - Frontend:**
```powershell
cd frontend
python -m http.server 8000
```

## ✅ Verificar

Si ves esto, está funcionando:
```
🚀 Iniciando NutriLife Backend API
📡 Servidor corriendo en: http://localhost:5000
```

---

## 💡 Nota importante

**SIEMPRE** activa el entorno virtual antes de ejecutar el backend:
```powershell
.venv\Scripts\Activate.ps1
```

