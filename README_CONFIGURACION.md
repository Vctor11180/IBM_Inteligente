# 🔐 Configuración de Variables de Entorno

## ⚠️ IMPORTANTE

Este archivo explica qué variables de entorno necesitas configurar.  
**NUNCA subas el archivo `.env` con valores reales a GitHub.**

---

## 📋 Variables Necesarias

### Para IPFS (Pinata)

Crea un archivo `.env` en la raíz del proyecto con:

```env
PINATA_JWT=tu_jwt_token_de_pinata_aqui
```

**Cómo obtener tu JWT de Pinata:**
1. Ve a: https://app.pinata.cloud/developers/api-keys
2. Crea una nueva API Key
3. Copia el JWT token
4. Pégalo en tu archivo `.env`

---

## 📝 Archivo .env.example

El archivo `.env.example` muestra la estructura sin valores reales.  
**SÍ debe subirse a GitHub** (es solo documentación).

---

## ✅ Verificación

Antes de subir a GitHub, verifica:

1. ✅ El archivo `.env` está en `.gitignore`
2. ✅ No hay claves hardcodeadas en el código
3. ✅ Todas las claves se leen de variables de entorno

---

## 🚀 Para Nuevos Colaboradores

1. Clona el repositorio
2. Copia `.env.example` a `.env`
3. Rellena los valores con tus propias claves
4. El archivo `.env` NO se subirá a GitHub (está en .gitignore)

---

**¡Mantén tus claves seguras! 🔒**

