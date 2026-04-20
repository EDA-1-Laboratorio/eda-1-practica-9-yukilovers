
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Slicing
print(numeros[2:5])     # [2, 3, 4]
print(numeros[:3])      # [0, 1, 2]     (primeros 3)
print(numeros[-3:])     # [7, 8, 9]     (últimos 3)
print(numeros[::2])     # [0, 2, 4, 6, 8]  (cada 2)
print(numeros[::-1])    # [9, 8, 7, ..., 0] (invertida)

# ¡CUIDADO con las copias!
# Asignación NO copia, ambas apuntan al mismo objeto
a = [1, 2, 3]
b = a
b[0] = 99
print("a:", a)  # a: [99, 2, 3]  ← ¡a también cambió!

# Para hacer una copia independiente:
c = [1, 2, 3]
d = c.copy()    # o también: d = c[:]
d[0] = 99
print("c:", c)  # c: [1, 2, 3]  ← c no cambió
print("d:", d)  # d: [99, 2, 3]

'''
Ejecución del código en python:


[2, 3, 4]
[0, 1, 2]
[7, 8, 9]
[0, 2, 4, 6, 8]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
a: [99, 2, 3]
c: [1, 2, 3]
d: [99, 2, 3]
'''
