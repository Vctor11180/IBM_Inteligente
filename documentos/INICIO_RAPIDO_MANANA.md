# 🚀 Inicio Rápido - Para Continuar Mañana

## 📋 Pasos para Levantar el Proyecto

### 1. Activar Entorno Virtual

```bash
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# O si no funciona:
.venv\Scripts\activate.bat
```

---

### 2. Iniciar Backend

**Terminal 1:**
```bash
cd D:\PROYECTOS\ia_web3
python backend/app.py
```

**Deberías ver:**
```
🚀 Iniciando NutriLife Backend API
📡 Servidor corriendo en: http://localhost:5000
```

---

### 3. Iniciar Frontend

**Terminal 2 (nueva terminal):**
```bash
cd D:\PROYECTOS\ia_web3\frontend
python -m http.server 8000
```

**O desde la raíz:**
```bash
cd D:\PROYECTOS\ia_web3
cd frontend
python -m http.server 8000
```

---

### 4. Abrir en el Navegador

Abre: **http://localhost:8000**

---

## ✅ Verificación Rápida

1. **Backend funcionando:**
   - Ve a: http://localhost:5000/api/health
   - Debería responder: `{"status": "ok"}`

2. **Frontend funcionando:**
   - Abre: http://localhost:8000
   - Deberías ver la aplicación NutriLife

3. **Wallet:**
   - Abre Core Wallet
   - Asegúrate de estar en Sepolia
   - Conecta en la aplicación

---

## 🔧 Si Algo No Funciona

### Backend no inicia:
```bash
# Verificar que estás en el venv
.venv\Scripts\Activate.ps1

# Instalar dependencias si falta algo
pip install -r requirements.txt
```

### Frontend no carga:
- Verifica que el servidor esté corriendo en el puerto 8000
- Verifica que estés en la carpeta `frontend`

### Wallet no conecta:
- Verifica que Core Wallet esté abierta
- Verifica que estés en red Sepolia

---

## 📝 Recordatorios

- ✅ Backend en: `http://localhost:5000`
- ✅ Frontend en: `http://localhost:8000`
- ✅ Wallet: Core Wallet en Sepolia
- ✅ Contrato: `0xcb726f3e59518C7b24c74FB7279aA4554927D4A1`

---

## 🎯 Próxima Fase

**Última fase:** Pruebas finales y verificación completa del flujo end-to-end.

**Tareas:**
- [ ] Probar flujo completo (IMC → Análisis → Guardar en Blockchain)
- [ ] Verificar historial
- [ ] Verificar transacciones en Etherscan
- [ ] Documentar resultados

---

**¡Hasta mañana! 🚀**

