'''
Escribe y ejecuta el siguiente código sobre ciclos anidados y patrones:
'''

# Ciclos anidados: tabla pitagórica
print("=== Tabla pitagórica (1-5) ===")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:4}", end="")
    print()

# Triángulo de asteriscos
print("\n=== Triángulo ===")
n = 5
for i in range(1, n + 1):
    print("*" * i)

# Triángulo invertido
print("\n=== Triángulo invertido ===")
for i in range(n, 0, -1):
    print("*" * i)

# Iterar sobre dos listas simultáneamente con zip
print("\n=== zip ===")
nombres = ["Ana", "Luis", "María"]
notas = [9.0, 7.5, 8.8]
for nombre, nota in zip(nombres, notas):
    estado = "Aprobado" if nota >= 8 else "Regular"
    print(f"  {nombre}: {nota} ({estado})")


'''
Ejecución del código en python:
=== Tabla pitagórica (1-5) ===
   1   2   3   4   5
   2   4   6   8  10
   3   6   9  12  15
   4   8  12  16  20
   5  10  15  20  25

=== Triángulo ===
*
**
***
****
*****

=== Triángulo invertido ===
*****
****
***
**


'''
