# 📦 Instalación de Dependencias

## ⚠️ Error: ModuleNotFoundError: No module named 'flask_cors'

Este error significa que las dependencias no están instaladas en tu entorno virtual.

## 🔧 Solución

### Si estás usando entorno virtual (recomendado):

```bash
# Activa el entorno virtual primero
# En Windows:
.venv\Scripts\Activate.ps1

# O en PowerShell:
& .venv/Scripts/Activate.ps1

# Luego instala las dependencias
pip install -r requirements.txt

# O instala solo lo necesario para el backend:
pip install flask flask-cors
```

### Si NO estás usando entorno virtual:

```bash
pip install -r requirements.txt
```

## ✅ Verificar instalación

Después de instalar, verifica:

```bash
python -c "import flask; import flask_cors; print('✅ Flask instalado:', flask.__version__)"
```

Si ves la versión, está correctamente instalado.

## 🚀 Iniciar la aplicación

Después de instalar las dependencias:

**Terminal 1 - Backend:**
```bash
python backend/app.py
```

**Terminal 2 - Frontend:**
```bash
cd frontend
python -m http.server 8000
```

O usa el script: `iniciar_app.bat` (doble clic)

