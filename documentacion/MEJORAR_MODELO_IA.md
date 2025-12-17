# 📸 Guía: Mejorar el Sistema de Análisis de IA

## 🎯 Objetivo

Mejorar la precisión del modelo de clasificación de porciones de comida recopilando más imágenes de entrenamiento y organizándolas correctamente.

**Estado Actual:**
- Accuracy: 55.56% (aceptable para dataset pequeño)
- Imágenes de entrenamiento: 17 (muy pocas)
- Imágenes de validación: 9

**Objetivo:**
- Accuracy: >80% (bueno)
- Imágenes de entrenamiento: 100-200+ (ideal)
- Imágenes de validación: 30-50

---

## 📊 ¿Por Qué Necesitas Más Imágenes?

### Problema Actual

El modelo actual tiene una precisión del 55.56%, lo que significa:
- ❌ Casi la mitad de las veces se equivoca
- ❌ No detecta bien los platos rebalsados (tu problema reportado)
- ❌ Poca confianza en las predicciones

### Solución

Más imágenes de entrenamiento = Modelo más preciso:
- ✅ Detecta mejor los patrones
- ✅ Diferencia mejor entre porción correcta y exceso
- ✅ Mayor confianza en las predicciones
- ✅ Mejor detección de platos rebalsados

---

## 📸 Tipos de Imágenes que Necesitas

### 1. Porción Correcta ✅

**Características:**
- Platos con cantidad adecuada de comida
- La comida no rebalsa del plato
- Porción visualmente "normal" o "saludable"
- Variedad de tipos de comida

**Ejemplos:**
- Plato con porción de arroz normal
- Ensalada bien servida
- Proteína (pollo, pescado) con porción adecuada
- Comida balanceada en plato

**Cantidad recomendada:** 50-100 imágenes

---

### 2. Exceso de Porción ⚠️

**Características:**
- Platos REBALSADOS de comida
- Comida que sobresale del plato
- Porciones excesivamente grandes
- Comida apilada o desbordada

**Ejemplos:**
- Plato rebalsado de arroz
- Montaña de comida
- Platos muy llenos
- Comida que se sale del plato

**Cantidad recomendada:** 50-100 imágenes

---

## 🎨 Características Importantes de las Imágenes

### ✅ Lo que SÍ debes incluir:

1. **Variedad de Tipos de Comida:**
   - Arroz, pasta, papas
   - Carnes (pollo, res, pescado)
   - Ensaladas y verduras
   - Platos combinados
   - Comida típica de tu región

2. **Diferentes Ángulos:**
   - Vista desde arriba (90°) - MEJOR
   - Vista oblicua (45°)
   - Vista lateral (si es relevante)

3. **Diferentes Tipos de Platos:**
   - Platos planos
   - Platos hondos
   - Platos de diferentes tamaños

4. **Diferentes Condiciones de Luz:**
   - Luz natural (día)
   - Luz artificial (interior)
   - Diferentes horas del día

5. **Diferentes Fondos:**
   - Mesa de cocina
   - Restaurante
   - Mesa común
   - Superficie clara/oscura

---

### ❌ Lo que NO debes incluir:

1. **Imágenes borrosas o de mala calidad**
   - No se pueden analizar bien

2. **Imágenes muy oscuras o muy claras**
   - Dificultan el análisis

3. **Múltiples platos en una imagen**
   - El modelo espera un solo plato

4. **Platos vacíos o casi vacíos**
   - No son relevantes para el problema

5. **Imágenes con muchos elementos adicionales**
   - Utensilios, servilletas, etc. pueden confundir

6. **Comida que no es visible o está tapada**
   - Debe ser fácil ver la cantidad

---

## 📁 Estructura de Carpetas

### Organización Actual:

```
entrenamiento/
├── Porcion_correcta/
│   ├── 1.jpg
│   ├── 2.jpg
│   └── ...
└── Exceso_porcion/
    ├── a.jpg
    ├── b.jpg
    └── ...

validacion/
├── Porcioncorrecta/
│   ├── v1.jpg
│   └── ...
└── Porcionexceso/
    ├── va.jpg
    └── ...
```

### Recomendación para Nuevas Imágenes:

