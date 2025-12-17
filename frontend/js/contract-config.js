// ============================================
// CONFIGURACIÓN DEL SMART CONTRACT
// ============================================
// 
// INSTRUCCIONES:
// 1. Después de deployar el contrato, copia la dirección aquí
// 2. El ABI ya está incluido desde NutriLifeABI.json
//
// ============================================

// ABI del contrato (cargado desde archivo JSON)
let NUTRILIFE_ABI = null;

// Cargar ABI desde archivo JSON
async function cargarABI() {
    try {
        const response = await fetch('js/NutriLifeABI.json');
        NUTRILIFE_ABI = await response.json();
        return NUTRILIFE_ABI;
    } catch (error) {
        console.error('Error cargando ABI:', error);
        // Fallback: ABI hardcodeado
        NUTRILIFE_ABI = [
            {
                "inputs": [],
                "stateMutability": "nonpayable",
                "type": "constructor"
            },
            {
                "anonymous": false,
                "inputs": [
                    {
                        "indexed": true,
                        "internalType": "address",
                        "name": "usuario",
                        "type": "address"
                    },
                    {
                        "indexed": true,
                        "internalType": "uint256",
                        "name": "idAnalisis",
                        "type": "uint256"
                    },
                    {
                        "indexed": false,
                        "internalType": "string",
                        "name": "cidIPFS",
                        "type": "string"
                    },
                    {
                        "indexed": false,
                        "internalType": "bool",
                        "name": "porcionCorrecta",
                        "type": "bool"
                    },
                    {
                        "indexed": false,
                        "internalType": "uint256",
                        "name": "confianza",
                        "type": "uint256"
                    },
                    {
                        "indexed": false,
                        "internalType": "uint256",
                        "name": "calorias",
                        "type": "uint256"
                    },
                    {
                        "indexed": false,
                        "internalType": "uint256",
                        "name": "timestamp",
                        "type": "uint256"
                    }
                ],
                "name": "AnalisisGuardado",
                "type": "event"
            },
            {
                "inputs": [
                    {
                        "internalType": "uint256",
                        "name": "",
                        "type": "uint256"
                    }
                ],
                "name": "analisisPorId",
                "outputs": [
                    {
                        "internalType": "address",
                        "name": "usuario",
                        "type": "address"
                    },
                    {
                        "internalType": "string",
                        "name": "cidIPFS",
                        "type": "string"
                    },
                    {
                        "internalType": "bool",
                        "name": "porcionCorrecta",
                        "type": "bool"
                    },
                    {
                        "internalType": "uint256",
                        "name": "confianza",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "calorias",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "timestamp",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "idAnalisis",
                        "type": "uint256"
                    }
                ],
                "stateMutability": "view",
                "type": "function"
            },
            {
                "inputs": [
                    {
                        "internalType": "address",
                        "name": "",
                        "type": "address"
                    },
                    {
                        "internalType": "uint256",
                        "name": "",
                        "type": "uint256"
                    }
                ],
                "name": "analisisPorUsuario",
                "outputs": [
                    {
                        "internalType": "uint256",
                        "name": "",
                        "type": "uint256"
                    }
                ],
                "stateMutability": "view",
                "type": "function"
            },
            {
                "inputs": [
                    {
                        "internalType": "address",
                        "name": "usuario",
                        "type": "address"
                    }
                ],
                "name": "contarAnalisisUsuario",
                "outputs": [
                    {
                        "internalType": "uint256",
                        "name": "",
                        "type": "uint256"
                    }
                ],
                "stateMutability": "view",
                "type": "function"
            },
            {
                "inputs": [
                    {
                        "internalType": "address",
                        "name": "",
                        "type": "address"
                    }
                ],
                "name": "estadisticasUsuario",
                "outputs": [
                    {
                        "internalType": "uint256",
                        "name": "totalAnalisis",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "porcionesCorrectas",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "excesos",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "caloriasTotales",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "caloriasPromedio",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "confianzaPromedio",
                        "type": "uint256"
                    }
                ],
                "stateMutability": "view",
                "type": "function"
            },
            {
                "inputs": [
                    {
                        "internalType": "string",
                        "name": "cidIPFS",
                        "type": "string"
                    },
                    {
                        "internalType": "bool",
                        "name": "porcionCorrecta",
                        "type": "bool"
                    },
                    {
                        "internalType": "uint256",
                        "name": "confianza",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "calorias",
                        "type": "uint256"
                    }
                ],
                "name": "guardarAnalisis",
                "outputs": [
                    {
                        "internalType": "uint256",
                        "name": "",
                        "type": "uint256"
                    }
                ],
                "stateMutability": "nonpayable",
                "type": "function"
            },
            {
                "inputs": [
                    {
                        "internalType": "uint256",
                        "name": "idAnalisis",
                        "type": "uint256"
                    }
                ],
                "name": "obtenerAnalisis",
                "outputs": [
                    {
                        "internalType": "address",
                        "name": "usuario",
                        "type": "address"
                    },
                    {
                        "internalType": "string",
                        "name": "cidIPFS",
                        "type": "string"
                    },
                    {
                        "internalType": "bool",
                        "name": "porcionCorrecta",
                        "type": "bool"
                    },
                    {
                        "internalType": "uint256",
                        "name": "confianza",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "calorias",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "timestamp",
                        "type": "uint256"
                    }
                ],
                "stateMutability": "view",
                "type": "function"
            },
            {
                "inputs": [
                    {
                        "internalType": "address",
                        "name": "usuario",
                        "type": "address"
                    }
                ],
                "name": "obtenerAnalisisUsuario",
                "outputs": [
                    {
                        "internalType": "uint256[]",
                        "name": "",
                        "type": "uint256[]"
                    }
                ],
                "stateMutability": "view",
                "type": "function"
            },
            {
                "inputs": [
                    {
                        "internalType": "address",
                        "name": "usuario",
                        "type": "address"
                    }
                ],
                "name": "obtenerEstadisticasUsuario",
                "outputs": [
                    {
                        "internalType": "uint256",
                        "name": "totalAnalisis",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "porcionesCorrectas",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "excesos",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "caloriasTotales",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "caloriasPromedio",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "confianzaPromedio",
                        "type": "uint256"
                    }
                ],
                "stateMutability": "view",
                "type": "function"
            },
            {
                "inputs": [],
                "name": "obtenerTotalAnalisis",
                "outputs": [
                    {
                        "internalType": "uint256",
                        "name": "",
                        "type": "uint256"
                    }
                ],
                "stateMutability": "view",
                "type": "function"
            },
            {
                "inputs": [],
                "name": "owner",
                "outputs": [
                    {
                        "internalType": "address",
                        "name": "",
                        "type": "address"
                    }
                ],
                "stateMutability": "view",
                "type": "function"
            }
        ];
        return NUTRILIFE_ABI;
    }
}

