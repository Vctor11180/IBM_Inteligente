# 📜 Diseño del Smart Contract - NutriLife

## 🎯 Objetivo

Smart Contract para almacenar análisis nutricionales de forma inmutable en blockchain, guardando referencias a imágenes en IPFS y resultados del análisis de IA.

---

## 📊 Estructura de Datos

### Struct: AnalisisNutricional

```solidity
struct AnalisisNutricional {
    address usuario;          // Dirección del wallet del usuario
    string cidIPFS;           // CID (hash) de la imagen en IPFS
    bool porcionCorrecta;     // true = porción correcta, false = exceso
    uint256 confianza;        // Confianza del modelo (0-100)
    uint256 calorias;         // Calorías estimadas
    uint256 timestamp;        // Fecha/hora del análisis (Unix timestamp)
    uint256 idAnalisis;       // ID único del análisis (auto-incremental)
}
```

**Consideraciones:**
- `usuario`: Dirección del wallet que guardó el análisis
- `cidIPFS`: String con el CID de IPFS (ej: "QmXYZ123...")
- `porcionCorrecta`: Boolean simple para el resultado
- `confianza`: Entero de 0-100 (multiplicar por 100 el valor decimal)
- `calorias`: Entero (no decimales para ahorrar gas)
- `timestamp`: Unix timestamp (segundos desde epoch)
- `idAnalisis`: ID único auto-incremental

---

## 🔐 Variables de Estado

```solidity
contract NutriLife {
    // Mapeo: usuario => lista de IDs de análisis
    mapping(address => uint256[]) public analisisPorUsuario;
    
    // Mapeo: ID => análisis completo
    mapping(uint256 => AnalisisNutricional) public analisisPorId;
    
    // Contador para IDs auto-incrementales
    uint256 private contadorAnalisis;
    
    // Eventos
    event AnalisisGuardado(
        address indexed usuario,
        uint256 indexed idAnalisis,
        string cidIPFS,
        bool porcionCorrecta,
        uint256 timestamp
    );
    
    // Owner del contrato (opcional, para funciones administrativas)
    address public owner;
    
    constructor() {
        owner = msg.sender;
        contadorAnalisis = 0;
    }
}
```

---

## 📝 Funciones Principales

### 1. `guardarAnalisis()` - Guardar un nuevo análisis

```solidity
function guardarAnalisis(
    string memory cidIPFS,
    bool porcionCorrecta,
    uint256 confianza,
    uint256 calorias
) public returns (uint256) {
    // Validaciones
    require(bytes(cidIPFS).length > 0, "CID IPFS no puede estar vacio");
    require(confianza <= 100, "Confianza debe ser entre 0 y 100");
    
    // Incrementar contador
    contadorAnalisis++;
    
    // Crear nuevo análisis
    AnalisisNutricional memory nuevoAnalisis = AnalisisNutricional({
        usuario: msg.sender,
        cidIPFS: cidIPFS,
        porcionCorrecta: porcionCorrecta,
        confianza: confianza,
        calorias: calorias,
        timestamp: block.timestamp,
        idAnalisis: contadorAnalisis
    });
    
    // Guardar en storage
    analisisPorId[contadorAnalisis] = nuevoAnalisis;
    analisisPorUsuario[msg.sender].push(contadorAnalisis);
    
    // Emitir evento
    emit AnalisisGuardado(
        msg.sender,
        contadorAnalisis,
        cidIPFS,
        porcionCorrecta,
        block.timestamp
    );
    
    return contadorAnalisis;
}
```

**Características:**
- Pública (cualquiera puede llamar)
- Retorna el ID del análisis guardado
- Valida inputs
- Emite evento para indexación

---

### 2. `obtenerAnalisis()` - Obtener un análisis específico

