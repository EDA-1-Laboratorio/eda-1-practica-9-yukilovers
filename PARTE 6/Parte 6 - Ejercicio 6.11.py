'''
Ejercicio 6.11 — Variables globales y locales (II)
Estudia el siguiente código y sin ejecutarlo, predice qué se imprime:
'''

contador = 0

def incrementar():
    global contador
    contador += 1

incrementar()
incrementar()
incrementar()
print("Contador:", contador)

# Tu predicción: Contador = 3