// Configuración del contrato
const CONTRACT_CONFIG = {
    // Dirección del contrato deployado en Sepolia Testnet
    // Deployado: Block 9857790, Tx: 0x4a9fd44390c9eb139983e02c47af30a5028ac145aa77c2e0d875e16d43ba7dd8
    // Verificado en: Sourcify, Blockscout, Routescan
    ADDRESS: "0xcb726f3e59518C7b24c74FB7279aA4554927D4A1", // Sepolia Testnet
    
    // Configuración de la red
    NETWORK: {
        name: "sepolia", // "sepolia" (recomendado), "holesky", o "mainnet"
        chainId: 11155111 // Sepolia: 11155111, Holesky: 17000, Mainnet: 1
    },
    
    // URLs de exploradores de blockchain
    EXPLORER_URLS: {
        sepolia: "https://sepolia.etherscan.io",
        holesky: "https://holesky.etherscan.io",
        mainnet: "https://etherscan.io"
    }
};

// Función helper para obtener URL del explorador
function getExplorerUrl(network, txHash) {
    const baseUrl = CONTRACT_CONFIG.EXPLORER_URLS[network] || CONTRACT_CONFIG.EXPLORER_URLS.sepolia;
    return `${baseUrl}/tx/${txHash}`;
}

// Función para obtener el ABI
async function getABI() {
    if (!NUTRILIFE_ABI) {
        await cargarABI();
    }
    return NUTRILIFE_ABI;
}

