# 🔗 Fase 5: Integración Web3 - Blockchain

## 📋 Objetivo

Implementar almacenamiento de datos nutricionales en blockchain usando Smart Contracts, permitiendo:
- Historial inmutable de análisis nutricionales
- Ownership de datos por parte del usuario
- Registro de CIDs de IPFS en blockchain
- Transparencia y trazabilidad
- Preparación para sistema de recompensas (Fase 6)

---

## 🎯 Checklist de la Fase 5

- [ ] Elegir red blockchain (Ethereum/Polygon)
- [ ] Desarrollo de Smart Contract
- [ ] Tests del Smart Contract
- [ ] Deployment a testnet (Goerli/Mumbai)
- [ ] Integración con MetaMask en frontend
- [ ] Conexión de wallet del usuario
- [ ] Guardado de análisis en blockchain
- [ ] Recuperación de historial desde blockchain
- [ ] Visualización de transacciones
- [ ] Manejo de gas fees

---

## 🌐 Elección de Red Blockchain

### Opción 1: Polygon (Recomendado para empezar) ⭐

**Ventajas:**
- ✅ Gas fees MUY bajos (~$0.001 por transacción)
- ✅ Transacciones rápidas
- ✅ Compatible con Ethereum (mismo código)
- ✅ Perfecto para desarrollo y testing

**Desventajas:**
- ⚠️ Menos descentralizado que Ethereum
- ⚠️ Menor seguridad que Ethereum mainnet

**Mejor para:** Desarrollo, pruebas, aplicaciones con muchas transacciones

---

### Opción 2: Ethereum Mainnet

**Ventajas:**
- ✅ Máxima seguridad y descentralización
- ✅ Red más establecida

**Desventajas:**
- ❌ Gas fees altos ($1-50+ por transacción)
- ❌ Transacciones más lentas
- ❌ Caro para desarrollo

**Mejor para:** Producción final, cuando el proyecto esté completo

---

### Opción 3: Ethereum Goerli (Testnet)

**Ventajas:**
- ✅ Gratis (ETH de prueba)
- ✅ Ideal para desarrollo y testing
- ✅ Mismo comportamiento que mainnet

**Desventajas:**
- ⚠️ Es testnet (no tiene valor real)

**Mejor para:** Desarrollo y pruebas antes de ir a producción

---

### Decisión Recomendada:

**Para Desarrollo:**
1. **Polygon Mumbai (Testnet)** - Gratis, rápido, ideal para probar
2. O **Ethereum Goerli (Testnet)** - Para simular mainnet

**Para Producción (después):**
- **Polygon Mainnet** - Si quieres gas fees bajos
- **Ethereum Mainnet** - Si quieres máxima seguridad

---

## 📜 Smart Contract - Diseño

### Estructura de Datos:

```solidity
struct AnalisisNutricional {
    address usuario;          // Dirección del wallet
    string cidIPFS;           // CID de la imagen en IPFS
    bool porcionCorrecta;     // Resultado del análisis
    uint256 confianza;        // Confianza del modelo (0-100)
    uint256 calorias;         // Calorías estimadas
    uint256 timestamp;        // Fecha/hora del análisis
    string metadata;          // JSON con más datos (opcional)
}
```

### Funciones del Smart Contract:

1. **`guardarAnalisis()`**
   - Guarda un nuevo análisis nutricional
   - Requiere wallet conectado
   - Paga gas fee

2. **`obtenerAnalisisUsuario()`**
   - Obtiene todos los análisis de un usuario
   - Gratis (solo lectura)

3. **`obtenerAnalisis()`**
   - Obtiene un análisis específico por ID
   - Gratis (solo lectura)

4. **Eventos:**
   - `AnalisisGuardado(address usuario, string cid, uint256 timestamp)`

---

## 🔧 Tecnologías Necesarias

### Frontend:
- **Web3.js** o **Ethers.js** - Interacción con blockchain
- **MetaMask** - Wallet del usuario

### Backend (Opcional):
- **Web3.py** - Para operaciones desde el backend
- **Infura/Alchemy** - RPC provider para conectar a blockchain

### Smart Contract:
- **Solidity** - Lenguaje del contrato
- **Hardhat** o **Truffle** - Framework de desarrollo
- **OpenZeppelin** - Librerías de seguridad

---

## 🔄 Flujo de Trabajo

```
1. Usuario sube imagen → Frontend
   ↓
2. Backend analiza con IA → Obtiene resultados
   ↓
3. Backend sube a IPFS → Obtiene CID
   ↓
4. Frontend muestra resultados + CID
   ↓
5. Usuario conecta wallet (MetaMask) → Opcional o automático
   ↓
6. Usuario confirma guardar en blockchain
   ↓
7. Frontend llama al Smart Contract → Guarda datos
   ↓
8. Usuario paga gas fee → Transacción confirmada
   ↓
9. Datos guardados en blockchain (inmutables)
   ↓
10. Frontend muestra confirmación + hash de transacción
```

---

