'''
Ejercicio 3.3 — Replica el ejemplo
Escribe y ejecuta el siguiente código que muestra particularidades de los operadores en Python:
'''

# Comparaciones encadenadas (¡no existen en C!)
edad = 20
print(18 <= edad <= 25)    # True  (en C: edad >= 18 && edad <= 25)

nota = 8.5
print(6.0 <= nota <= 10.0) # True

# Operador "in" (no existe en C)
vocales = "aeiou"
print("a" in vocales)      # True
print("x" in vocales)      # False

# Operador is (identidad, no igualdad)
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a == b)   # True  (mismo contenido)
print(a is b)   # False (distintos objetos en memoria)
print(a is c)   # True  (mismo objeto en memoria)

# Operador * con cadenas y listas
print("hola " * 3)         # hola hola hola
print([0] * 5)             # [0, 0, 0, 0, 0]

'''
SALIDA:
True
True
True
False
True
False
True
hola hola hola
[0, 0, 0, 0, 0]
'''
