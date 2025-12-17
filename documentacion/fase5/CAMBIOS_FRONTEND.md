# 🔧 Cambios Necesarios en Frontend para Fase 5 (Blockchain)

## 📋 Análisis del index.html Actual

El `index.html` actual tiene:
- ✅ 4 secciones principales (IMC, Recomendaciones, Analizar, NutriBot)
- ✅ Navegación con botones en el header
- ✅ Integración con backend para análisis
- ✅ Visualización de resultados de IPFS (CID)
- ❌ NO tiene integración con MetaMask
- ❌ NO tiene conexión a blockchain
- ❌ NO tiene funcionalidad para guardar en blockchain

---

## 🎯 Cambios Necesarios

### 1. Agregar Librerías Web3

**En el `<head>` de index.html:**

```html
<!-- Agregar antes de styles.css -->
<script src="https://cdn.ethers.io/lib/ethers-5.7.2.umd.min.js"></script>
<!-- O usar Web3.js -->
<!-- <script src="https://cdn.jsdelivr.net/npm/web3@latest/dist/web3.min.js"></script> -->
```

**Recomendación:** Usar **Ethers.js** (más moderno y fácil de usar)

---

### 2. Agregar Indicador de Wallet en el Header

**En el `<header>` (después de la navegación):**

```html
<header class="topbar">
    <div class="brand">
        <div class="logo">🍃</div>
        <span>NutriLife</span>
    </div>

    <nav>
        <!-- Botones de navegación existentes -->
        <button class="nav-btn active" onclick="mostrarVista('imc')">Calculadora IMC</button>
        <button class="nav-btn" onclick="mostrarVista('reco')">Recomendaciones</button>
        <button class="nav-btn" onclick="mostrarVista('analizar')">📷 Analizar Comida</button>
        <button class="nav-btn" onclick="mostrarVista('bot')">NutriBot</button>
        <!-- NUEVO: Botón para historial blockchain -->
        <button class="nav-btn" onclick="mostrarVista('historial')">📜 Historial</button>
    </nav>

    <!-- NUEVO: Indicador de Wallet -->
    <div class="wallet-status" id="walletStatus">
        <button class="wallet-btn" id="walletBtn" onclick="toggleWallet()">
            🔗 Conectar Wallet
        </button>
        <div class="wallet-info hidden" id="walletInfo">
            <span class="wallet-address" id="walletAddress"></span>
            <button class="disconnect-btn" onclick="desconectarWallet()">Desconectar</button>
        </div>
    </div>
</header>
```

---

### 3. Agregar Botón "Guardar en Blockchain" en Resultados

**En la función `mostrarResultados()` (después de mostrar IPFS):**

```html
<!-- Después del cuadro de IPFS, agregar: -->
<div class="blockchain-section" id="blockchainSection" style="display: none;">
    <div class="blockchain-info">
        <h4>🔗 Guardar en Blockchain</h4>
        <p>Guarda este análisis de forma permanente e inmutable en la blockchain</p>
        
        <div class="gas-info">
            <small>Costo estimado: <span id="gasEstimate">~$0.01</span> (Polygon)</small>
        </div>
        
        <button class="primary-btn" id="btnGuardarBlockchain" onclick="guardarEnBlockchain()">
            💾 Guardar en Blockchain
        </button>
        
        <div class="tx-status hidden" id="txStatus">
            <p>⏳ Transacción pendiente...</p>
            <a href="#" id="txLink" target="_blank">Ver en explorador</a>
        </div>
    </div>
</div>
```

**Lógica JavaScript:**
```javascript
// Después de mostrar resultados IPFS, mostrar sección blockchain
if (result.ipfs && result.ipfs.cid) {
    document.getElementById('blockchainSection').style.display = 'block';
    
    // Guardar datos para usar después
    window.resultadoActual = result;
}
```

---

### 4. Nueva Sección: Historial de Blockchain

