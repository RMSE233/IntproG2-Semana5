Calificacion1 = int(input("Ingrese la calificacion 1: "))
Calificacion2 = int(input("Ingrese la calificacion 2: "))
Calificacion3 = int(input("Ingrese la calificacion 3: "))
Suma = Calificacion1 + Calificacion2 + Calificacion3
Promedio = Suma / 3

print(f"""Calificacion 1: {Calificacion1:>3}
          Calificacion 2: {Calificacion2:>3}
          Calificacion 3: {Calificacion3:>3}
          {"Promedio":<15} {Promedio:>3.0f}""")