```solidity
function obtenerAnalisis(uint256 idAnalisis) 
    public 
    view 
    returns (
        address usuario,
        string memory cidIPFS,
        bool porcionCorrecta,
        uint256 confianza,
        uint256 calorias,
        uint256 timestamp
    ) 
{
    AnalisisNutricional memory analisis = analisisPorId[idAnalisis];
    require(analisis.idAnalisis != 0, "Analisis no existe");
    
    return (
        analisis.usuario,
        analisis.cidIPFS,
        analisis.porcionCorrecta,
        analisis.confianza,
        analisis.calorias,
        analisis.timestamp
    );
}
```

**Características:**
- Función `view` (no modifica estado, gratis)
- Retorna todos los datos del análisis
- Verifica que el análisis existe

---

### 3. `obtenerAnalisisUsuario()` - Obtener todos los análisis de un usuario

```solidity
function obtenerAnalisisUsuario(address usuario) 
    public 
    view 
    returns (uint256[] memory) 
{
    return analisisPorUsuario[usuario];
}
```

**Características:**
- Retorna array de IDs
- Después se pueden obtener uno por uno con `obtenerAnalisis()`
- Alternativa: retornar array completo (más gas si son muchos)

---

### 4. `obtenerTodosAnalisisUsuario()` - Versión completa (alternativa)

```solidity
function obtenerTodosAnalisisUsuario(address usuario) 
    public 
    view 
    returns (
        uint256[] memory ids,
        string[] memory cids,
        bool[] memory porcionesCorrectas,
        uint256[] memory confianzas,
        uint256[] memory calorias,
        uint256[] memory timestamps
    ) 
{
    uint256[] memory listaIds = analisisPorUsuario[usuario];
    uint256 cantidad = listaIds.length;
    
    // Inicializar arrays de retorno
    ids = new uint256[](cantidad);
    cids = new string[](cantidad);
    porcionesCorrectas = new bool[](cantidad);
    confianzas = new uint256[](cantidad);
    calorias = new uint256[](cantidad);
    timestamps = new uint256[](cantidad);
    
    // Llenar arrays
    for (uint256 i = 0; i < cantidad; i++) {
        AnalisisNutricional memory analisis = analisisPorId[listaIds[i]];
        ids[i] = analisis.idAnalisis;
        cids[i] = analisis.cidIPFS;
        porcionesCorrectas[i] = analisis.porcionCorrecta;
        confianzas[i] = analisis.confianza;
        calorias[i] = analisis.calorias;
        timestamps[i] = analisis.timestamp;
    }
    
    return (ids, cids, porcionesCorrectas, confianzas, calorias, timestamps);
}
```

**Nota:** Esta función puede ser cara en gas si el usuario tiene muchos análisis. La versión simple (`obtenerAnalisisUsuario()`) es más eficiente.

---

### 5. `contarAnalisisUsuario()` - Contar análisis de un usuario

```solidity
function contarAnalisisUsuario(address usuario) 
    public 
    view 
    returns (uint256) 
{
    return analisisPorUsuario[usuario].length;
}
```

---

### 6. `obtenerTotalAnalisis()` - Estadística global (opcional)

```solidity
function obtenerTotalAnalisis() public view returns (uint256) {
    return contadorAnalisis;
}
```

---

## 📊 Eventos

### Event: AnalisisGuardado

```solidity
event AnalisisGuardado(
    address indexed usuario,        // Indexado para búsquedas
    uint256 indexed idAnalisis,     // Indexado para búsquedas
    string cidIPFS,                 // No indexado (string es caro)
    bool porcionCorrecta,
    uint256 timestamp
);
```

**Uso:**
- Indexar eventos en frontend
- Filtrar por usuario
- Filtrar por ID
- Crear historiales sin llamar al contrato

---

## 🔒 Consideraciones de Seguridad

### 1. Validación de Inputs

```solidity
require(bytes(cidIPFS).length > 0, "CID IPFS no puede estar vacio");
require(confianza <= 100, "Confianza debe ser entre 0 y 100");
require(calorias > 0, "Calorias deben ser mayores a 0");
```

### 2. Límites (Opcional)