```
entrenamiento/
├── Porcion_correcta/
│   ├── 1.jpg
│   ├── 2.jpg
│   ├── ... (hasta 100+ imágenes)
│   ├── arroz_normal_1.jpg
│   ├── ensalada_1.jpg
│   ├── pollo_porcion_1.jpg
│   └── ...
└── Exceso_porcion/
    ├── a.jpg
    ├── b.jpg
    ├── ... (hasta 100+ imágenes)
    ├── arroz_rebalsado_1.jpg
    ├── plato_lleno_1.jpg
    ├── exceso_carne_1.jpg
    └── ...
```

**Nomenclatura recomendada:** `tipo_comida_descripcion_numero.jpg`

---

## 📊 Distribución Recomendada

### Dataset Ideal:

| Tipo | Entrenamiento | Validación | Total |
|------|---------------|------------|-------|
| Porción Correcta | 70-80 | 20-25 | 90-105 |
| Exceso | 70-80 | 20-25 | 90-105 |
| **TOTAL** | **140-160** | **40-50** | **180-210** |

### Distribución Mínima (Mejora Significativa):

| Tipo | Entrenamiento | Validación | Total |
|------|---------------|------------|-------|
| Porción Correcta | 40-50 | 10-15 | 50-65 |
| Exceso | 40-50 | 10-15 | 50-65 |
| **TOTAL** | **80-100** | **20-30** | **100-130** |

**Regla de oro:** 80% entrenamiento, 20% validación

---

## 📸 Proceso de Recolección de Imágenes

### Paso 1: Planificación

1. **Decide tu meta:** ¿100 imágenes? ¿200 imágenes?
2. **Planifica las sesiones:** No intentes hacerlo todo en un día
3. **Prepara tu espacio:** Buena iluminación, superficie limpia

### Paso 2: Toma de Fotos

**Para cada comida:**

1. **Prepara el plato:**
   - Usa platos normales (no muy pequeños ni muy grandes)
   - Sirve la comida normalmente

2. **Toma la foto:**
   - **Vista desde arriba es la mejor** (90°)
   - Asegúrate de que toda la comida esté visible
   - Buena iluminación
   - Enfoca bien la imagen

3. **Clasifica inmediatamente:**
   - ¿Es porción correcta? → `Porcion_correcta/`
   - ¿Es exceso? → `Exceso_porcion/`
   - **IMPORTANTE:** Sé honesto con la clasificación

### Paso 3: Organización

1. **Revisa las fotos:**
   - Elimina las borrosas
   - Elimina las muy oscuras/claras
   - Verifica que la clasificación sea correcta

2. **Renombra las imágenes:**
   - Usa nombres descriptivos
   - Ejemplo: `arroz_normal_1.jpg`, `plato_rebalsado_2.jpg`

3. **Organiza en carpetas:**
   - Mueve a `entrenamiento/` o `validacion/`
   - Recuerda: 80% entrenamiento, 20% validación

---

## 🎯 Criterios de Clasificación

### Porción Correcta ✅

**Se considera correcta cuando:**
- La comida no rebalsa del plato
- La cantidad parece "normal" o "saludable"
- Hay espacio visible entre la comida y el borde del plato
- La porción es visualmente apropiada

**Ejemplos:**
- Plato con arroz que ocupa ~40-60% del plato
- Ensalada servida normalmente
- Proteína con acompañantes balanceados

### Exceso de Porción ⚠️

**Se considera exceso cuando:**
- La comida **REBALSA** del plato
- La comida está **muy apilada** o en montaña
- No hay espacio entre la comida y el borde del plato
- La cantidad es claramente **excesiva**

**Ejemplos:**
- Plato rebalsado de comida
- Montaña de arroz que se sale del plato
- Comida apilada hasta el borde

---

## 💡 Consejos para Mejorar el Dataset

### 1. Diversidad es Clave

No todas las imágenes deben ser del mismo tipo:
- ✅ Variedad de comidas
- ✅ Variedad de platos
- ✅ Variedad de ángulos
- ✅ Variedad de iluminación

### 2. Balance es Importante

Asegúrate de tener aproximadamente el mismo número de:
- Porciones correctas vs. Excesos
- Diferentes tipos de comida en cada categoría

