"""
Servicio para cálculos nutricionales y recomendaciones
"""

class NutricionService:
    """Servicio para generar recomendaciones nutricionales"""
    
    def __init__(self):
        pass
    
    def generar_recomendaciones(self, imc, categoria, calorias):
        """
        Genera recomendaciones nutricionales basadas en IMC
        
        Args:
            imc: Índice de masa corporal
            categoria: Categoría del IMC (Bajo peso, Normal, etc.)
            calorias: Calorías diarias recomendadas
            
        Returns:
            dict: Recomendaciones nutricionales
        """
        # Distribución de calorías por comida (aproximada)
        cal_desayuno = int(calorias * 0.25)
        cal_almuerzo = int(calorias * 0.35)
        cal_cena = int(calorias * 0.25)
        cal_snacks = calorias - cal_desayuno - cal_almuerzo - cal_cena
        
        # Recomendaciones según categoría
        if categoria == "Bajo peso":
            desayuno = {
                "descripcion": "Avena con frutas, nueces y miel",
                "calorias": cal_desayuno,
                "proteinas": int(cal_desayuno * 0.15 / 4)
            }
            almuerzo = {
                "descripcion": "Pasta integral con pollo y verduras",
                "calorias": cal_almuerzo,
                "proteinas": int(cal_almuerzo * 0.25 / 4)
            }
            cena = {
                "descripcion": "Salmón a la plancha con quinoa y vegetales",
                "calorias": cal_cena,
                "proteinas": int(cal_cena * 0.30 / 4)
            }
            snacks = ["Batido de proteína", "Almendras y frutos secos", "Yogurt griego con granola"]
            tips = [
                "💧 Bebe al menos 2.5 litros de agua",
                "🏋️ Realiza entrenamiento de fuerza",
                "🍽️ Come 5-6 comidas pequeñas al día",
                "📊 Aumenta gradualmente las porciones"
            ]
        elif categoria == "Normal":
            desayuno = {
                "descripcion": "Yogurt natural con frutas frescas y granola",
                "calorias": cal_desayuno,
                "proteinas": int(cal_desayuno * 0.18 / 4)
            }
            almuerzo = {
                "descripcion": "Pechuga de pollo a la plancha, ensalada y arroz",
                "calorias": cal_almuerzo,
                "proteinas": int(cal_almuerzo * 0.28 / 4)
            }
            cena = {
                "descripcion": "Pescado al vapor con verduras asadas",
                "calorias": cal_cena,
                "proteinas": int(cal_cena * 0.30 / 4)
            }
            snacks = ["Frutas frescas variadas", "Almendras (30g)", "Zanahoria con hummus"]
            tips = [
                "💧 Bebe al menos 2 litros de agua",
                "🏃 Realiza actividad física regular",
                "😴 Duerme entre 7-8 horas",
                "📒 Lleva un registro alimenticio"
            ]
        else:  # Sobrepeso u Obesidad
            desayuno = {
                "descripcion": "Huevos revueltos con espinacas y tostada integral",
                "calorias": cal_desayuno,
                "proteinas": int(cal_desayuno * 0.25 / 4)
            }
            almuerzo = {
                "descripcion": "Ensalada grande con pollo a la plancha",
                "calorias": cal_almuerzo,
                "proteinas": int(cal_almuerzo * 0.30 / 4)
            }
            cena = {
                "descripcion": "Pescado blanco con verduras al vapor",
                "calorias": cal_cena,
                "proteinas": int(cal_cena * 0.35 / 4)
            }
            snacks = ["Manzana", "Yogurt griego sin azúcar", "Pepino con limón"]
            tips = [
                "💧 Bebe 2-2.5 litros de agua",
                "🚶 Camina al menos 30 minutos diarios",
                "🍽️ Controla el tamaño de las porciones",
                "⏰ Evita comer 3 horas antes de dormir"
            ]
        
        return {
            "desayuno": desayuno,
            "almuerzo": almuerzo,
            "cena": cena,
            "snacks": snacks,
            "tips": tips
        }
    
    def generar_recomendacion_porcion(self, analisis, imc, calorias_objetivo, objetivo):
        """
        Genera recomendaciones específicas basadas en el análisis de la porción
        
        Args:
            analisis: Resultado del análisis de la imagen
            imc: IMC del usuario
            calorias_objetivo: Calorías objetivo diarias
            objetivo: Objetivo del usuario (mantener/perder/ganar peso)
            
        Returns:
            dict: Recomendación personalizada
        """
        porcion_correcta = analisis['porcion_correcta']
        confianza = analisis['confianza']
        
        # Estimar calorías (aproximado basado en la porción)
        # Una porción "correcta" promedio tiene ~400-500 cal
        # Un exceso tiene ~700-900 cal
        if porcion_correcta:
            calorias_estimadas = 450
            gramos_estimados = 350
        else:
            calorias_estimadas = 800
            gramos_estimados = 600
        
        # Generar mensaje según el análisis y objetivo
        if porcion_correcta:
            if objetivo in ["mantener peso", "mantener"]:
                mensaje = "Porción adecuada para tu objetivo calórico. Perfecto para mantener tu peso."
                accion = "continuar"
            elif objetivo in ["perder peso", "adelgazar"]:
                mensaje = "Porción adecuada. Ideal para tu objetivo de pérdida de peso."
                accion = "continuar"
            else:  # ganar peso
                mensaje = "Porción adecuada, pero podrías considerar aumentar un poco más para ganar peso."
                accion = "aumentar_ligeramente"
        else:  # exceso
            if objetivo in ["mantener peso", "mantener"]:
                porcentaje_reduccion = int((calorias_estimadas - calorias_objetivo / 3) / calorias_estimadas * 100)
                mensaje = f"Porción excesiva ({calorias_estimadas} cal). Para mantener peso, reduce aproximadamente un {porcentaje_reduccion}% de esta porción."
                accion = "reducir"
            elif objetivo in ["perder peso", "adelgazar"]:
                porcentaje_reduccion = int((calorias_estimadas - (calorias_objetivo / 3 - 100)) / calorias_estimadas * 100)
                mensaje = f"Porción excesiva ({calorias_estimadas} cal). Para perder peso, reduce aproximadamente un {porcentaje_reduccion}% de esta porción."
                accion = "reducir_significativamente"
            else:  # ganar peso
                mensaje = "Porción grande, pero adecuada para tu objetivo de ganar peso."
                accion = "continuar"
        
        return {
            "mensaje": mensaje,
            "calorias_estimadas": calorias_estimadas,
            "gramos_estimados": gramos_estimados,
            "accion": accion,
            "calorias_diarias_objetivo": calorias_objetivo,
            "calorias_restantes_aproximadas": max(0, calorias_objetivo - calorias_estimadas)
        }

