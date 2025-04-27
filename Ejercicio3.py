#Calculo de interes compuesto
capital_inicial = float(input("Ingrese el capital inicial: "))
tasa_interes = float(input("Ingrese la tasa de interés anual (en porcentaje): "))
años = int(input("Ingrese la cantidad de años: "))

tasa_decimal = tasa_interes / 100
valor = (1 + tasa_decimal) ** años
monto_final = capital_inicial * valor
interes_ganado = monto_final - capital_inicial


print("\nCapital inicial: $", capital_inicial)
print("Tasa de interés anual: ", tasa_interes, "%")
print("Años: ", años)
print("Monto final: $", round(monto_final, 2))
print("Interés ganado: $", round(interes_ganado, 2))