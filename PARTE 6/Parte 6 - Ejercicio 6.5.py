'''
Ejercicio 6.5 — Completa el código
Escribe una función que reciba una lista de números y retorne dos listas: una con los números pares y otra con los impares.
'''
def separar_pares_impares(numeros):
    pares = []
    impares = []
    for n in numeros:
        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)
    return pares, impares

# Prueba
datos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
p, i = separar_pares_impares(datos)
print("Pares:", p)      # [2, 4, 6, 8, 10]
print("Impares:", i)    # [1, 3, 5, 7, 9]
'''
Salida:
Pares: [2, 4, 6, 8, 10]
Impares: [1, 3, 5, 7, 9]
'''
