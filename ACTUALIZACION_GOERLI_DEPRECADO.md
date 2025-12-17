# ⚠️ Actualización: Goerli Deprecado → Usar Sepolia

## 📢 Cambio Importante

**Goerli testnet ha sido oficialmente deprecado por Ethereum.**

### ¿Qué significa esto?

- ❌ Goerli ya no recibe soporte oficial
- ❌ Los faucets pueden fallar o estar vacíos
- ⚠️ Las transacciones pueden tardar mucho o no confirmarse
- ⚠️ Puede dejar de funcionar en cualquier momento

---

## ✅ Solución: Migrar a Sepolia

**Sepolia** es el reemplazo oficial recomendado por Ethereum.

### Ventajas de Sepolia:

- ✅ Soporte activo de Ethereum
- ✅ Faucets funcionando correctamente
- ✅ Transacciones rápidas y confiables
- ✅ Recomendado oficialmente
- ✅ Misma funcionalidad que Goerli

---

## 🔄 Cambios Necesarios

### 1. Configuración Actualizada

**Ya actualizado en:** `frontend/js/contract-config.js`

- Cambiado de `goerli` a `sepolia`
- Chain ID actualizado a `11155111`
- Explorer URL actualizado

### 2. MetaMask

**Agregar Sepolia:**
- Ve a chainlist.org
- Busca "Sepolia"
- Conecta wallet y agrega la red

**O manualmente:**
```
Network name: Sepolia
RPC URL: https://rpc.sepolia.org
Chain ID: 11155111
Currency: ETH
Explorer: https://sepolia.etherscan.io
```

### 3. Deployment

**Usar Sepolia en lugar de Goerli:**
- Ver guía: `DEPLOY_SEPOLIA_GUIA.md`

---

## 📋 Checklist de Migración

- [ ] Sepolia agregada a MetaMask
- [ ] ETH de prueba obtenido en Sepolia
- [ ] Contrato deployado en Sepolia
- [ ] Configuración actualizada (`contract-config.js`)
- [ ] Testing en Sepolia

---

## 📚 Documentación Actualizada

- ✅ `DEPLOY_SEPOLIA_GUIA.md` - Nueva guía para Sepolia
- ✅ `frontend/js/contract-config.js` - Actualizado para Sepolia
- ⚠️ `DEPLOY_GOERLI_GUIA.md` - Deprecada (solo referencia)

---

## 🎯 Próximos Pasos

1. **Agrega Sepolia a MetaMask**
2. **Obtén ETH de prueba** (sepoliafaucet.com)
3. **Deploy en Sepolia** siguiendo la nueva guía
4. **Actualiza la dirección del contrato** después del deploy

---

**¡Todo listo para usar Sepolia! 🚀**

