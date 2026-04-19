'''
Ejercicio 6.10 — Variables globales y locales (I)
Estudia el siguiente código y sin ejecutarlo, predice qué se imprime. Luego verifica ejecutándolo.
'''

x = 100  # Variable global

def modificar():
    x = 50   # Variable local (¡no modifica la global!)
    print("Dentro de la función, x =", x)

modificar()
print("Fuera de la función, x =", x)

'''
Tu predicción:

Dentro de la función, x = 50
Fuera de la función, x = 100
'''