**Nueva sección en index.html (después de `vista-bot`):**

```html
<!-- Vista Historial -->
<section id="vista-historial" class="hidden">
    <div class="bot-header">
        <div class="bot-icon">📜</div>
        <h2>Historial de Análisis</h2>
        <p>Todos tus análisis guardados en blockchain</p>
    </div>

    <div class="historial-container" id="historialContainer">
        <div class="loading-state" id="historialLoading">
            <div class="spinner"></div>
            <p>Cargando historial desde blockchain...</p>
        </div>

        <div class="historial-list" id="historialList">
            <!-- Los análisis se cargarán aquí dinámicamente -->
        </div>

        <div class="empty-state hidden" id="historialVacio">
            <p>No tienes análisis guardados en blockchain aún.</p>
            <p>Analiza una imagen y guárdala para comenzar tu historial.</p>
        </div>
    </div>
</div>
```

---

### 5. Funciones JavaScript Necesarias

**Nuevo archivo: `frontend/js/blockchain.js` (o agregar al final de index.html):**

```javascript
// =============================
// BLOCKCHAIN / WEB3 FUNCTIONS
// =============================

let walletAddress = null;
let provider = null;
let signer = null;
let contract = null;

// Dirección del Smart Contract (se actualizará después del deploy)
const CONTRACT_ADDRESS = "0x..."; // Se actualiza después de deployar
const CONTRACT_ABI = [...]; // ABI del contrato

// Detectar MetaMask
function detectarMetaMask() {
    if (typeof window.ethereum !== 'undefined') {
        return true;
    }
    return false;
}

// Conectar Wallet
async function conectarWallet() {
    if (!detectarMetaMask()) {
        alert('MetaMask no está instalado. Por favor, instálalo desde https://metamask.io');
        return false;
    }

    try {
        provider = new ethers.providers.Web3Provider(window.ethereum);
        await provider.send("eth_requestAccounts", []);
        signer = provider.getSigner();
        walletAddress = await signer.getAddress();

        // Actualizar UI
        document.getElementById('walletBtn').classList.add('hidden');
        document.getElementById('walletInfo').classList.remove('hidden');
        document.getElementById('walletAddress').textContent = 
            `${walletAddress.substring(0, 6)}...${walletAddress.substring(38)}`;

        // Inicializar contrato
        contract = new ethers.Contract(CONTRACT_ADDRESS, CONTRACT_ABI, signer);

        return true;
    } catch (error) {
        console.error('Error conectando wallet:', error);
        alert('Error al conectar wallet: ' + error.message);
        return false;
    }
}

// Desconectar Wallet
function desconectarWallet() {
    walletAddress = null;
    provider = null;
    signer = null;
    contract = null;
    
    document.getElementById('walletBtn').classList.remove('hidden');
    document.getElementById('walletInfo').classList.add('hidden');
}

// Toggle Wallet (conectar/desconectar)
async function toggleWallet() {
    if (walletAddress) {
        desconectarWallet();
    } else {
        await conectarWallet();
    }
}

// Guardar análisis en Blockchain
async function guardarEnBlockchain() {
    if (!walletAddress) {
        const conectado = await conectarWallet();
        if (!conectado) return;
    }

    if (!window.resultadoActual || !window.resultadoActual.ipfs) {
        alert('No hay análisis disponible para guardar');
        return;
    }

    try {
        const resultado = window.resultadoActual;
        const analisis = resultado.analisis;
        const recomendacion = resultado.recomendacion;
        const ipfs = resultado.ipfs;

        // Mostrar estado de carga
        document.getElementById('txStatus').classList.remove('hidden');
        document.getElementById('btnGuardarBlockchain').disabled = true;

        // Preparar datos
        const datosAnalisis = {
            cidIPFS: ipfs.cid,
            porcionCorrecta: analisis.porcion_correcta,
            confianza: Math.round(analisis.confianza * 100), // Convertir a 0-100
            calorias: recomendacion.calorias_estimadas,
            timestamp: Math.floor(Date.now() / 1000) // Unix timestamp
        };

        // Llamar al Smart Contract
        const tx = await contract.guardarAnalisis(
            datosAnalisis.cidIPFS,
            datosAnalisis.porcionCorrecta,
            datosAnalisis.confianza,
            datosAnalisis.calorias
        );

        // Esperar confirmación
        const receipt = await tx.wait();

        // Actualizar UI con éxito
        document.getElementById('txStatus').innerHTML = `
            <p>✅ Guardado exitosamente en blockchain</p>
            <a href="https://polygonscan.com/tx/${receipt.transactionHash}" target="_blank">
                Ver transacción
            </a>
        `;

        console.log('Transacción confirmada:', receipt.transactionHash);

    } catch (error) {
        console.error('Error guardando en blockchain:', error);
        document.getElementById('txStatus').innerHTML = 
            `<p>❌ Error: ${error.message}</p>`;
        document.getElementById('btnGuardarBlockchain').disabled = false;
    }
}

// Obtener historial desde Blockchain
async function cargarHistorial() {
    if (!walletAddress) {
        document.getElementById('historialVacio').classList.remove('hidden');
        return;
    }

    try {
        document.getElementById('historialLoading').classList.remove('hidden');
        
        // Llamar al Smart Contract
        const analisis = await contract.obtenerAnalisisUsuario(walletAddress);

        // Renderizar historial
        const historialList = document.getElementById('historialList');
        historialList.innerHTML = '';

        if (analisis.length === 0) {
            document.getElementById('historialVacio').classList.remove('hidden');
        } else {
            analisis.forEach((item, index) => {
                const div = document.createElement('div');
                div.className = 'historial-item';
                div.innerHTML = `
                    <div class="historial-header">
                        <span>Análisis #${index + 1}</span>
                        <small>${new Date(item.timestamp * 1000).toLocaleDateString()}</small>
                    </div>
                    <div class="historial-content">
                        <p>CID IPFS: <code>${item.cidIPFS}</code></p>
                        <p>Porción: ${item.porcionCorrecta ? '✅ Correcta' : '⚠️ Exceso'}</p>
                        <p>Confianza: ${item.confianza}%</p>
                        <p>Calorías: ${item.calorias} kcal</p>
                        <a href="https://gateway.pinata.cloud/ipfs/${item.cidIPFS}" target="_blank">
                            Ver imagen
                        </a>
                    </div>
                `;
                historialList.appendChild(div);
            });
        }

        document.getElementById('historialLoading').classList.add('hidden');
    } catch (error) {
        console.error('Error cargando historial:', error);
        document.getElementById('historialLoading').classList.add('hidden');
        document.getElementById('historialVacio').classList.remove('hidden');
    }
}
```

