# ✅ Solución: Instalar Dependencias en .venv

## 🔍 Problema Actual

Las dependencias están instaladas en el sistema global, pero cuando activas el `.venv`, Python busca las dependencias ahí y no las encuentra.

## ✅ Solución Rápida

**Ejecuta estos comandos en orden:**

```powershell
# 1. Activa el entorno virtual
.venv\Scripts\Activate.ps1

# 2. Verifica que estás en .venv (debe mostrar ruta con .venv)
python -c "import sys; print(sys.executable)"

# 3. Instala las dependencias en el .venv
python -m pip install flask flask-cors tensorflow numpy Pillow opencv-python requests

# 4. Verifica que se instalaron
python -c "import flask; import tensorflow; print('✅ Todo OK')"
```

**Nota**: TensorFlow es grande (~500MB), puede tardar varios minutos.

---

## 🚀 Después de Instalar

**Terminal 1 - Backend:**
```powershell
.venv\Scripts\Activate.ps1
python backend/app.py
```

**Terminal 2 - Frontend:**
```powershell
cd frontend
python -m http.server 8000
```

---

## ⚠️ Si Sigue Sin Funcionar

Si después de instalar sigues teniendo el error, prueba:

```powershell
# Activa .venv
.venv\Scripts\Activate.ps1

# Usa pip directamente (sin python -m)
pip install --force-reinstall flask flask-cors tensorflow numpy Pillow opencv-python
```

---

**IMPORTANTE**: Siempre activa el `.venv` antes de ejecutar el backend.

