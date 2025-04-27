#Calculo del consumo del agua por persona
litros_totales = float(input("Ingrese el total de litros consumidos en un mes en la vivienda: "))
personas = int(input("Ingrese la cantidad de personas que viven en la casa: "))

consumo_mensual_por_persona = litros_totales / personas
consumo_diario_por_persona = consumo_mensual_por_persona / 30

print("\n--- Resumen del Consumo de Agua ---")
print("Consumo total del mes: ", litros_totales, "litros")
print("Cantidad de personas en la vivienda: ", personas)
print("Consumo mensual por persona: ", round(consumo_mensual_por_persona, 2), "litros")
print("Consumo diario por persona: ", round(consumo_diario_por_persona, 2), "litros")