---

### 6. Actualizar función mostrarVista()

**Modificar para incluir la nueva vista:**

```javascript
function mostrarVista(vista) {
    // Oculta todas las vistas
    document.querySelectorAll("section[id^='vista-']")
        .forEach(v => v.classList.add("hidden"));

    // Muestra la vista seleccionada
    document.getElementById("vista-" + vista).classList.remove("hidden");

    // Si es la vista de historial, cargar datos
    if (vista === 'historial') {
        cargarHistorial();
    }

    // Quita clase active de todos los botones
    document.querySelectorAll(".nav-btn").forEach(b => b.classList.remove("active"));

    // Añade clase active al botón correspondiente
    const btn = document.querySelector(`.nav-btn[onclick="mostrarVista('${vista}')"]`);
    if (btn) btn.classList.add("active");
}
```

---

### 7. Estilos CSS Necesarios

**Agregar a `styles.css`:**

```css
/* Wallet Status */
.wallet-status {
    display: flex;
    align-items: center;
    gap: 12px;
}

.wallet-btn {
    background: linear-gradient(135deg, #6366f1, #8b5cf6);
    color: white;
    border: none;
    padding: 8px 16px;
    border-radius: 8px;
    cursor: pointer;
    font-size: 14px;
    font-weight: 500;
}

.wallet-info {
    display: flex;
    align-items: center;
    gap: 12px;
}

.wallet-address {
    background: #f3f4f6;
    padding: 8px 12px;
    border-radius: 6px;
    font-family: monospace;
    font-size: 13px;
}

.disconnect-btn {
    background: #ef4444;
    color: white;
    border: none;
    padding: 6px 12px;
    border-radius: 6px;
    cursor: pointer;
    font-size: 12px;
}

/* Blockchain Section */
.blockchain-section {
    background: #f0f9ff;
    border: 1px solid #0ea5e9;
    border-radius: 12px;
    padding: 20px;
    margin-top: 20px;
}

.blockchain-info h4 {
    margin: 0 0 8px 0;
    color: #0c4a6e;
}

.gas-info {
    margin: 12px 0;
    color: #64748b;
    font-size: 13px;
}

.tx-status {
    margin-top: 12px;
    padding: 12px;
    background: #fef3c7;
    border-radius: 8px;
    color: #92400e;
}

.tx-status a {
    color: #0284c7;
    text-decoration: none;
}

/* Historial */
.historial-container {
    max-width: 900px;
    margin: 0 auto;
}

.historial-list {
    display: grid;
    gap: 16px;
    margin-top: 20px;
}

.historial-item {
    background: white;
    border-radius: 12px;
    padding: 20px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.historial-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 12px;
    padding-bottom: 12px;
    border-bottom: 1px solid #e5e7eb;
}

.historial-content p {
    margin: 8px 0;
    color: #4b5563;
}

.historial-content code {
    background: #f3f4f6;
    padding: 4px 8px;
    border-radius: 4px;
    font-size: 12px;
}

.empty-state {
    text-align: center;
    padding: 40px;
    color: #6b7280;
}
```

