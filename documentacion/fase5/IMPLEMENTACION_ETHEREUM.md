# 🔧 Guía de Implementación - Ethereum

## 🎯 Configuración para Ethereum

Esta guía te ayudará a configurar el proyecto para desarrollar y deployar el Smart Contract en Ethereum.

---

## 📋 Prerequisitos

### 1. Node.js y npm

```bash
node --version  # Debe ser >= 16.0.0
npm --version
```

### 2. Instalar Hardhat (Recomendado)

```bash
npm init -y
npm install --save-dev hardhat
npx hardhat init
```

**Selecciona:**
- Create a JavaScript project
- Yes to all questions

---

## 📁 Estructura del Proyecto

```
ia_web3/
├── contracts/
│   └── NutriLife.sol           # ✅ Smart Contract creado
├── scripts/
│   ├── deploy.js               # Script de deployment
│   └── test.js                 # Script de pruebas
├── test/
│   └── NutriLife.test.js       # Tests unitarios
├── hardhat.config.js           # Configuración de Hardhat
└── package.json                # Dependencias
```

---

## ⚙️ Configuración de Hardhat

### hardhat.config.js

```javascript
require("@nomicfoundation/hardhat-toolbox");
require("dotenv").config();

/** @type import('hardhat/config').HardhatUserConfig */
module.exports = {
  solidity: {
    version: "0.8.19",
    settings: {
      optimizer: {
        enabled: true,
        runs: 200
      }
    }
  },
  networks: {
    // Ethereum Sepolia Testnet (Recomendado - Goerli está deprecado)
    sepolia: {
      url: process.env.SEPOLIA_RPC_URL || "https://rpc.sepolia.org",
      accounts: process.env.PRIVATE_KEY ? [process.env.PRIVATE_KEY] : [],
      chainId: 11155111
    },
    // Ethereum Sepolia Testnet (alternativa)
    sepolia: {
      url: process.env.SEPOLIA_RPC_URL || "https://rpc.sepolia.org",
      accounts: process.env.PRIVATE_KEY ? [process.env.PRIVATE_KEY] : [],
      chainId: 11155111
    },
    // Ethereum Mainnet (para producción)
    mainnet: {
      url: process.env.MAINNET_RPC_URL || "https://eth.llamarpc.com",
      accounts: process.env.PRIVATE_KEY ? [process.env.PRIVATE_KEY] : [],
      chainId: 1
    }
  },
  etherscan: {
    apiKey: process.env.ETHERSCAN_API_KEY
  }
};
```

---

## 🔐 Variables de Entorno

### Crear archivo `.env` en la raíz:

```env
# Private Key de tu wallet (NUNCA compartir)
PRIVATE_KEY=tu_private_key_aqui

# RPC URLs (puedes usar servicios gratuitos)
GOERLI_RPC_URL=https://rpc.ankr.com/eth_goerli
SEPOLIA_RPC_URL=https://rpc.sepolia.org
MAINNET_RPC_URL=https://eth.llamarpc.com

# API Key de Etherscan (para verificar contratos)
ETHERSCAN_API_KEY=tu_api_key_aqui

# Dirección del contrato deployado (se llena después del deploy)
CONTRACT_ADDRESS=
```

**⚠️ IMPORTANTE:** Agrega `.env` al `.gitignore`!

---

## 📦 Instalar Dependencias

```bash
npm install --save-dev @nomicfoundation/hardhat-toolbox
npm install --save-dev dotenv
npm install --save-dev @openzeppelin/contracts  # (opcional, para mejoras futuras)
```

---

## 🧪 Crear Tests

### test/NutriLife.test.js

