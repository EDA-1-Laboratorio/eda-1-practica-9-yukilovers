'''
Ejercicio 6.9 — Completa el código
Completa la función que elimina los duplicados de una lista manteniendo el orden original:
'''

def eliminar_duplicados(lista):
    vistos = set(lista)     # Pista: usa un conjunto (set)
    resultado = []
    for elemento in lista:
        if elemento in vistos:
            resultado.append(elemento)
            vistos.remove(elemento)
    return resultado

# Pruebas
print(eliminar_duplicados([1, 3, 2, 1, 5, 3, 2, 4]))
# [1, 3, 2, 5, 4]
print(eliminar_duplicados(["a", "b", "a", "c", "b"]))
# ['a', 'b', 'c']