### 3. Calidad sobre Cantidad

- ✅ 100 imágenes buenas > 200 imágenes malas
- ✅ Enfócate en imágenes claras y bien clasificadas

### 4. Casos Difíciles

Incluye casos "limítrofes":
- Porciones que están "casi" rebalsadas
- Porciones que están "casi" correctas
- Esto ayuda al modelo a aprender mejor los límites

---

## 🔄 Proceso de Reentrenamiento

### Después de Recolectar las Imágenes:

1. **Organiza las carpetas:**
   ```
   entrenamiento/
   ├── Porcion_correcta/ (70-80 imágenes)
   └── Exceso_porcion/ (70-80 imágenes)
   
   validacion/
   ├── Porcioncorrecta/ (20-25 imágenes)
   └── Porcionexceso/ (20-25 imágenes)
   ```

2. **Preprocesa los datos:**
   ```bash
   python scripts/preprocesamiento.py
   ```

3. **Entrena el modelo:**
   ```bash
   python scripts/entrenar_modelo.py
   ```

4. **Verifica las métricas:**
   - Accuracy debería mejorar (>80% ideal)
   - Revisa la matriz de confusión
   - Prueba con imágenes nuevas

5. **Reemplaza el modelo:**
   - El nuevo modelo se guardará en `modelos/modelo_porciones.keras`
   - Reemplazará al modelo anterior automáticamente

---

## 📊 Métricas Esperadas Después de Mejorar

### Con 80-100 imágenes de entrenamiento:
- Accuracy: 70-75% (mejora significativa)
- Mejor detección de excesos
- Más confianza en predicciones

### Con 140-160 imágenes de entrenamiento:
- Accuracy: 80-85% (muy bueno)
- Excelente detección de excesos
- Alta confianza en predicciones
- Mejor en casos difíciles

### Con 200+ imágenes de entrenamiento:
- Accuracy: 85-90%+ (excelente)
- Detección casi perfecta
- Muy alta confianza
- Funciona bien en casi todos los casos

---

## ✅ Checklist de Recolección

### Antes de Empezar:
- [ ] Entiendo qué es "porción correcta" vs. "exceso"
- [ ] Tengo un plan para tomar las fotos
- [ ] Sé dónde guardar las imágenes

### Durante la Recolección:
- [ ] Tomo fotos desde arriba (mejor ángulo)
- [ ] Buena iluminación
- [ ] Imágenes enfocadas y claras
- [ ] Clasifico inmediatamente (correcta o exceso)
- [ ] Variedad de tipos de comida
- [ ] Balance entre correctas y excesos

### Después de Recolectar:
- [ ] Reviso todas las imágenes (elimino las malas)
- [ ] Verifico que la clasificación sea correcta
- [ ] Organizo en carpetas (80% entrenamiento, 20% validación)
- [ ] Renombro las imágenes con nombres descriptivos
- [ ] Cuento las imágenes para verificar balance

### Antes de Reentrenar:
- [ ] Tengo al menos 80-100 imágenes totales
- [ ] Balance aproximado entre clases
- [ ] Imágenes organizadas correctamente
- [ ] Carpetas `entrenamiento/` y `validacion/` listas

---

## 🎯 Resumen Ejecutivo

**Para mejorar significativamente el modelo:**

1. **Recolecta:** 80-100+ imágenes de calidad
2. **Distribuye:** 80% entrenamiento, 20% validación
3. **Balance:** Mismo número de "correctas" y "excesos"
4. **Variedad:** Diferentes tipos de comida, ángulos, iluminación
5. **Calidad:** Imágenes claras, enfocadas, bien clasificadas

**Resultado esperado:**
- Accuracy: 70-80%+ (vs. 55.56% actual)
- Mejor detección de platos rebalsados
- Mayor confianza en las predicciones

---

## 📝 Notas Finales

- **No te apresures:** Mejor 100 imágenes buenas que 200 malas
- **Sé consistente:** Usa los mismos criterios para clasificar
- **Revisa regularmente:** Verifica que tus imágenes sean correctas
- **Itera:** Después de entrenar, prueba y ajusta según sea necesario

**¡Buena suerte con la recolección de imágenes! 📸**