```javascript
const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("NutriLife", function () {
  let nutrilife;
  let owner;
  let addr1;

  beforeEach(async function () {
    [owner, addr1] = await ethers.getSigners();

    const NutriLife = await ethers.getContractFactory("NutriLife");
    nutrilife = await NutriLife.deploy();
    await nutrilife.deployed();
  });

  describe("Deployment", function () {
    it("Should set the right owner", async function () {
      expect(await nutrilife.owner()).to.equal(owner.address);
    });

    it("Should start with zero analyses", async function () {
      expect(await nutrilife.obtenerTotalAnalisis()).to.equal(0);
    });
  });

  describe("Guardar Analisis", function () {
    it("Should save an analysis correctly", async function () {
      const tx = await nutrilife.guardarAnalisis(
        "QmTest123...",
        true,
        85,
        450
      );
      await tx.wait();

      expect(await nutrilife.obtenerTotalAnalisis()).to.equal(1);
      
      const analisis = await nutrilife.obtenerAnalisis(1);
      expect(analisis.cidIPFS).to.equal("QmTest123...");
      expect(analisis.porcionCorrecta).to.equal(true);
      expect(analisis.confianza).to.equal(85);
      expect(analisis.calorias).to.equal(450);
    });

    it("Should update user statistics", async function () {
      await nutrilife.guardarAnalisis("QmTest1", true, 85, 450);
      await nutrilife.guardarAnalisis("QmTest2", false, 90, 600);

      const stats = await nutrilife.obtenerEstadisticasUsuario(owner.address);
      expect(stats.totalAnalisis).to.equal(2);
      expect(stats.porcionesCorrectas).to.equal(1);
      expect(stats.excesos).to.equal(1);
      expect(stats.caloriasPromedio).to.equal(525); // (450 + 600) / 2
    });

    it("Should reject invalid inputs", async function () {
      await expect(
        nutrilife.guardarAnalisis("", true, 85, 450)
      ).to.be.revertedWith("CID IPFS no puede estar vacio");

      await expect(
        nutrilife.guardarAnalisis("QmTest", true, 101, 450)
      ).to.be.revertedWith("Confianza debe ser entre 0 y 100");
    });
  });

  describe("Obtener Analisis", function () {
    beforeEach(async function () {
      await nutrilife.guardarAnalisis("QmTest1", true, 85, 450);
      await nutrilife.guardarAnalisis("QmTest2", false, 90, 600);
    });

    it("Should return user's analysis IDs", async function () {
      const ids = await nutrilife.obtenerAnalisisUsuario(owner.address);
      expect(ids.length).to.equal(2);
      expect(ids[0]).to.equal(1);
      expect(ids[1]).to.equal(2);
    });

    it("Should return correct analysis by ID", async function () {
      const analisis = await nutrilife.obtenerAnalisis(1);
      expect(analisis.cidIPFS).to.equal("QmTest1");
      expect(analisis.usuario).to.equal(owner.address);
    });

    it("Should revert for non-existent analysis", async function () {
      await expect(nutrilife.obtenerAnalisis(999)).to.be.revertedWith(
        "Analisis no existe"
      );
    });
  });
});
```

---

## 🚀 Script de Deployment

### scripts/deploy.js

```javascript
const hre = require("hardhat");

async function main() {
  console.log("🚀 Deploying NutriLife contract...");

  const NutriLife = await hre.ethers.getContractFactory("NutriLife");
  const nutrilife = await NutriLife.deploy();

  await nutrilife.deployed();

  console.log("✅ NutriLife deployed to:", nutrilife.address);
  console.log("📝 Contract address:", nutrilife.address);
  console.log("\n💡 Save this address in your .env file as CONTRACT_ADDRESS");

  // Verificar en Etherscan (opcional)
  if (hre.network.name !== "hardhat" && process.env.ETHERSCAN_API_KEY) {
    console.log("\n⏳ Verifying contract on Etherscan...");
    try {
      await hre.run("verify:verify", {
        address: nutrilife.address,
        constructorArguments: [],
      });
      console.log("✅ Contract verified on Etherscan!");
    } catch (error) {
      console.log("⚠️ Verification failed:", error.message);
    }
  }
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
```

---

## 📝 Comandos Útiles

### Compilar contrato:
```bash
npx hardhat compile
```

### Ejecutar tests:
```bash
npx hardhat test
```

### Deploy a Sepolia Testnet:
```bash
npx hardhat run scripts/deploy.js --network sepolia
```

### Deploy a Sepolia Testnet:
```bash
npx hardhat run scripts/deploy.js --network sepolia
```

### Deploy a Mainnet (producción):
```bash
npx hardhat run scripts/deploy.js --network mainnet
```

---

## 🔑 Obtener ETH de Prueba (Testnet)

### Sepolia Faucet (Recomendado - Goerli está deprecado):
- https://sepoliafaucet.com/
- https://www.alchemy.com/faucets/ethereum-sepolia
- https://faucet.quicknode.com/ethereum/sepolia

---

## 📊 Después del Deploy

1. **Guardar la dirección del contrato** en `.env`:
   ```env
   CONTRACT_ADDRESS=0x...
   ```

2. **Obtener el ABI** del archivo de compilación:
   ```
   artifacts/contracts/NutriLife.sol/NutriLife.json
   ```
   Copia el campo `abi` de este archivo.

3. **Usar en frontend** con la dirección y ABI.

---

## ⚠️ Importante

- **Testnet primero:** Siempre prueba en testnet antes de mainnet
- **Gas fees:** En mainnet, cada transacción cuesta dinero real
- **Private Key:** NUNCA compartas tu private key
- **Backup:** Guarda bien tu private key y contraseña de MetaMask

---

## ✅ Checklist de Deployment

- [ ] Hardhat configurado
- [ ] Contrato compilado sin errores
- [ ] Tests pasando
- [ ] `.env` configurado con PRIVATE_KEY
- [ ] ETH de prueba obtenido (para testnet)
- [ ] Contrato deployado en testnet
- [ ] Contrato verificado en Etherscan
- [ ] Dirección y ABI guardados
- [ ] Listo para integrar en frontend

---

**¡Listo para deployar a Ethereum! 🚀**

