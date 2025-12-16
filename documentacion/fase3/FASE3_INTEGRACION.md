# 📚 Fase 3: Integración Frontend-Backend

## 📋 Objetivo

Integrar completamente el frontend con el backend API, permitiendo a los usuarios:
- Subir imágenes de comida
- Analizar las imágenes con el modelo de IA
- Ver recomendaciones nutricionales personalizadas basadas en su IMC
- Integrar el análisis con la calculadora de IMC existente

## 🎯 Checklist de la Fase 3

- [ ] Crear componente de subida de imágenes
- [ ] Integrar botón de cámara en NutriBot con subida de imágenes
- [ ] Conectar con endpoint `/api/analizar-imagen`
- [ ] Mostrar resultados del análisis en la UI
- [ ] Integrar datos del IMC del usuario con el análisis
- [ ] Añadir vista de análisis de imágenes
- [ ] Mostrar recomendaciones visualmente
- [ ] Manejar errores y estados de carga
- [ ] Mejorar UX con feedback visual

## 🏗️ Cambios Necesarios en el Frontend

### 1. Nueva Vista: Análisis de Imágenes

Agregar una nueva sección donde se muestre:
- Área para subir/seleccionar imagen
- Vista previa de la imagen
- Botón para analizar
- Resultados del análisis (porción correcta/exceso)
- Recomendaciones personalizadas
- Calorías estimadas

### 2. Modificar NutriBot

- El botón 📷 debe abrir selector de imágenes
- Permitir arrastrar y soltar imágenes
- Mostrar análisis directamente en el chat

### 3. Integrar con Calculadora IMC

- Usar datos del IMC calculado para personalizar recomendaciones
- Guardar datos del usuario en localStorage
- Pre-llenar campos en análisis de imágenes

## 📡 Integración con Backend

### Endpoint a usar: POST `/api/analizar-imagen`

**Request** (FormData):
```
imagen: File
imc: number
categoria_imc: string
calorias_objetivo: number
objetivo: string
```

**Response**:
```json
{
  "success": true,
  "analisis": {
    "porcion_correcta": true,
    "confianza": 0.85,
    "probabilidad_correcta": 0.85,
    "probabilidad_exceso": 0.15
  },
  "recomendacion": {
    "mensaje": "...",
    "calorias_estimadas": 450,
    "gramos_estimados": 350,
    "accion": "continuar"
  }
}
```

## 💻 Estructura de Código

### Nuevas funciones JavaScript necesarias:

1. `subirImagen()` - Maneja la selección de archivo
2. `analizarImagen(file, datosUsuario)` - Envía imagen al backend
3. `mostrarResultadosAnalisis(resultado)` - Muestra resultados en UI
4. `obtenerDatosUsuario()` - Obtiene IMC del usuario desde localStorage o calculadora
5. `mostrarVistaAnalisis()` - Muestra vista de análisis

## 🎨 Componentes UI a Crear

1. **Input de imagen**:
   - Input file oculto
   - Botón estilizado para subir
   - Vista previa de imagen
   - Drag & drop zone

2. **Tarjeta de resultados**:
   - Indicador visual (verde/amarillo/rojo)
   - Porción correcta/exceso
   - Confianza del modelo
   - Calorías estimadas
   - Recomendaciones

3. **Estados de carga**:
   - Spinner mientras procesa
   - Mensaje "Analizando imagen..."

## 📝 Flujo de Usuario

```
1. Usuario calcula su IMC (o ya lo tiene guardado)
   ↓
2. Usuario hace clic en botón de cámara o "Analizar comida"
   ↓
3. Selecciona/sube imagen de comida
   ↓
4. Se muestra vista previa de imagen
   ↓
5. Usuario hace clic en "Analizar"
   ↓
6. Se muestra estado de carga
   ↓
7. Backend procesa imagen con IA
   ↓
8. Se muestran resultados:
   - Porción correcta/exceso
   - Confianza
   - Calorías estimadas
   - Recomendación personalizada
```

## 🔧 Mejoras de UX

- Feedback inmediato al subir imagen
- Animaciones suaves
- Mensajes claros y amigables
- Manejo de errores con mensajes útiles
- Guardar historial de análisis (localStorage)

## ⏭️ Siguiente Fase

Una vez completada la Fase 3, pasaremos a la **Fase 4: Integración Web3 - IPFS** donde guardaremos las imágenes de forma descentralizada.

## 📂 Archivos a Modificar

- `index.html` - Agregar nueva vista y componentes
- `styles.css` - Estilos para nuevos componentes
- JavaScript inline en `index.html` - Agregar funciones de integración

