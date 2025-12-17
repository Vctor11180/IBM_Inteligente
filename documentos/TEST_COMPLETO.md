# 🧪 Guía de Prueba Completa

## 🚀 Iniciar Servicios

### Terminal 1 - Backend:

```powershell
# 1. Activa el entorno virtual
.venv\Scripts\Activate.ps1

# 2. Inicia el backend
python backend/app.py
```

**Deberías ver:**
```
🚀 Iniciando NutriLife Backend API
📡 Servidor corriendo en: http://localhost:5000
✅ Modelo cargado correctamente
```

---

### Terminal 2 - Frontend:

```powershell
# En otra terminal, ve a la carpeta frontend
cd frontend

# Inicia el servidor
python -m http.server 8000
```

**Deberías ver:**
```
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

---

## 🌐 Abrir la Aplicación

Abre tu navegador en:
```
http://localhost:8000
```

---

## ✅ Checklist de Pruebas

### 1. ✅ Probar Calculadora de IMC
- [ ] Ir a "Calcular IMC"
- [ ] Ingresar peso y altura
- [ ] Verificar que muestre IMC y categoría
- [ ] Verificar que muestre recomendaciones

### 2. ✅ Probar Análisis de Imagen (Con IPFS)
- [ ] Ir a "Analizar Comida"
- [ ] Subir una imagen (puedes usar `validacion/Porcioncorrecta/v1.jpg`)
- [ ] Hacer clic en "🔍 Analizar Comida"
- [ ] Verificar que aparezcan los resultados del análisis
- [ ] **IMPORTANTE:** Verificar que aparezca el cuadro azul de IPFS con:
  - [ ] 🌐 Icono y "Almacenado en IPFS"
  - [ ] CID (hash único, ejemplo: `QmXYZ123...`)
  - [ ] Enlace "🔗 Ver imagen en IPFS →"
- [ ] Verificar en la consola del backend que aparezca:
  ```
  ✅ Archivo subido a IPFS. CID: QmXYZ123...
  ```

### 3. ✅ Verificar en Pinata (Opcional)
- [ ] Ir a https://pinata.cloud
- [ ] Iniciar sesión
- [ ] Ir a "Files"
- [ ] Verificar que tu imagen esté ahí

### 4. ✅ Probar Chatbot
- [ ] Usar el NutriBot
- [ ] Hacer preguntas como:
  - "¿Cuántas calorías debo comer?"
  - "¿Qué alimentos son buenos para bajar de peso?"
- [ ] Verificar que responda adecuadamente

---

## 🎯 Resultado Esperado

### Si todo funciona correctamente:

✅ **Frontend:**
- Calculadora de IMC funciona
- Análisis de imágenes funciona
- Se muestra información de IPFS (CID)
- Chatbot responde

✅ **Backend (consola):**
```
✅ Modelo cargado correctamente
✅ Archivo subido a IPFS. CID: QmXYZ123...
✅ Imagen subida a IPFS con CID: QmXYZ123...
```

✅ **Pinata:**
- Imágenes visibles en el dashboard
- CID funciona en el gateway

---

## ⚠️ Si Algo No Funciona

### Si no aparece IPFS:
1. Verifica que `backend/.env` exista y tenga el JWT
2. Revisa la consola del backend para errores
3. Verifica tu conexión a internet

### Si el análisis no funciona:
1. Verifica que el modelo esté cargado (mensaje en backend)
2. Verifica que el archivo `modelos/modelo_porciones.keras` exista

### Si hay errores de conexión:
1. Verifica que ambos servicios estén corriendo
2. Verifica que los puertos 5000 y 8000 no estén en uso
3. Revisa la consola del navegador (F12)

---

## 🎉 ¡Todo Listo!

Si todas las pruebas pasan, la Fase 4 está completamente funcional.