## 📡 Cambios Necesarios en Frontend

### 1. Conectar Wallet (MetaMask)

**Nuevo botón/componente:**
```javascript
// Detectar MetaMask
if (typeof window.ethereum !== 'undefined') {
    // MetaMask instalado
    // Botón para conectar
} else {
    // MetaMask no instalado
    // Mostrar mensaje para instalar
}
```

**Función para conectar:**
```javascript
async function conectarWallet() {
    try {
        const accounts = await window.ethereum.request({
            method: 'eth_requestAccounts'
        });
        return accounts[0]; // Dirección del wallet
    } catch (error) {
        console.error('Error conectando wallet:', error);
    }
}
```

### 2. Guardar en Blockchain

**Después del análisis:**
- Mostrar botón "Guardar en Blockchain"
- Si wallet no conectado, pedir conectar primero
- Mostrar costo de gas estimado
- Confirmar transacción

### 3. Visualizar Historial

**Nueva sección:**
- Historial de análisis guardados
- Mostrar desde blockchain
- Filtrar por usuario
- Mostrar hash de transacciones

### 4. Estado del Wallet

**Indicador visual:**
- Mostrar si wallet está conectado
- Mostrar dirección del wallet (acortada)
- Botón para desconectar

---

## 📁 Estructura de Archivos Necesarios

```
contracts/
├── NutriLife.sol              # Smart Contract principal
└── Migrations.sol             # Migraciones (si usa Truffle)

scripts/
├── deploy.js                  # Script de deployment
└── test.js                    # Tests del contrato

test/
└── NutriLife.test.js          # Tests unitarios

frontend/
├── index.html                 # Modificar: agregar conexión wallet
├── js/
│   ├── web3.js               # Integración con blockchain
│   └── contract.js           # Interacción con Smart Contract
└── styles.css                # Estilos para nuevos componentes
```

---

## 🔐 Seguridad y Consideraciones

### Gas Fees:
- **Polygon:** ~$0.001 por transacción (muy barato)
- **Ethereum Goerli:** Gratis (testnet)
- **Ethereum Mainnet:** $1-50+ (caro)

### Privacidad:
- Los datos están en blockchain (públicos)
- Solo la dirección del wallet identifica al usuario
- Considerar usar direcciones proxy o ZK-proofs para mayor privacidad

### UX:
- Hacer opcional guardar en blockchain
- Mostrar claramente el costo de gas
- Permitir cancelar antes de confirmar

---

## 🧪 Testing

### Testnet:
1. Obtener tokens de prueba (faucet)
2. Deployar contrato en testnet
3. Probar todas las funciones
4. Verificar que todo funcione

### Local (Hardhat):
1. Ejecutar blockchain local
2. Deployar contrato localmente
3. Tests automatizados
4. Debugging fácil

---

## 📊 Integración con IPFS

El Smart Contract guardará:
- **CID de IPFS** (ya tenemos esto de la Fase 4)
- **Resultado del análisis** (porción correcta/exceso)
- **Metadatos** (calorías, confianza, etc.)

**No guarda:**
- La imagen en sí (está en IPFS)
- Solo la referencia (CID)

---

## ⏭️ Siguiente Fase

Después de la Fase 5, la Fase 6 incluirá:
- Dashboard de historial nutricional
- Sistema de recompensas (tokens/NFTs)
- Comparación temporal (evolución)
- Estadísticas y gráficos

---

## 📝 Archivos a Crear/Modificar

### Nuevos:
- `contracts/NutriLife.sol` - Smart Contract
- `scripts/deploy.js` - Deployment script
- `test/NutriLife.test.js` - Tests
- `frontend/js/web3.js` - Integración blockchain
- `frontend/js/contract.js` - Interacción contrato

### Modificar:
- `frontend/index.html` - Agregar conexión wallet, botón guardar en blockchain
- `frontend/styles.css` - Estilos para nuevos componentes
- `package.json` - Agregar dependencias (web3.js, ethers.js)
- `backend/routes/api.py` - Opcional: endpoints para blockchain

---

## 🎯 Decisión: ¿Qué Red Usar?

**Recomendación para empezar:**

1. **Desarrollo/Testing:** Polygon Mumbai Testnet
   - Gratis
   - Rápido
   - Fácil de obtener tokens de prueba

2. **Producción (después):** Polygon Mainnet
   - Gas fees bajos
   - Buen para usuarios
   - Escalable

**Alternativa:** Ethereum Goerli Testnet si prefieres simular Ethereum mainnet.

---

## 💡 Consideraciones de UX

### Opcionalidad:
- Hacer opcional guardar en blockchain
- Algunos usuarios pueden no querer pagar gas fees
- Permitir usar la app sin blockchain

### Información Clara:
- Mostrar costo estimado de gas antes de confirmar
- Explicar qué se guarda en blockchain
- Mostrar beneficios de usar blockchain

---

**Nota**: Esta fase requiere conocimientos básicos de Solidity y Web3, pero es totalmente implementable siguiendo la documentación paso a paso.

