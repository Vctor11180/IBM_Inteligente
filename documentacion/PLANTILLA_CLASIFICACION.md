# 📋 Plantilla de Clasificación de Imágenes

Usa esta plantilla para clasificar tus imágenes de manera consistente.

---

## ✅ Porción Correcta

### Criterios:
- [ ] La comida NO rebalsa del plato
- [ ] Hay espacio visible entre la comida y el borde del plato
- [ ] La cantidad parece "normal" o "saludable"
- [ ] La porción es visualmente apropiada

### Ejemplos Visuales:

**✅ CORRECTO - Arroz Normal:**
- Arroz ocupa ~40-60% del plato
- No rebalsa
- Espacio visible en el borde

**✅ CORRECTO - Ensalada:**
- Ensalada servida normalmente
- Ingredientes visibles
- No desborda

**✅ CORRECTO - Proteína con Acompañantes:**
- Porción de proteína normal
- Acompañantes balanceados
- Todo dentro del plato

---

## ⚠️ Exceso de Porción

### Criterios:
- [ ] La comida **REBALSA** del plato
- [ ] La comida está **muy apilada** o en montaña
- [ ] NO hay espacio entre la comida y el borde
- [ ] La cantidad es claramente **excesiva**

### Ejemplos Visuales:

**⚠️ EXCESO - Plato Rebalsado:**
- Comida que se sale del plato
- Montaña de comida
- No hay espacio visible

**⚠️ EXCESO - Muy Apilado:**
- Comida apilada hasta el borde
- Cantidad excesiva
- Rebalsa visualmente

**⚠️ EXCESO - Comida Desbordada:**
- Comida que se sale por los lados
- Claramente excesivo
- Más de lo que debería

---

## ❓ Casos Difíciles (Casos Limítrofes)

### Caso 1: "Casi Rebalsado"
**Clasificación:** ⚠️ **Exceso**
- Si está muy cerca del borde y parece excesivo → Exceso
- Mejor clasificar como exceso si hay duda

### Caso 2: "Mucha Comida pero Bien Servida"
**Clasificación:** ✅ **Correcta**
- Si no rebalsa y está bien distribuida → Correcta
- Importa más si rebalsa que la cantidad total

### Caso 3: "Poco Comida pero en Plato Pequeño"
**Clasificación:** ✅ **Correcta**
- Si no rebalsa y la proporción es correcta → Correcta
- El tamaño del plato no define la porción

---

## 📸 Checklist Rápido para Cada Imagen

Antes de guardar una imagen, verifica:

1. **Calidad:**
   - [ ] Imagen clara y enfocada
   - [ ] Buena iluminación
   - [ ] Se ve toda la comida

2. **Clasificación:**
   - [ ] ¿Rebalsa? → ⚠️ Exceso
   - [ ] ¿No rebalsa? → ✅ Correcta
   - [ ] ¿Duda? → ⚠️ Exceso (mejor ser estricto)

3. **Ubicación:**
   - [ ] ¿Entrenamiento o Validación? (80% / 20%)
   - [ ] ¿Carpeta correcta? (`Porcion_correcta/` o `Exceso_porcion/`)

---

## 💡 Regla de Oro

**"Si duda si es exceso, clasifícala como exceso"**

Es mejor tener más ejemplos de exceso que el modelo no detecte bien que tener menos y que siga fallando con platos rebalsados.

