// ============================================
// CONFIGURACIÓN DEL SMART CONTRACT
// ============================================
// 
// INSTRUCCIONES:
// 1. Después de deployar el contrato, copia la dirección aquí
// 2. Copia el ABI desde Remix (botón ABI) o desde el archivo compilado
// 3. Renombra este archivo a: contract-config.js
// 4. Actualiza los valores con tu contrato deployado
//
// ============================================

const CONTRACT_CONFIG = {
    // Dirección del contrato deployado en Ethereum
    // Ejemplo: "0x1234567890123456789012345678901234567890"
    ADDRESS: "0x...", // ⚠️ ACTUALIZAR después del deploy
    
    // ABI del contrato (copiar desde Remix - botón ABI)
    // O desde: artifacts/contracts/NutriLife.sol/NutriLife.json (campo "abi")
    ABI: [
        // ⚠️ PEGAR EL ABI COMPLETO AQUÍ desde Remix
        // Es un array JSON con todas las funciones del contrato
    ],
    
    // Configuración de la red
    NETWORK: {
        name: "goerli", // "goerli", "sepolia", o "mainnet"
        chainId: 5 // Goerli: 5, Sepolia: 11155111, Mainnet: 1
    },
    
    // URLs de exploradores de blockchain
    EXPLORER_URLS: {
        goerli: "https://goerli.etherscan.io",
        sepolia: "https://sepolia.etherscan.io",
        mainnet: "https://etherscan.io"
    }
};

// Función helper para obtener URL del explorador
function getExplorerUrl(network, txHash) {
    const baseUrl = CONTRACT_CONFIG.EXPLORER_URLS[network] || CONTRACT_CONFIG.EXPLORER_URLS.goerli;
    return `${baseUrl}/tx/${txHash}`;
}