```solidity
uint256 public MAX_ANALISIS_POR_USUARIO = 1000; // Límite opcional

function guardarAnalisis(...) public {
    require(
        analisisPorUsuario[msg.sender].length < MAX_ANALISIS_POR_USUARIO,
        "Limite de analisis alcanzado"
    );
    // ... resto del código
}
```

### 3. Reentrancy Protection

No es necesario aquí porque no enviamos ETH, pero buena práctica:

```solidity
bool private locked;

modifier noReentrant() {
    require(!locked, "No reentrant");
    locked = true;
    _;
    locked = false;
}
```

---

## ⛽ Optimización de Gas

### Estrategias:

1. **Usar `uint256` en lugar de `uint8/uint16`**
   - Solidity empaqueta en palabras de 32 bytes
   - Usar tipos más pequeños puede aumentar el gas

2. **Eventos indexados**
   - Solo indexar campos necesarios (máx 3)
   - Los strings NO deben indexarse (muy caro)

3. **Función `view` cuando sea posible**
   - No modifica estado = gratis

4. **Packing de variables de estado**
   - Variables pequeñas juntas en misma palabra (32 bytes)
   - Ejemplo: `bool porcionCorrecta` puede ir con otras variables

5. **Evitar loops grandes**
   - `obtenerTodosAnalisisUsuario()` puede ser cara
   - Mejor retornar IDs y obtener uno por uno

---

## 📝 Código Completo del Contrato

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract NutriLife {
    // ============ STRUCTS ============
    
    struct AnalisisNutricional {
        address usuario;
        string cidIPFS;
        bool porcionCorrecta;
        uint256 confianza;    // 0-100
        uint256 calorias;
        uint256 timestamp;
        uint256 idAnalisis;
    }
    
    // ============ STATE VARIABLES ============
    
    mapping(address => uint256[]) public analisisPorUsuario;
    mapping(uint256 => AnalisisNutricional) public analisisPorId;
    
    uint256 private contadorAnalisis;
    address public owner;
    
    // ============ EVENTS ============
    
    event AnalisisGuardado(
        address indexed usuario,
        uint256 indexed idAnalisis,
        string cidIPFS,
        bool porcionCorrecta,
        uint256 confianza,
        uint256 calorias,
        uint256 timestamp
    );
    
    // ============ MODIFIERS ============
    
    modifier soloOwner() {
        require(msg.sender == owner, "Solo el owner puede ejecutar");
        _;
    }
    
    // ============ CONSTRUCTOR ============
    
    constructor() {
        owner = msg.sender;
        contadorAnalisis = 0;
    }
    
    // ============ FUNCTIONS ============
    
    /**
     * @dev Guarda un nuevo análisis nutricional
     * @param cidIPFS CID de la imagen en IPFS
     * @param porcionCorrecta true si es porción correcta, false si es exceso
     * @param confianza Nivel de confianza del modelo (0-100)
     * @param calorias Calorías estimadas
     * @return ID del análisis guardado
     */
    function guardarAnalisis(
        string memory cidIPFS,
        bool porcionCorrecta,
        uint256 confianza,
        uint256 calorias
    ) public returns (uint256) {
        // Validaciones
        require(bytes(cidIPFS).length > 0, "CID IPFS no puede estar vacio");
        require(confianza <= 100, "Confianza debe ser entre 0 y 100");
        require(calorias > 0, "Calorias deben ser mayores a 0");
        
        // Incrementar contador
        contadorAnalisis++;
        
        // Crear nuevo análisis
        AnalisisNutricional memory nuevoAnalisis = AnalisisNutricional({
            usuario: msg.sender,
            cidIPFS: cidIPFS,
            porcionCorrecta: porcionCorrecta,
            confianza: confianza,
            calorias: calorias,
            timestamp: block.timestamp,
            idAnalisis: contadorAnalisis
        });
        
        // Guardar en storage
        analisisPorId[contadorAnalisis] = nuevoAnalisis;
        analisisPorUsuario[msg.sender].push(contadorAnalisis);
        
        // Emitir evento
        emit AnalisisGuardado(
            msg.sender,
            contadorAnalisis,
            cidIPFS,
            porcionCorrecta,
            confianza,
            calorias,
            block.timestamp
        );
        
        return contadorAnalisis;
    }
    
    /**
     * @dev Obtiene un análisis específico por ID
     */
    function obtenerAnalisis(uint256 idAnalisis) 
        public 
        view 
        returns (
            address usuario,
            string memory cidIPFS,
            bool porcionCorrecta,
            uint256 confianza,
            uint256 calorias,
            uint256 timestamp
        ) 
    {
        AnalisisNutricional memory analisis = analisisPorId[idAnalisis];
        require(analisis.idAnalisis != 0, "Analisis no existe");
        
        return (
            analisis.usuario,
            analisis.cidIPFS,
            analisis.porcionCorrecta,
            analisis.confianza,
            analisis.calorias,
            analisis.timestamp
        );
    }
    
    /**
     * @dev Obtiene todos los IDs de análisis de un usuario
     */
    function obtenerAnalisisUsuario(address usuario) 
        public 
        view 
        returns (uint256[] memory) 
    {
        return analisisPorUsuario[usuario];
    }
    
    /**
     * @dev Cuenta cuántos análisis tiene un usuario
     */
    function contarAnalisisUsuario(address usuario) 
        public 
        view 
        returns (uint256) 
    {
        return analisisPorUsuario[usuario].length;
    }
    
    /**
     * @dev Obtiene el total de análisis guardados (estadística global)
     */
    function obtenerTotalAnalisis() public view returns (uint256) {
        return contadorAnalisis;
    }
}
```

---

## 🧪 Casos de Uso

### Caso 1: Usuario guarda análisis

```javascript
// Frontend
const tx = await contract.guardarAnalisis(
    "QmXYZ123...",      // CID IPFS
    true,                // Porción correcta
    85,                  // 85% de confianza
    450                  // 450 calorías
);

