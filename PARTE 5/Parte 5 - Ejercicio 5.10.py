'''
Ejercicio 5.10 — Opción múltiple
¿Qué imprime el siguiente código?
'''

tupla = (1, 2, 3)
lista = list(tupla)
lista.append(4)
print(tupla, lista)

'''
a) (1, 2, 3, 4) [1, 2, 3, 4]
b) (1, 2, 3) [1, 2, 3, 4]
c) Error: no se puede convertir una tupla a lista
d) (1, 2, 3) [1, 2, 3]
Respuesta: b) (1, 2, 3) [1, 2, 3, 4]
'''
