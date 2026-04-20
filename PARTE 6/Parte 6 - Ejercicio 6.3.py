'''
Escribe y ejecuta el siguiente código sobre funciones lambda (anónimas):
'''

# Función lambda: función de una sola expresión
doble = lambda x: x * 2
print(doble(5))   # 10

# Útil para ordenar con criterio personalizado
alumnos = [
    {"nombre": "Carlos", "promedio": 8.5},
    {"nombre": "Ana", "promedio": 9.2},
    {"nombre": "Luis", "promedio": 7.8},
]

# Ordenar por promedio (de mayor a menor)
alumnos_ordenados = sorted(alumnos, key=lambda a: a["promedio"], reverse=True)
for a in alumnos_ordenados:
    print(f"  {a['nombre']}: {a['promedio']}")

# map: aplica una función a cada elemento
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, numeros))
print("Cuadrados:", cuadrados)   # [1, 4, 9, 16, 25]

# filter: filtra elementos que cumplen una condición
pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Pares:", pares)           # [2, 4]

'''
Ejecución del código en python:
10
  Ana: 9.2
  Carlos: 8.5
  Luis: 7.8
Cuadrados: [1, 4, 9, 16, 25]
Pares: [2, 4]

'''