await tx.wait(); // Esperar confirmación
```

### Caso 2: Usuario consulta su historial

```javascript
// Obtener IDs
const ids = await contract.obtenerAnalisisUsuario(walletAddress);

// Obtener cada análisis
for (let id of ids) {
    const analisis = await contract.obtenerAnalisis(id);
    console.log(analisis);
}
```

---

## 📊 Estimación de Gas

### Por transacción (Polygon):
- `guardarAnalisis()`: ~50,000 - 70,000 gas
- En Polygon: ~$0.001 - $0.002 por transacción

### Por consulta (gratis):
- `obtenerAnalisis()`: Gratis (view)
- `obtenerAnalisisUsuario()`: Gratis (view)

---

## 🔄 Versiones Futuras (Mejoras Opcionales)

### Versión 2.0 (Opcional):
- Sistema de permisos (solo usuario puede ver sus análisis)
- ~~Estadísticas agregadas~~ ✅ **IMPLEMENTADO EN V1.0**
- Sistema de recompensas (tokens)
- Múltiples usuarios por análisis

---

## ✅ Checklist de Desarrollo

- [x] Escribir contrato en Solidity ✅
- [ ] Compilar con Hardhat/Truffle
- [ ] Escribir tests unitarios
- [ ] Deployar a testnet (Ethereum Goerli/Sepolia)
- [ ] Verificar contrato en Etherscan
- [ ] Obtener ABI y dirección del contrato
- [ ] Integrar en frontend
- [ ] Testing end-to-end

## 📝 Notas de Implementación

**Ethereum seleccionado:**
- Usaremos Ethereum Goerli/Sepolia para testnet
- Ethereum Mainnet para producción

**Estadísticas agregadas implementadas:**
- Struct `EstadisticasUsuario` agregado
- Función `obtenerEstadisticasUsuario()` implementada
- Actualización automática de estadísticas al guardar análisis

---

**Este diseño es simple, seguro y eficiente en gas. Perfecto para empezar con blockchain!**

