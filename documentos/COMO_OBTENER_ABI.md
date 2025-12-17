# 📋 Cómo Obtener el ABI desde Remix

## 🎯 Objetivo

Obtener el ABI (Application Binary Interface) del contrato NutriLife compilado en Remix para usarlo en el frontend.

---

## 📝 Método 1: Desde el Panel de Compilación (Más Fácil)

### Paso a Paso:

1. **En Remix, ve al panel izquierdo donde está "SOLIDITY COMPILER"**

2. **Después de compilar exitosamente, busca la sección del contrato:**
   - Deberías ver algo como "Contract: prueba.sol"
   - O "Contract: NutriLife"

3. **Haz clic en el botón "ABI"**
   - Está en la parte inferior del panel de compilación
   - Tiene un ícono azul de documento

4. **Copia el contenido:**
   - Se abrirá un archivo JSON
   - Selecciona TODO el contenido (Ctrl+A)
   - Copia (Ctrl+C)

5. **Guarda en un archivo:**
   - Crea o abre: `frontend/js/NutriLifeABI.json`
   - Pega el contenido
   - Guarda

---

## 📝 Método 2: Desde el Navegador de Archivos de Remix

### Paso a Paso:

1. **En Remix, ve a la pestaña "FILE EXPLORER" (panel izquierdo)**

2. **Navega a la carpeta de compilación:**
   - Busca una carpeta llamada `artifacts/` o `.deps/`
   - O busca archivos `.json`

3. **Busca el archivo del contrato:**
   - Debería llamarse algo como: `NutriLife.json` o `prueba_NutriLife.json`
   - O busca archivos que contengan el nombre de tu contrato

4. **Abre el archivo JSON**

5. **Busca el campo `"abi"`:**
   ```json
   {
     "contractName": "NutriLife",
     "abi": [
       {
         "inputs": [...],
         "name": "guardarAnalisis",
         ...
       },
       ...
     ],
     ...
   }
   ```

6. **Copia solo el array del campo `"abi"`:**
   - Es el array que está dentro de `"abi": [...]`
   - Copia desde `[` hasta `]`

---

## 📝 Método 3: Desde la Consola del Navegador (Avanzado)

Si los métodos anteriores no funcionan:

1. **Abre la consola del navegador** (F12)

2. **En Remix, después de compilar, ejecuta en la consola:**
   ```javascript
   // Busca el compilador de Remix
   remix.call('compilerArtefacts', 'getCompilerAbstract', 'prueba.sol')
     .then(result => {
       const abi = result.data.abi;
       console.log(JSON.stringify(abi, null, 2));
       // Copia el resultado
     });
   ```

---

## ✅ Verificar que el ABI es Correcto

El ABI debería contener funciones como:

- `guardarAnalisis` - Función para guardar análisis
- `obtenerAnalisis` - Función para obtener análisis por ID
- `obtenerAnalisisUsuario` - Función para obtener IDs de usuario
- `obtenerEstadisticasUsuario` - Función para obtener estadísticas
- `contarAnalisisUsuario` - Función para contar análisis
- `obtenerTotalAnalisis` - Función para total global

**Formato esperado:**
```json
[
  {
    "inputs": [...],
    "name": "guardarAnalisis",
    "outputs": [...],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  ...
]
```

---

## 💾 Guardar el ABI

### Opción 1: Como archivo JSON separado

**Crear:** `frontend/js/NutriLifeABI.json`

```json
[
  {
    "inputs": [...],
    "name": "guardarAnalisis",
    ...
  },
  ...
]
```

### Opción 2: Directamente en el código JavaScript

**En:** `frontend/js/contract-config.js`

```javascript
const NUTRILIFE_ABI = [
  // ... pegar el ABI aquí
];
```

---

## 🎯 Formato Final del ABI

El ABI debe ser un **array JSON** que empiece con `[` y termine con `]`.

**Ejemplo mínimo:**
```json
[
  {
    "inputs": [
      {"internalType": "string", "name": "cidIPFS", "type": "string"},
      {"internalType": "bool", "name": "porcionCorrecta", "type": "bool"},
      {"internalType": "uint256", "name": "confianza", "type": "uint256"},
      {"internalType": "uint256", "name": "calorias", "type": "uint256"}
    ],
    "name": "guardarAnalisis",
    "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
    "stateMutability": "nonpayable",
    "type": "function"
  }
]
```

---

## ✅ Checklist

- [ ] Encontré el botón "ABI" en Remix
- [ ] Copié todo el contenido del ABI
- [ ] Verifiqué que es un array JSON válido
- [ ] Guardé el ABI en un archivo
- [ ] El ABI contiene las funciones principales

---

## 🆘 Si Tienes Problemas

**Problema:** No encuentro el botón ABI
- **Solución:** Asegúrate de haber compilado primero. El botón aparece después de compilar.

**Problema:** El ABI está vacío o incompleto
- **Solución:** Revisa que la compilación fue exitosa. Si hay errores, el ABI no estará completo.

**Problema:** No puedo copiar el ABI
- **Solución:** Intenta hacer clic derecho → "Guardar como" o usar el método 2 (desde archivos).

---

**¿Ya obtuviste el ABI? Si sí, guárdalo y podemos continuar con el siguiente paso! 📋**

