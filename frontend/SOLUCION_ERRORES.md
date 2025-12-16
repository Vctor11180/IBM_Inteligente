# 🔧 Solución de Errores - Frontend

## ❌ Error: "Error al conectar con Colab"

**Problema**: El mensaje de error todavía menciona "Colab" pero ahora usamos backend local.

**Solución**: Ya corregido en el código. El mensaje ahora dice "Error al conectar con el servidor".

---

## ❌ Error: "Failed to fetch" al analizar imagen

Este error puede ocurrir por varias razones:

### 1. El backend no está corriendo

**Solución**: Inicia el backend primero:

```bash
python backend/app.py
```

Deberías ver:
```
🚀 Iniciando NutriLife Backend API
📡 Servidor corriendo en: http://localhost:5000
```

### 2. Usando file:/// (protocolo de archivo)

**Problema**: Los navegadores bloquean peticiones CORS cuando abres el archivo directamente con `file:///`.

**Solución**: Usa un servidor local:

#### Opción A: Python (Recomendado)
```bash
cd frontend
python -m http.server 8000
```
Luego abre: `http://localhost:8000`

#### Opción B: Node.js (si tienes npm)
```bash
cd frontend
npx http-server -p 8000
```

#### Opción C: VS Code Live Server
- Instala la extensión "Live Server"
- Click derecho en `index.html` → "Open with Live Server"

### 3. CORS bloqueado

**Problema**: El backend puede no estar permitiendo peticiones desde el frontend.

**Solución**: Verifica que en `backend/app.py` tengas:

```python
CORS(app, origins=["http://localhost:3000", "http://127.0.0.1:5500", "http://localhost:8000", "file://"])
```

---

## ❌ Mensaje: "No tienes datos de IMC"

**Problema**: El usuario intenta analizar una imagen sin calcular su IMC primero.

**Solución**: 
1. **Opción 1**: Calcula tu IMC primero (recomendado)
   - Ve a "Calculadora IMC"
   - Ingresa tus datos
   - Haz clic en "Calcular mi IMC"
   - Los datos se guardan automáticamente

2. **Opción 2**: Usa valores por defecto
   - Haz clic en "Aceptar" cuando aparezca el mensaje
   - Se usarán valores estándar (IMC 22.5, Normal, 2000 kcal)

---

## 🔍 Verificar que todo funcione

### Paso 1: Verifica que el backend esté corriendo
```bash
# En una terminal:
python backend/app.py
```

### Paso 2: Prueba el endpoint directamente
Abre en el navegador o con curl:
```
http://localhost:5000/api/health
```

Deberías ver:
```json
{
  "status": "ok",
  "modelo_cargado": true,
  "version": "1.0.0"
}
```

### Paso 3: Abre el frontend con servidor local
```bash
cd frontend
python -m http.server 8000
```

Abre: `http://localhost:8000`

---

## ✅ Checklist de Solución

- [ ] Backend corriendo en `http://localhost:5000`
- [ ] Frontend abierto con servidor local (no file:///)
- [ ] IMC calculado (opcional pero recomendado)
- [ ] Imagen seleccionada antes de analizar
- [ ] Formato de imagen correcto (JPG, PNG, JPEG)
- [ ] Tamaño de imagen < 10MB

---

## 🐛 Debug

Si sigues teniendo problemas, abre la consola del navegador (F12) y revisa:
- Errores en la consola
- Pestaña "Network" para ver las peticiones
- Verifica que las peticiones lleguen al backend

---

**Nota**: Siempre usa un servidor local para desarrollo. `file:///` tiene muchas limitaciones de seguridad.

