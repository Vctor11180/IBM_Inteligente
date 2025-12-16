# 🧪 Testing de Endpoints - Fase 2

## ¿Por qué es importante el testing?

El testing de endpoints es **MUY IMPORTANTE** porque:

### 1. **Validar que todo funciona correctamente**
   - Asegura que los endpoints respondan como se espera
   - Detecta errores antes de integrar con el frontend
   - Verifica que el modelo de IA se carga y funciona

### 2. **Ahorrar tiempo en debugging**
   - Encuentra problemas temprano
   - Facilita identificar dónde está el error
   - Evita problemas al integrar con el frontend

### 3. **Documentación viva**
   - Muestra cómo usar los endpoints
   - Ejemplos reales de requests y responses
   - Referencia rápida para desarrollo

### 4. **Confianza en producción**
   - Saber que el código funciona antes de desplegar
   - Reducir bugs en producción
   - Mejor experiencia para los usuarios

---

## 📋 Qué debemos probar

### ✅ Endpoints básicos

1. **GET `/api/health`**
   - ✅ Responde correctamente (200)
   - ✅ Retorna estructura JSON esperada
   - ✅ Indica si el modelo está cargado

2. **POST `/api/calcular-imc`**
   - ✅ Calcula IMC correctamente
   - ✅ Retorna categoría correcta
   - ✅ Genera recomendaciones
   - ✅ Rechaza datos incompletos (400)
   - ✅ Funciona con diferentes casos (normal, sobrepeso, etc.)

3. **POST `/api/analizar-imagen`**
   - ✅ Procesa imágenes correctamente
   - ✅ Retorna análisis del modelo IA
   - ✅ Genera recomendaciones personalizadas
   - ✅ Rechaza peticiones sin imagen (400)
   - ✅ Maneja errores de procesamiento

### ✅ Casos de error

- Peticiones sin datos requeridos
- Formatos incorrectos
- Imágenes inválidas
- Datos fuera de rango

---

## 🚀 Cómo ejecutar el testing

### Opción 1: Script automatizado (Recomendado)

He creado un script de testing completo: `backend/test_endpoints.py`

**Pasos:**

1. **Inicia el servidor backend** (en una terminal):
   ```bash
   python backend/app.py
   ```

2. **Ejecuta el script de testing** (en otra terminal):
   ```bash
   python backend/test_endpoints.py
   ```

El script probará automáticamente todos los endpoints y mostrará resultados detallados.

### Opción 2: Pruebas manuales con curl

**Health check:**
```bash
curl http://localhost:5000/api/health
```

**Calcular IMC:**
```bash
curl -X POST http://localhost:5000/api/calcular-imc \
  -H "Content-Type: application/json" \
  -d '{"edad": 25, "peso": 70, "altura": 1.75, "actividad": "Moderada"}'
```

**Analizar imagen:**
```bash
curl -X POST http://localhost:5000/api/analizar-imagen \
  -F "imagen=@validacion/Porcioncorrecta/v1.jpg" \
  -F "imc=22.5" \
  -F "calorias_objetivo=2000" \
  -F "objetivo=mantener peso"
```

### Opción 3: Pruebas con Postman o Insomnia

Puedes importar los endpoints y probarlos manualmente con estas herramientas.

---

## 📊 Resultados esperados

### GET /api/health
```json
{
  "status": "ok",
  "modelo_cargado": true,
  "version": "1.0.0"
}
```

### POST /api/calcular-imc
```json
{
  "imc": 22.86,
  "categoria": "Normal",
  "objetivo": "Mantener peso saludable...",
  "calorias": 2200,
  "desayuno": { ... },
  "almuerzo": { ... },
  ...
}
```

### POST /api/analizar-imagen
```json
{
  "success": true,
  "analisis": {
    "porcion_correcta": true,
    "confianza": 0.85,
    ...
  },
  "recomendacion": {
    "mensaje": "...",
    "calorias_estimadas": 450,
    ...
  }
}
```

---

## 🐛 Solución de problemas comunes

### Error: "No se pudo conectar al servidor"
**Solución**: Asegúrate de que el servidor esté corriendo:
```bash
python backend/app.py
```

### Error: "Modelo NO está cargado"
**Solución**: Verifica que el archivo `modelos/modelo_porciones.keras` exista.

### Error: "ModuleNotFoundError: No module named 'requests'"
**Solución**: Instala requests:
```bash
pip install requests
```

### Error: "Timeout" en analizar-imagen
**Solución**: Es normal que tarde más. El script tiene timeout de 30 segundos.

---

## ✅ Checklist de Testing

Antes de pasar a la Fase 3, asegúrate de:

- [ ] Servidor backend inicia sin errores
- [ ] GET `/api/health` funciona
- [ ] POST `/api/calcular-imc` funciona con datos válidos
- [ ] POST `/api/calcular-imc` rechaza datos inválidos
- [ ] POST `/api/analizar-imagen` procesa imágenes correctamente
- [ ] POST `/api/analizar-imagen` rechaza peticiones sin imagen
- [ ] El modelo de IA se carga correctamente
- [ ] Las recomendaciones se generan correctamente
- [ ] Todos los errores se manejan apropiadamente

---

## 🎯 Conclusión

**SÍ, el testing es muy importante**. Nos permite:

1. ✅ Confirmar que el backend funciona correctamente
2. ✅ Detectar problemas antes de integrar con el frontend
3. ✅ Tener confianza al pasar a la siguiente fase
4. ✅ Documentar el comportamiento esperado

**Tiempo estimado**: 5-10 minutos para ejecutar todas las pruebas.

---

**Recomendación**: Ejecuta el testing ahora antes de continuar con la Fase 3. Esto evitará problemas futuros y te dará confianza de que todo funciona correctamente.

