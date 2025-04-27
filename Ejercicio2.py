#Control de inventario de un producto
Inventario_inicial = int(input("Ingrese el inventario inicial del producto: "))
Productos_recibidos = int(input("Ingrese la cantidad de productos recibidos:"))
Productos_vendidos = int(input("Ingrese la cantidad de productos vendidos: "))

Inventario_total = Inventario_inicial + Productos_recibidos

Inventario_actual = Inventario_total - Productos_vendidos

print("\n--- Resumen del Inventario ---")
print("Inventario inicial:", Inventario_inicial)
print("Productos recibidos:", Productos_recibidos)
print("Productos vendidos:", Productos_vendidos)
print("Inventario final disponible:", Inventario_actual)
