'''
Ejercicio 4.5 — Completa el código
Completa el código que combina dos listas en una lista de tuplas (como un "zip"):
'''
nombres = ["Ana", "Luis", "María", "Pedro"]
edades = [20, 22, 19, 21]

# Combinar usando zip()
combinada = list(zip(nombres, edades))
print(combinada)
# [('Ana', 20), ('Luis', 22), ('María', 19), ('Pedro', 21)]

# Encontrar el nombre de la persona más joven
edad_minima = min(edades)
indice_joven = edades.index(edad_minima)
print(f"El más joven es {nombres[indice_joven]} con {edad_minima} años")
'''
Salida esperada:
[('Ana', 20), ('Luis', 22), ('María', 19), ('Pedro', 21)]
El más joven es María con 19 años
'''