---

## 📊 Resumen de Cambios

### Archivos a Modificar:
1. ✅ `frontend/index.html`
   - Agregar librería Ethers.js
   - Agregar indicador de wallet en header
   - Agregar botón "Guardar en Blockchain"
   - Agregar sección de historial
   - Agregar funciones JavaScript

2. ✅ `frontend/styles.css`
   - Estilos para wallet
   - Estilos para sección blockchain
   - Estilos para historial

### Archivos Nuevos (Opcional):
- `frontend/js/blockchain.js` - Funciones blockchain separadas
- `frontend/js/contract-config.js` - Configuración del contrato (dirección, ABI)

---

## ✅ Checklist de Implementación

- [ ] Agregar librería Ethers.js
- [ ] Agregar indicador de wallet en header
- [ ] Implementar función `conectarWallet()`
- [ ] Implementar función `guardarEnBlockchain()`
- [ ] Agregar botón "Guardar en Blockchain" en resultados
- [ ] Crear sección de historial
- [ ] Implementar función `cargarHistorial()`
- [ ] Agregar estilos CSS
- [ ] Agregar botón "Historial" en navegación
- [ ] Testing con MetaMask
- [ ] Testing con Smart Contract deployado

---

## 🎯 Cambios Mínimos Esenciales

Si quieres hacerlo paso a paso, los cambios mínimos son:

1. **Agregar Ethers.js** en el `<head>`
2. **Agregar botón de wallet** en el header
3. **Implementar `conectarWallet()`**
4. **Agregar botón "Guardar"** después de mostrar resultados IPFS
5. **Implementar `guardarEnBlockchain()`** básica

El historial puede venir después en una iteración.

---

**Nota:** Estos cambios se implementarán después de:
1. Desarrollar el Smart Contract
2. Deployarlo a testnet
3. Obtener la dirección del contrato y el ABI

