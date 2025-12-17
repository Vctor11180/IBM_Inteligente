# 📸 Guía Rápida: Mejorar el Modelo de IA

## 🎯 Objetivo

Mejorar la precisión del modelo actual (55.56%) recopilando más imágenes de entrenamiento.

---

## 📊 Situación Actual

- **Accuracy:** 55.56% (aceptable pero bajo)
- **Imágenes de entrenamiento:** 17 (muy pocas)
- **Problema reportado:** No detecta bien platos rebalsados

---

## ✅ Solución: Más Imágenes

### Meta Recomendada:
- **Mínimo:** 80-100 imágenes totales
- **Ideal:** 140-160 imágenes totales
- **Excelente:** 200+ imágenes totales

### Distribución:
- **80% entrenamiento** (70-80 imágenes por clase)
- **20% validación** (20-25 imágenes por clase)

---

## 📸 Tipos de Imágenes Necesarias

### 1. Porción Correcta ✅ (50-100 imágenes)
- Platos con cantidad adecuada
- Comida NO rebalsa del plato
- Variedad: arroz, ensaladas, proteínas, platos combinados

### 2. Exceso de Porción ⚠️ (50-100 imágenes)
- Platos REBALSADOS de comida
- Comida que sobresale del plato
- Montañas de comida
- Variedad de tipos de comida

---

## 📁 Organización

### Estructura de Carpetas:

```
entrenamiento/
├── Porcion_correcta/
│   ├── 1.jpg (existente)
│   ├── ... (agregar 50-80 imágenes más)
│   └── arroz_normal_1.jpg (nuevo)
│
└── Exceso_porcion/
    ├── a.jpg (existente)
    ├── ... (agregar 50-80 imágenes más)
    └── plato_rebalsado_1.jpg (nuevo)

validacion/
├── Porcioncorrecta/
│   ├── v1.jpg (existente)
│   └── ... (agregar 15-20 imágenes más)
│
└── Porcionexceso/
    ├── va.jpg (existente)
    └── ... (agregar 15-20 imágenes más)
```

---

## 📸 Cómo Tomar las Fotos

### ✅ Mejores Prácticas:

1. **Ángulo:** Vista desde arriba (90°) - MEJOR
2. **Iluminación:** Buena luz (natural o artificial)
3. **Enfoque:** Imagen clara y enfocada
4. **Contenido:** Un solo plato, toda la comida visible
5. **Clasificación:** Decide inmediatamente si es correcta o exceso

### ❌ Evitar:

- Imágenes borrosas
- Muy oscuras o muy claras
- Múltiples platos
- Comida tapada

---

## 🎯 Criterios de Clasificación

### Porción Correcta ✅
- Comida NO rebalsa
- Espacio visible en el borde
- Cantidad "normal"

### Exceso ⚠️
- Comida REBALSA del plato
- Muy apilada o en montaña
- Sin espacio en el borde

**Regla:** Si dudas, clasifica como exceso (mejor ser estricto)

---

## 🔄 Después de Recolectar

### 1. Preprocesar:
```bash
python scripts/preprocesamiento.py
```

### 2. Entrenar:
```bash
python scripts/entrenar_modelo.py
```

### 3. Verificar:
- Accuracy debería mejorar (>70-80%)
- Probar con imágenes nuevas

---

## 📚 Documentación Completa

Para más detalles, consulta:
- **`documentacion/MEJORAR_MODELO_IA.md`** - Guía completa y detallada
- **`documentacion/PLANTILLA_CLASIFICACION.md`** - Plantilla de clasificación

---

## ✅ Checklist Rápido

- [ ] Entiendo qué es "porción correcta" vs. "exceso"
- [ ] Tengo plan para tomar fotos
- [ ] Tomaré fotos desde arriba
- [ ] Clasificaré inmediatamente
- [ ] Buscaré variedad de tipos de comida
- [ ] Mantendré balance (50% correctas, 50% excesos)
- [ ] Organizaré 80% entrenamiento, 20% validación

---

**Meta:** Al menos 80-100 imágenes nuevas para mejorar significativamente el modelo.

**Resultado esperado:** Accuracy 70-80%+ (vs. 55.56% actual)

