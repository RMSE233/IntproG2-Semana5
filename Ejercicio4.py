#Calculo del consumo de combustible
distancia = float(input("Ingrese la distancia recorrida en kilómetros: "))
litros_consumidos = float(input("Ingrese la cantidad de litros consumidos: "))

rendimiento = distancia / litros_consumidos
precio_por_litro = 1.30  # Puedes cambiar este valor según el precio real
gasto_total = litros_consumidos * precio_por_litro

print("\n--- Resumen del Consumo de Combustible ---")
print("Distancia recorrida: ", distancia, "km")
print("Litros consumidos: ", litros_consumidos, "litros")
print("Precio por litro: $", precio_por_litro)
print("Rendimiento del vehículo: ", round(rendimiento, 2), "km/l")
print("Gasto total en combustible: $", round(gasto_total, 2))

