# 🧪 Guía: Probar el Flujo Completo

## 🎯 Objetivo

Verificar que toda la aplicación funciona correctamente de extremo a extremo.

---

## ✅ Checklist de Pruebas

### 1. Preparación

- [ ] Backend corriendo en `http://localhost:5000`
- [ ] Frontend corriendo en `http://localhost:8000`
- [ ] Wallet (Core Wallet) abierta y desbloqueada
- [ ] Red Sepolia seleccionada en wallet
- [ ] Tener ETH de prueba en Sepolia (0.05 ETH es suficiente)

---

### 2. Prueba 1: Calcular IMC

**Pasos:**
1. Abre la aplicación en el navegador
2. Ve a "Calculadora IMC"
3. Ajusta edad, peso, altura y nivel de actividad
4. Haz clic en "Calcular mi IMC"

**Resultado esperado:**
- ✅ Muestra IMC calculado
- ✅ Muestra categoría (Normal, Sobrepeso, etc.)
- ✅ Muestra recomendaciones personalizadas
- ✅ Cambia a vista "Recomendaciones"

---

### 3. Prueba 2: Analizar Imagen

**Pasos:**
1. Ve a "📷 Analizar Comida"
2. Sube una imagen de comida (arrastra o haz clic)
3. Espera el análisis

**Resultado esperado:**
- ✅ Muestra vista previa de imagen
- ✅ Muestra estado de carga
- ✅ Muestra resultados del análisis:
  - Porción correcta/exceso
  - Confianza del modelo
  - Calorías estimadas
  - Recomendación personalizada
- ✅ Muestra CID de IPFS
- ✅ Link para ver imagen en IPFS

---

### 4. Prueba 3: Conectar Wallet

**Pasos:**
1. Haz clic en "🔗 Conectar Wallet"
2. Acepta la conexión en Core Wallet
3. Acepta cambiar a Sepolia si lo solicita

**Resultado esperado:**
- ✅ Muestra dirección de wallet (ej: `0xe352...8730`)
- ✅ Botón "Desconectar" visible
- ✅ Wallet conectada en Sepolia

---

### 5. Prueba 4: Guardar en Blockchain

**Pasos:**
1. Después de analizar una imagen
2. Verifica que aparece sección "🔗 Guardar en Blockchain"
3. Haz clic en "💾 Guardar en Blockchain"
4. Confirma la transacción en Core Wallet

**Resultado esperado:**
- ✅ Aparece estado "⏳ Transacción pendiente..."
- ✅ Después de confirmarse: "✅ Guardado exitosamente"
- ✅ Link a Etherscan para ver transacción
- ✅ Transacción visible en Etherscan

---

### 6. Prueba 5: Ver Historial

**Pasos:**
1. Haz clic en "📜 Historial"
2. Espera a que cargue

**Resultado esperado:**
- ✅ Muestra "Cargando historial desde blockchain..."
- ✅ Muestra lista de análisis guardados
- ✅ Cada análisis muestra:
  - Número de análisis
  - Fecha y hora
  - CID IPFS
  - Porción (Correcta/Exceso)
  - Confianza (%)
  - Calorías (kcal)
  - Link para ver imagen en IPFS

---

### 7. Prueba 6: Múltiples Análisis

**Pasos:**
1. Analiza otra imagen
2. Guárdala en blockchain
3. Vuelve al historial

**Resultado esperado:**
- ✅ Aparece nuevo análisis en el historial
- ✅ Ordenado del más reciente al más antiguo
- ✅ Ambos análisis visibles

---

## 🆘 Problemas Comunes y Soluciones

### "Error al conectar con el servidor"
- **Solución:** Verifica que el backend esté corriendo
- Comando: `python backend/app.py`

### "Failed to fetch" al analizar imagen
- **Solución:** Usa servidor local para frontend
- Comando: `cd frontend && python -m http.server 8000`

### "No hay análisis disponible para guardar"
- **Solución:** Primero analiza una imagen
- Debe aparecer CID de IPFS antes de guardar

### "insufficient funds"
- **Solución:** Necesitas más ETH de prueba
- Ve a: https://sepoliafaucet.com/

### "Por favor cambia a la red SEPOLIA"
- **Solución:** Cambia manualmente a Sepolia en Core Wallet
- O acepta el cambio automático cuando aparezca

### El historial está vacío
- **Solución:** Guarda al menos un análisis primero
- Verifica que la transacción se haya confirmado

---

## ✅ Resultado Final Esperado

Después de completar todas las pruebas, deberías tener:

1. ✅ IMC calculado y guardado
2. ✅ Imagen analizada con IA
3. ✅ Imagen almacenada en IPFS
4. ✅ Análisis guardado en blockchain
5. ✅ Historial visible con todos los análisis
6. ✅ Transacciones visibles en Etherscan

---

## 📊 Verificación en Etherscan

Para verificar que todo está funcionando:

1. Ve a: https://sepolia.etherscan.io/address/0xcb726f3e59518C7b24c74FB7279aA4554927D4A1
2. Ve a la pestaña "Read Contract"
3. Prueba `obtenerTotalAnalisis()` - debería mostrar el número de análisis
4. Prueba `obtenerAnalisisUsuario(0xe3527c3c5fA3172E9331D94d3c10614698d08730)` - debería mostrar tus IDs de análisis

---

**¡Una vez completadas todas las pruebas, el proyecto estará completamente verificado! ✅**

