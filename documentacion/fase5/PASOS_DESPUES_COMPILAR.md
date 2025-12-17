# ✅ Pasos Después de Compilar el Contrato

## 🎉 ¡Contrato Compilado Exitosamente!

Si Remix compiló sin errores, el contrato está listo. Ahora necesitas:

---

## 📋 Checklist de Próximos Pasos

### 1. ✅ Obtener el ABI del Contrato

En Remix, después de compilar:
- Haz clic en **"ABI"** (abajo del panel)
- Copia el JSON completo
- Guárdalo en un archivo: `frontend/js/NutriLifeABI.json`

**O también puedes:**
- Ir a la carpeta de compilación de Remix
- Buscar el archivo `.json` del contrato
- Copiar el campo `abi`

---

### 2. 🚀 Deployar a Testnet

#### Opción A: Deploy desde Remix (Más Fácil)

**Paso 1: Configurar MetaMask**
1. Abre MetaMask
2. Cambia a red de prueba:
   - **Sepolia Testnet** (recomendado - Goerli está deprecado)
   - O **Holesky Testnet**

**Paso 2: Obtener ETH de Prueba**
- Ve a un faucet de Sepolia:
  - Sepolia: https://sepoliafaucet.com/ (recomendado)
  - Alchemy: https://www.alchemy.com/faucets/ethereum-sepolia
- Conecta tu wallet
- Solicita ETH de prueba

**Paso 3: Deploy en Remix**
1. En Remix, ve a la pestaña **"Deploy & Run Transactions"**
2. Selecciona **"Injected Provider - MetaMask"**
3. **IMPORTANTE:** Verifica que MetaMask esté en **"Sepolia"** (no Goerli)
4. Selecciona tu contrato **"NutriLife"**
5. Haz clic en **"Deploy"**
6. Confirma la transacción en MetaMask
7. Espera la confirmación

**Paso 4: Guardar Dirección del Contrato**
- Después del deploy, Remix mostrará la dirección del contrato
- Copia esta dirección (ejemplo: `0x1234...`)
- Actualiza `frontend/js/contract-config.js`:
  ```javascript
  ADDRESS: "0xTuDireccionDeSepolia",
  NETWORK: { name: "sepolia", chainId: 11155111 }
  ```

---

#### Opción B: Deploy con Hardhat (Avanzado)

Si prefieres usar Hardhat:
1. Sigue la guía en `IMPLEMENTACION_ETHEREUM.md`
2. Configura Hardhat
3. Ejecuta: `npx hardhat run scripts/deploy.js --network goerli`

---

### 3. 📝 Crear Archivo de Configuración para Frontend

**Crear:** `frontend/js/contract-config.js`

```javascript
// Configuración del Smart Contract
const CONTRACT_CONFIG = {
    // Dirección del contrato deployado (actualizar después del deploy)
    ADDRESS: "0x...", // Reemplazar con tu dirección
    
    // ABI del contrato (copiar de Remix)
    ABI: [
        // ... pegar el ABI completo aquí
    ],
    
    // Red (testnet o mainnet)
    NETWORK: {
        name: "goerli", // o "sepolia", "mainnet"
        chainId: 5 // Goerli: 5, Sepolia: 11155111, Mainnet: 1
    }
};
```

---

### 4. 🔗 Integrar en Frontend

Después de obtener la dirección y ABI:

1. **Agregar Ethers.js** al `index.html`
2. **Agregar botón de wallet** (ver `CAMBIOS_FRONTEND.md`)
3. **Agregar función para guardar en blockchain**
4. **Agregar sección de historial**

Ver guía completa en: `documentacion/fase5/CAMBIOS_FRONTEND.md`

---

### 5. 🧪 Probar el Contrato

**En Remix:**
1. Después del deploy, expande el contrato en "Deployed Contracts"
2. Prueba las funciones:
   - `guardarAnalisis()` - Ingresa datos de prueba
   - `obtenerAnalisis()` - Verifica que se guardó
   - `obtenerEstadisticasUsuario()` - Verifica estadísticas

**En el Frontend:**
- Conecta wallet
- Analiza una imagen
- Haz clic en "Guardar en Blockchain"
- Verifica que se guarde correctamente

---

## ✅ Estado Actual

- [x] Contrato escrito
- [x] Contrato compilado en Remix
- [ ] ABI copiado y guardado
- [ ] Contrato deployado a testnet
- [ ] Dirección del contrato guardada
- [ ] Integrado en frontend
- [ ] Probado end-to-end

---

## 🎯 Siguiente Paso Inmediato

**Ahora mismo deberías:**

1. **Deployar a Goerli Testnet desde Remix**
   - Conectar MetaMask
   - Seleccionar Goerli
   - Deploy
   - Guardar dirección

2. **O copiar el ABI** si ya lo tienes listo

3. **Preparar para integrar en frontend**

---

## 📚 Documentación de Referencia

- `CAMBIOS_FRONTEND.md` - Qué cambiar en el frontend
- `IMPLEMENTACION_ETHEREUM.md` - Guía completa de deployment
- `DISENO_SMART_CONTRACT.md` - Diseño del contrato

---

**¿Ya deployaste el contrato a testnet? Si no, ese es el siguiente paso! 🚀**

