# 🔒 Guía: Subir Proyecto a GitHub de Forma Segura

## ✅ Verificación de Seguridad

Antes de subir a GitHub, verifica que NO estés subiendo información sensible.

---

## 🔐 Qué NUNCA Debe Subirse

### ❌ Archivos que NO deben subirse:

1. **Archivos `.env`** (ya está en .gitignore ✅)
   - Contiene: `PINATA_JWT`, claves privadas
   
2. **Claves privadas de wallets**
   - Private keys de Ethereum
   - Seed phrases
   
3. **API Keys**
   - PINATA_JWT (JWT de Pinata)
   - ETHERSCAN_API_KEY (si la usas)
   - Cualquier otra API key

4. **Archivos de configuración con secrets**
   - Cualquier archivo que contenga credenciales

---

## ✅ Verificación Pre-Commit

### Paso 1: Verificar .gitignore

El archivo `.gitignore` ya está configurado para ignorar:
- ✅ `.env` y `*.env`
- ✅ `venv/` y `.venv/`
- ✅ `__pycache__/`
- ✅ `node_modules/`
- ✅ `artifacts/` y `cache/`

**Verificación:**
```bash
# Verifica qué archivos serían subidos
git status
```

**Si ves `.env` en la lista, NO LO SUBAS!**

---

### Paso 2: Buscar Claves en el Código

**Busca si hay claves hardcodeadas:**

```bash
# Buscar posibles claves hardcodeadas (en Windows PowerShell)
Select-String -Path .\backend\* -Pattern "PINATA_JWT|api_key|secret|private_key" -CaseSensitive:$false
```

**Si encuentras claves hardcodeadas, elimínalas y usa variables de entorno.**

---

## ✅ Estado Actual del Proyecto

### ✅ Bien Configurado:

1. **Pinata JWT**: ✅ Se lee de variable de entorno (`os.getenv('PINATA_JWT')`)
2. **No hay claves hardcodeadas**: ✅ Todo usa variables de entorno
3. **.gitignore configurado**: ✅ Ignora `.env` y otros archivos sensibles

---

## 📋 Checklist Antes de Subir a GitHub

- [ ] Verificar que `.env` NO está en `git status`
- [ ] Verificar que no hay claves hardcodeadas en el código
- [ ] Verificar que `.gitignore` incluye `.env`
- [ ] Crear `.env.example` con estructura (sin valores reales)
- [ ] Revisar que no hay información sensible en commits anteriores

---

## 🚀 Pasos para Subir a GitHub

### 1. Verificar Estado de Git

```bash
git status
```

**Asegúrate de que `.env` NO aparezca en la lista.**

---

### 2. Si .env está en Git (accidentalmente)

Si accidentalmente ya agregaste `.env` a Git:

```bash
# Remover del tracking (NO elimina el archivo local)
git rm --cached .env

# Agregar a .gitignore (ya está, pero verifica)
echo ".env" >> .gitignore

# Commit el cambio
git commit -m "Remove .env from tracking"
```

---

### 3. Agregar Archivos

```bash
# Agregar todos los archivos (excepto los en .gitignore)
git add .

# Verificar qué se va a subir
git status
```

---

### 4. Crear Commit

```bash
git commit -m "feat: Implementación completa Fase 1-5: IA, Backend, Frontend, IPFS y Blockchain"
```

---

### 5. Subir a GitHub

```bash
# Si es tu primer push
git remote add origin https://github.com/TU_USUARIO/TU_REPO.git
git branch -M main
git push -u origin main

# Si ya tienes el remote configurado
git push
```

---

## 📝 Archivo .env.example

He creado `.env.example` que documenta qué variables se necesitan **sin valores reales**.

**Este archivo SÍ debe subirse** (es solo documentación).

---

## 🔍 Qué SÍ Debe Subirse

### ✅ Archivos que SÍ deben subirse:

- ✅ Todo el código fuente (`*.py`, `*.html`, `*.css`, `*.js`, `*.sol`)
- ✅ Archivos de configuración sin secrets (`requirements.txt`, `package.json`)
- ✅ Documentación (`*.md`)
- ✅ `.env.example` (ejemplo sin valores reales)
- ✅ `.gitignore`
- ✅ Modelos (opcional, si son pequeños)
- ✅ Estructura de carpetas

### ❌ Archivos que NO deben subirse:

- ❌ `.env` (con valores reales)
- ❌ Claves privadas
- ❌ API keys
- ❌ `__pycache__/`
- ❌ `venv/` o `.venv/`
- ❌ `node_modules/`
- ❌ Archivos temporales

---

## 🆘 Si Subiste Algo por Error

### Si subiste `.env` o claves:

1. **Cambia las claves inmediatamente:**
   - Ve a Pinata y genera un nuevo JWT
   - Si subiste una private key, transfiere tus fondos a una nueva wallet

2. **Elimina el archivo del historial de Git:**
   ```bash
   # Esto es complejo, busca ayuda o considera el repositorio comprometido
   # Mejor: elimina el repo y créalo de nuevo
   ```

3. **Mejor práctica:** Si subiste información sensible, es mejor:
   - Eliminar el repositorio
   - Regenerar todas las claves
   - Crear un nuevo repositorio

---

## ✅ Resumen

**Tu proyecto está configurado correctamente:**
- ✅ `.env` está en `.gitignore`
- ✅ No hay claves hardcodeadas
- ✅ Todo usa variables de entorno
- ✅ `.env.example` creado para documentación

**Puedes subir a GitHub con seguridad.**

Solo verifica una vez más con `git status` que `.env` no aparece antes de hacer commit.

---

**¡Todo listo para subir de forma segura! 🔒**

