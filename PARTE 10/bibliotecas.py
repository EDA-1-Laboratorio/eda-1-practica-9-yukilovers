'''
Crea un archivo bibliotecas.py:
'''

import math
import random

# Biblioteca math
print("=== math ===")
print("Pi:", math.pi)
print("e:", math.e)
print("sqrt(144):", math.sqrt(144))
print("ceil(4.2):", math.ceil(4.2))
print("floor(4.8):", math.floor(4.8))
print("log2(1024):", math.log2(1024))

# Biblioteca random
print("\n=== random ===")
print("Entero aleatorio [1, 10]:", random.randint(1, 10))
print("Flotante aleatorio [0, 1):", random.random())

colores = ["rojo", "verde", "azul", "amarillo"]
print("Elección aleatoria:", random.choice(colores))

random.shuffle(colores)
print("Lista mezclada:", colores)

'''
Ejecución del código 
=== random ===
Entero aleatorio [1, 10]: 6
Flotante aleatorio [0, 1): 0.914987957735843
Elección aleatoria: amarillo
Lista mezclada: ['amarillo', 'rojo', 'verde', 'azul']
'''
