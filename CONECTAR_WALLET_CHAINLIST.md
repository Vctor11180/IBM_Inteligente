# 🔗 Cómo Conectar Wallet en ChainList

## 💡 Aclaración Importante

**ChainList puede sugerirte "Core Wallet", pero NO es necesario.**

Puedes usar **MetaMask** (que es lo que necesitamos para el proyecto).

---

## ✅ Opción 1: Usar MetaMask (Recomendado)

### Paso 1: Buscar Sepolia en ChainList

1. **En ChainList, en la barra de búsqueda:**
   - Escribe: **"Sepolia"**
   - O busca: **"Sepolia Testnet"**

2. **Marca el checkbox:**
   - ✅ **"Include Testnets"** (para que aparezcan las redes de prueba)

### Paso 2: Conectar MetaMask

1. **Busca la tarjeta de "Sepolia"**
   - Debería decir "ChainID: 11155111"
   - Debería decir "Currency: ETH"

2. **Haz clic en "Connect Wallet"**
   - Se abrirá una ventana pidiendo qué wallet usar
   - **Selecciona "MetaMask"**

3. **MetaMask se abrirá:**
   - Te pedirá aprobar la conexión
   - Haz clic en "Next" y luego "Connect"

### Paso 3: Agregar la Red

1. **Después de conectar, ChainList detectará si ya tienes Sepolia:**
   - Si **NO** la tienes, verás un botón **"Add to MetaMask"**
   - Haz clic en ese botón

2. **MetaMask se abrirá:**
   - Te mostrará los detalles de la red Sepolia
   - Haz clic en **"Approve"** o **"Aprobar"**

3. **¡Listo!**
   - Sepolia se agregará a tu MetaMask
   - Cambiará automáticamente a la red Sepolia

---

## 🔍 Si No Ves el Botón "Connect Wallet" con MetaMask

### Alternativa: Agregar Sepolia Manualmente

**Si prefieres agregar Sepolia directamente sin ChainList:**

1. **Abre MetaMask**
2. **Haz clic en el menú de redes** (arriba, donde dice "Ethereum Mainnet")
3. **Haz clic en "Add network" o "Agregar red"**
4. **Haz clic en "Add a network manually" o "Agregar red manualmente"**
5. **Ingresa estos datos:**

```
Network name: Sepolia
New RPC URL: https://rpc.sepolia.org
Chain ID: 11155111
Currency symbol: ETH
Block explorer URL: https://sepolia.etherscan.io
```

6. **Haz clic en "Save" o "Guardar"**

---

## ❓ ¿Core Wallet o MetaMask?

### Core Wallet:
- Es otra wallet de Ethereum
- Funciona, pero NO es necesaria
- Este proyecto está diseñado para MetaMask

### MetaMask (Recomendado):
- ✅ La wallet más popular
- ✅ Compatible con todos los proyectos
- ✅ Fácil de usar
- ✅ Lo que necesitamos para este proyecto

**Conclusión:** Usa **MetaMask**, ignora Core Wallet.

---

## ✅ Verificación

**Para verificar que Sepolia está agregada:**

1. Abre MetaMask
2. Haz clic en el menú de redes (arriba)
3. Deberías ver **"Sepolia"** en la lista
4. Selecciónala

**Deberías ver:**
- Network: Sepolia
- Chain ID: 11155111
- Balance: 0 ETH (todavía no has pedido ETH de prueba)

---

## 🎯 Siguiente Paso

Una vez que tengas Sepolia en MetaMask:

1. **Obtén ETH de prueba:**
   - Ve a: https://sepoliafaucet.com/
   - Conecta MetaMask
   - Solicita 0.5 ETH

2. **Luego deploya el contrato en Remix**

---

## 🆘 Problemas Comunes

### "No veo MetaMask en la lista de wallets"
- **Solución:** Asegúrate de tener MetaMask instalado y desbloqueado
- Refresca la página de ChainList

### "ChainList me pide Core Wallet"
- **Solución:** Ignóralo, busca el botón "Connect Wallet" y selecciona MetaMask
- O agrega Sepolia manualmente (ver arriba)

### "No encuentro Sepolia en ChainList"
- **Solución:** 
  1. Marca el checkbox "Include Testnets"
  2. Busca "Sepolia" en la barra de búsqueda
  3. O usa el método manual (ver arriba)

---

**¡Usa MetaMask, no necesitas Core Wallet! 🔐**

