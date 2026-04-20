'''
Ejercicio 2.5 — Completa el código
Completa el código para generar un acrónimo a partir de una frase:
Salida esperada:
EDDYA
'''
frase = "Estructura de Datos y Algoritmos"

palabras = frase.split()   # Dividir la frase en palabras
acronimo = ""

for palabra in palabras:
    acronimo = acronimo + palabra[0].upper()   # Primera letra en mayúscula

print(acronimo)
