# ⚠️ DEPRECADO: Guía: Deployar a Goerli Testnet desde Remix

## ⚠️ IMPORTANTE: Goerli está Deprecado

**Esta guía está deprecada. Goerli testnet ya no recibe soporte oficial.**

**Por favor, usa la guía actualizada:** `DEPLOY_SEPOLIA_GUIA.md`

Goerli ha sido reemplazado por **Sepolia** como testnet recomendado.

## 📊 Estado Actual

✅ Contrato deployado en **VM de Remix** (para pruebas locales)
- Dirección: `0xd9145CCE52D386f254917e481eB44e9943F39138`

⏳ **Siguiente:** Deployar a **Goerli Testnet** (red real de prueba)

---

## 🔍 Diferencia: VM de Remix vs Goerli Testnet

### VM de Remix (Lo que tienes ahora):
- ✅ Funciona solo en Remix
- ✅ No requiere wallet
- ✅ Gratis e instantáneo
- ❌ NO es una red real
- ❌ No se puede usar desde el frontend
- ❌ Se pierde al recargar Remix

### Goerli Testnet (Lo que necesitas):
- ✅ Red de prueba real de Ethereum
- ✅ Se puede usar desde el frontend
- ✅ Necesita MetaMask
- ✅ Necesita ETH de prueba (gratis)
- ✅ Permanece deployado permanentemente

---

## 🎯 Pasos para Deployar en Goerli Testnet

### Paso 1: Instalar y Configurar MetaMask

**Si no tienes MetaMask:**
1. Instala MetaMask desde: https://metamask.io
2. Crea una wallet
3. **Guarda bien tu frase de recuperación**

**Si ya tienes MetaMask:**
1. Abre MetaMask
2. En la parte superior, haz clic en la red actual
3. Busca "Goerli test network"
4. Si no aparece:
   - Haz clic en "Show/hide test networks"
   - Activa "Show test networks"
   - Busca "Goerli test network" y selecciónala

---

### Paso 2: Obtener ETH de Prueba (Goerli)

**Necesitas ETH de prueba para pagar gas fees (es gratis, solo de prueba)**

#### Opción 1: Goerli Faucet (Recomendado)
1. Ve a: https://goerlifaucet.com/
2. Conecta tu wallet de MetaMask
3. Selecciona la red "Goerli"
4. Haz clic en "Request 0.05 ETH"
5. Espera unos minutos
6. Verifica en MetaMask que recibiste el ETH

#### Opción 2: Alchemy Faucet
1. Ve a: https://www.alchemy.com/faucets/ethereum-goerli
2. Conecta tu wallet
3. Solicita ETH de prueba
4. Verifica en MetaMask

#### Opción 3: QuickNode Faucet
1. Ve a: https://faucet.quicknode.com/ethereum/goerli
2. Ingresa tu dirección de wallet
3. Solicita ETH

**Cantidad necesaria:** ~0.05 ETH de prueba es suficiente para deployar y hacer varias transacciones

---

### Paso 3: Conectar MetaMask con Remix

1. **En Remix:**
   - Ve a la pestaña "Deploy & Run Transactions" (panel izquierdo)

2. **En "ENVIRONMENT":**
   - Actualmente dice "Remix VM (Berlin)" o similar
   - Cambia a: **"Injected Provider - MetaMask"**
   - Esto conectará Remix con tu MetaMask

3. **MetaMask se abrirá:**
   - Te pedirá permisos para conectar
   - Haz clic en "Next" y luego "Connect"

4. **Verifica:**
   - En Remix, deberías ver tu dirección de wallet
   - Verifica que estés en "Goerli" network

---

### Paso 4: Deployar el Contrato

1. **En Remix, panel "Deploy & Run Transactions":**
   - Deberías ver "Injected Provider - MetaMask"
   - Tu dirección de wallet debería aparecer
   - Asegúrate de que dice "network: Goerli"

2. **Selecciona el contrato:**
   - En "CONTRACT", selecciona: **"NutriLife - prueba.sol"**

3. **Haz clic en "Deploy"**
   - MetaMask se abrirá
   - Te mostrará una transacción para confirmar

4. **Confirma en MetaMask:**
   - Revisa el "Gas fee" (debería ser bajo, ~0.001-0.01 ETH)
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
   ADDRESS: "0xTuNuevaDireccionDeGoerli", // Dirección en Goerli
   ```

---

## ✅ Verificación

### Verificar en Etherscan:

1. Ve a: https://goerli.etherscan.io
2. Pega la dirección de tu contrato
3. Deberías ver:
   - Transacción de creación
   - Estado del contrato
   - Código (si verificaste el contrato)

---

## 🎯 Después del Deploy en Goerli

Una vez deployado en Goerli, tendrás:

1. ✅ Contrato en red real de prueba
2. ✅ Dirección del contrato
3. ✅ ABI ya guardado
4. ✅ Listo para integrar en frontend

**Siguiente paso:** Integrar en el frontend (agregar funciones de blockchain)

---

## ⚠️ Notas Importantes

1. **ETH de Prueba:**
   - Solo funciona en Goerli
   - NO tiene valor real
   - Se puede obtener gratis de faucets

2. **Gas Fees:**
   - En Goerli son muy bajos (prácticamente gratis)
   - En Mainnet cuestan dinero real

3. **Dirección del Contrato:**
   - Cada deploy genera una nueva dirección
   - La dirección de VM de Remix NO funciona en Goerli
   - Necesitas la nueva dirección después de deployar en Goerli

---

## 🆘 Problemas Comunes

### MetaMask no aparece en Remix:
- Verifica que MetaMask esté instalado y desbloqueado
- Refresca Remix
- Asegúrate de seleccionar "Injected Provider - MetaMask"

### No tengo ETH de prueba:
- Usa uno de los faucets mencionados
- Puede tardar unos minutos en llegar

### Error "insufficient funds":
- Necesitas más ETH de prueba
- Solicita más en un faucet

### La transacción está pendiente mucho tiempo:
- Es normal, puede tardar 1-2 minutos
- Espera a que se confirme

---

## ✅ Checklist

- [ ] MetaMask instalado
- [ ] MetaMask configurado con Goerli
- [ ] ETH de prueba obtenido
- [ ] Remix conectado con MetaMask
- [ ] Contrato deployado en Goerli
- [ ] Nueva dirección del contrato guardada
- [ ] Contrato verificado en Etherscan (opcional)

---

**¿Listo para deployar en Goerli? Sigue estos pasos y me dices si tienes algún problema! 🚀**

