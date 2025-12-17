# 🔧 Solución: Error "ethers is not defined"

## ❌ Error

```
Error al conectar wallet: ethers is not defined
```

## 🔍 Causa

El CDN de Ethers.js no está cargando correctamente o el script intenta usar `ethers` antes de que se cargue.

## ✅ Solución Aplicada

### 1. Cambio de URL del CDN

**Antes:**
```html
<script src="https://cdn.ethers.io/lib/ethers-5.7.2.umd.min.js"></script>
```

**Después:**
```html
<script src="https://cdn.jsdelivr.net/npm/ethers@5.7.2/dist/ethers.umd.min.js"></script>
```

### 2. Verificación de Disponibilidad

Se agregó una verificación en `conectarWallet()` para asegurar que `ethers` esté disponible:

```javascript
if (typeof ethers === 'undefined') {
    alert('Error: Ethers.js no está cargado. Por favor, recarga la página.');
    console.error('Ethers.js no está disponible');
    return false;
}
```

---

## 🔄 Pasos para Resolver

1. **Recarga la página completamente** (Ctrl+F5 o Cmd+Shift+R)
2. **Verifica en la consola del navegador** que no haya errores de carga
3. **Abre las herramientas de desarrollador** (F12)
4. **Ve a la pestaña Network**
5. **Recarga la página**
6. **Busca "ethers"** en las peticiones
7. **Verifica que se cargue correctamente** (status 200)

---

## 🆘 Si el Error Persiste

### Opción 1: Verificar Conexión a Internet

El CDN requiere conexión a internet. Verifica que tengas conexión.

### Opción 2: Usar CDN Alternativo

Si jsdelivr no funciona, puedes probar:

```html
<script src="https://unpkg.com/ethers@5.7.2/dist/ethers.umd.min.js"></script>
```

### Opción 3: Descargar Ethers.js Localmente

1. Descarga: https://github.com/ethers-io/ethers.js/releases
2. Extrae `ethers.umd.min.js`
3. Colócalo en `frontend/js/ethers.umd.min.js`
4. Cambia el script a:

```html
<script src="js/ethers.umd.min.js"></script>
```

---

## ✅ Verificación

Para verificar que Ethers.js está cargado:

1. Abre la consola del navegador (F12)
2. Escribe: `typeof ethers`
3. Debería devolver: `"object"`

Si devuelve `"undefined"`, Ethers.js no se cargó correctamente.

---

## 📝 Notas

- El CDN de jsdelivr es más confiable y tiene mejor disponibilidad
- La versión 5.7.2 es estable y compatible
- Si usas un servidor local (`python -m http.server`), asegúrate de que el HTML se esté sirviendo correctamente

---

**Si el problema persiste, verifica la consola del navegador para más detalles del error.**

