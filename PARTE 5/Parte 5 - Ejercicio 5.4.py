'''
Ejercicio 5.4 — Completa el código
Completa el siguiente programa que usa un diccionario para contar la frecuencia de cada letra en una cadena:
'''
texto = "abracadabra"
frecuencia = {}

for letra in texto:
    if letra in frecuencia:
        frecuencia[letra] = frecuencia[letra] + 1
    else:
        frecuencia[letra] = 1

print(frecuencia)
'''
Salid esperada:
{'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
'''
