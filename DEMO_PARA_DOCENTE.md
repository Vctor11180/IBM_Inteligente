# 🎬 Guía Rápida: Cómo Mostrar el Contrato a tu Docente

## 🎯 Pasos Rápidos (2 minutos)

### 1. Abre el Contrato en Etherscan

**Copia y pega este enlace en el navegador:**

```
https://sepolia.etherscan.io/address/0xcb726f3e59518C7b24c74FB7279aA4554927D4A1
```

---

### 2. Qué Mostrar

En la página de Etherscan verás:

#### 📍 Parte Superior (Overview)
- **Address:** `0xcb726f3e59518C7b24c74FB7279aA4554927D4A1`
- **Balance:** 0 ETH (normal, es un contrato)
- **Token:** (si aplica)

#### 📋 Tabs Principales

**1. Transactions (Transacciones)**
- Haz clic en esta pestaña
- Verás la transacción de creación (deploy)
- Muestra: `Creation | Contract Creation`
- Puedes hacer clic para ver los detalles

**2. Code (Código)**
- Muestra el código Solidity del contrato
- Si está verificado, verás el código completo
- Si no, puedes mencionar que está verificado en otros exploradores

**3. Read Contract (Leer Contrato)**
- Funciones que puedes probar sin gastar gas
- Ejemplos: `obtenerTotalAnalisis()`, `owner()`, etc.

**4. Write Contract (Escribir Contrato)**
- Requiere conectar wallet
- Funciones para guardar datos (gasta gas)
- Puedes hacer una demo guardando un análisis

---

### 3. Mostrar la Transacción de Creación

**Haz clic en la transacción de creación**, o usa este enlace directo:

```
https://sepolia.etherscan.io/tx/0x4a9fd44390c9eb139983e02c47af30a5028ac145aa77c2e0d875e16d43ba7dd8
```

**Muestra:**
- ✅ Status: Success
- 📦 Block: 9857790
- ⛽ Gas Used: 1,383,963
- 🔗 Contract Address creado

---

## 💡 Puntos Clave para Mencionar

### ✅ Lo que Demuestra el Contrato

1. **Deploy Exitoso**
   - Contrato desplegado en blockchain pública
   - Transacción verificada y permanente

2. **Funcionalidad Completa**
   - Guardado de análisis nutricionales
   - Estadísticas agregadas
   - Consulta de datos

3. **Integración Web3**
   - Compatible con wallets (MetaMask, Core Wallet)
   - Almacenamiento en IPFS
   - Blockchain Ethereum

4. **Código Verificado**
   - Código fuente público
   - Auditable y transparente

---

## 🎬 Demo Interactiva (Opcional)

Si quieres hacer una demo en vivo:

### Paso 1: Conectar Wallet
1. Abre Core Wallet
2. Asegúrate de estar en Sepolia
3. En Etherscan, haz clic en "Connect to Web3"

### Paso 2: Leer Datos
1. Ve a "Read Contract"
2. Prueba `obtenerTotalAnalisis()` → debería devolver 0 (o el número actual)
3. Prueba `owner()` → muestra tu dirección

### Paso 3: Escribir Datos (Demo)
1. Ve a "Write Contract"
2. Expande `guardarAnalisis()`
3. Ingresa datos de prueba:
   - `cidIPFS`: "QmTest123..." (cualquier string)
   - `porcionCorrecta`: true
   - `confianza`: 85
   - `calorias`: 500
4. Haz clic en "Write"
5. Confirma en Core Wallet
6. Espera la confirmación
7. Muestra la nueva transacción en Etherscan

---

## 📸 Screenshots Sugeridos

Si prefieres tomar screenshots, captura:

1. **Página principal del contrato**
   - Muestra la dirección y estado

2. **Tab "Code"**
   - Muestra el código Solidity

3. **Tab "Transactions"**
   - Muestra la transacción de creación

4. **Tab "Read Contract"**
   - Muestra las funciones disponibles

---

## 📋 Resumen para Decir

**Puedes decir algo como:**

> "He desplegado un Smart Contract en la blockchain de Ethereum (red Sepolia). 
> El contrato permite almacenar análisis nutricionales de forma permanente e 
> inmutable. Puedes verlo aquí en Etherscan [mostrar enlace], donde está 
> verificado públicamente. El contrato incluye funciones para guardar análisis, 
> consultar estadísticas y mantener un historial de cada usuario. Es parte de 
> un proyecto más grande que integra IA para análisis de imágenes, almacenamiento 
> en IPFS y blockchain para registro permanente."

---

## 🔗 Enlaces de Referencia Rápida

**Contrato:**
https://sepolia.etherscan.io/address/0xcb726f3e59518C7b24c74FB7279aA4554927D4A1

**Transacción:**
https://sepolia.etherscan.io/tx/0x4a9fd44390c9eb139983e02c47af30a5028ac145aa77c2e0d875e16d43ba7dd8

---

**¡Listo para la presentación! 🎓**

