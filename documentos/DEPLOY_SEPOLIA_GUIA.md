# 🚀 Guía: Deployar a Sepolia Testnet (Reemplazo de Goerli)

## ⚠️ IMPORTANTE: Goerli está Deprecado

**Goerli testnet ha sido deprecado oficialmente.**

**Solución:** Usar **Sepolia** (testnet recomendado por Ethereum)

---

## 🎯 ¿Por qué Sepolia?

✅ **Soporte activo** de Ethereum  
✅ **Faucets funcionando** correctamente  
✅ **Transacciones rápidas** y confiables  
✅ **Recomendado oficialmente** por Ethereum  
✅ **Misma funcionalidad** que Goerli  

---

## 📋 Pasos para Deployar en Sepolia

### Paso 1: Configurar MetaMask con Sepolia

**Si Sepolia NO aparece en MetaMask:**

1. **Abre MetaMask**
2. **Haz clic en el menú de redes** (arriba, donde dice "Ethereum Mainnet" o la red actual)
3. **Haz clic en "Add network" o "Agregar red"**
4. **Haz clic en "Add a network manually" o "Agregar red manualmente"**
5. **Ingresa estos datos:**

```
Network name: Sepolia
New RPC URL: https://sepolia.infura.io/v3/YOUR_INFURA_KEY
O usa: https://rpc.sepolia.org
Chain ID: 11155111
Currency symbol: ETH
Block explorer URL: https://sepolia.etherscan.io
```

**O más fácil (usando ChainList):**
- Ve a: https://chainlist.org/
- Marca el checkbox "Include Testnets" (arriba)
- Busca "Sepolia" en la barra de búsqueda
- Haz clic en "Connect Wallet" en la tarjeta de Sepolia
- **Selecciona "MetaMask"** (ignora si te sugiere Core Wallet)
- MetaMask se abrirá, aprueba la conexión
- Luego haz clic en "Add to MetaMask" para agregar la red
- Acepta en MetaMask

**⚠️ Nota:** Si ChainList te sugiere "Core Wallet", ignóralo y selecciona MetaMask directamente.

---

### Paso 2: Obtener ETH de Prueba para Sepolia

**Faucets de Sepolia:**

#### Opción 1: Sepolia Faucet (Recomendado)
1. Ve a: https://sepoliafaucet.com/
2. Conecta tu wallet de MetaMask
3. Haz clic en "Request 0.5 ETH"
4. Espera unos minutos
5. Verifica en MetaMask

#### Opción 2: Alchemy Faucet
1. Ve a: https://www.alchemy.com/faucets/ethereum-sepolia
2. Crea cuenta (gratis) o conéctate con Google
3. Ingresa tu dirección de wallet
4. Solicita 0.5 ETH
5. Verifica en MetaMask

#### Opción 3: QuickNode Faucet
1. Ve a: https://faucet.quicknode.com/ethereum/sepolia
2. Ingresa tu dirección de wallet
3. Solicita ETH de prueba

**Cantidad necesaria:** 0.5 ETH de prueba es más que suficiente

---

### Paso 3: Conectar Remix con tu Wallet

**✅ Nota:** Funciona con **MetaMask**, **Core Wallet**, o cualquier wallet compatible.

1. **En Remix:**
   - Ve a la pestaña "Deploy & Run Transactions" (panel izquierdo)

2. **En "ENVIRONMENT":**
   - Actualmente dice "Remix VM (Berlin)" o similar
   - Cambia a: **"Injected Provider - MetaMask"**
   - ⚠️ Aunque diga "MetaMask", funcionará con Core Wallet también

3. **Tu wallet se abrirá:**
   - Te pedirá permisos para conectar
   - Acepta la conexión

4. **IMPORTANTE - Verifica la red:**
   - En tu wallet (Core Wallet/MetaMask), asegúrate de estar en **"Sepolia"**
   - En Remix, deberías ver "network: Sepolia"

---

### Paso 4: Deployar el Contrato en Sepolia

1. **En Remix, panel "Deploy & Run Transactions":**
   - Deberías ver "Injected Provider - MetaMask" (funciona con Core Wallet también)
   - Tu dirección de wallet debería aparecer
   - **Verifica que dice "network: Sepolia"**

2. **Selecciona el contrato:**
   - En "CONTRACT", selecciona: **"NutriLife - prueba.sol"**

