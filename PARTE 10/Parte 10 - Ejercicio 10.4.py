'''
Ejercicio 10.4 — Completa el código
Completa el siguiente programa que simula el lanzamiento de un dado 1000 veces y cuenta cuántas veces sale cada cara:
'''
import random

resultados = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

for _ in range(1000):
    dado = random.randint(1, 6)
    resultados[dado] += 1

print("Resultados de 1000 lanzamientos:")
for cara, conteo in resultados.items():
    print(f"  Cara {cara}: {conteo} veces")
'''
Salida: 
Resultados de 1000 lanzamientos:
  Cara 1: 164 veces
  Cara 2: 163 veces
  Cara 3: 180 veces
  Cara 4: 142 veces
  Cara 5: 177 veces
  Cara 6: 174 veces
'''