3. **Haz clic en "Deploy"**
   - Tu wallet (Core Wallet/MetaMask) se abrirá
   - Te mostrará una transacción para confirmar
   - Revisa que la red sea "Sepolia"

4. **Confirma en tu wallet:**
   - Revisa el "Gas fee" (debería ser muy bajo, ~0.0001-0.001 ETH)
   - Haz clic en "Confirm"
   - Espera la confirmación (30 segundos - 2 minutos)

5. **Espera la confirmación:**
   - En Remix, verás "creation of NutriLife pending..."
   - Después de confirmarse, verás "✓ Transaction mined and execution succeed"
   - Aparecerá una nueva sección "Deployed Contracts" con tu contrato

---

### Paso 5: Guardar la Nueva Dirección

**Después del deploy exitoso:**

1. En Remix, en "Deployed Contracts", expande tu contrato
2. Verás la dirección completa (ejemplo: `0xAbC123...`)
3. **Copia esta dirección completa**

4. **Actualiza** `frontend/js/contract-config.js`:
   ```javascript
   ADDRESS: "0xTuNuevaDireccionDeSepolia", // Dirección en Sepolia
   NETWORK: {
       name: "sepolia",
       chainId: 11155111
   }
   ```

---

## ✅ Verificación

### Verificar en Etherscan:

1. Ve a: https://sepolia.etherscan.io
2. Pega la dirección de tu contrato
3. Deberías ver:
   - Transacción de creación
   - Estado del contrato
   - Código (si verificaste el contrato)

---

## 📊 Comparación: Sepolia vs Goerli

| Característica | Goerli (Deprecado) | Sepolia (Actual) |
|---------------|-------------------|------------------|
| Estado | ❌ Deprecado | ✅ Activo |
| Faucets | ⚠️ Pueden fallar | ✅ Funcionando |
| Soporte | ❌ No oficial | ✅ Oficial |
| Chain ID | 5 | 11155111 |
| Explorer | goerli.etherscan.io | sepolia.etherscan.io |

---

## 🎯 Después del Deploy en Sepolia

Una vez deployado en Sepolia, tendrás:

1. ✅ Contrato en red de prueba activa
2. ✅ Dirección del contrato
3. ✅ ABI ya guardado
4. ✅ Listo para integrar en frontend

**Siguiente paso:** Integrar en el frontend (agregar funciones de blockchain)

---

## ⚠️ Notas Importantes

1. **ETH de Prueba:**
   - Solo funciona en Sepolia
   - NO tiene valor real
   - Se puede obtener gratis de faucets

2. **Gas Fees:**
   - En Sepolia son muy bajos (prácticamente gratis)
   - En Mainnet cuestan dinero real

3. **Dirección del Contrato:**
   - Cada deploy genera una nueva dirección
   - La dirección de VM de Remix NO funciona en Sepolia
   - Necesitas la nueva dirección después de deployar en Sepolia

---

## 🆘 Problemas Comunes

### MetaMask no muestra Sepolia:
- **Solución:** Agrégala manualmente usando los datos arriba, o usa chainlist.org

### No encuentro faucet de Sepolia:
- **Solución:** Usa https://sepoliafaucet.com o https://www.alchemy.com/faucets/ethereum-sepolia

### La transacción está pendiente mucho tiempo:
- **Solución:** Es normal, puede tardar 1-2 minutos. Espera a que se confirme.

### Error "insufficient funds":
- **Solución:** Necesitas más ETH de prueba. Solicita más en un faucet.

---

## ✅ Checklist

- [ ] MetaMask instalado
- [ ] Sepolia agregada a MetaMask
- [ ] ETH de prueba obtenido (Sepolia)
- [ ] Remix conectado con MetaMask
- [ ] Verificado que está en red "Sepolia"
- [ ] Contrato deployado en Sepolia
- [ ] Nueva dirección del contrato guardada
- [ ] Contrato verificado en Etherscan (opcional)

---

## 📝 Resumen Rápido

1. **Agrega Sepolia a MetaMask** (chainlist.org es fácil)
2. **Obtén ETH de prueba** (sepoliafaucet.com)
3. **Conecta Remix con MetaMask**
4. **Verifica que estés en Sepolia** (no Goerli)
5. **Deploy el contrato**
6. **Guarda la nueva dirección**

---

**¡Listo para deployar en Sepolia! 🚀**

