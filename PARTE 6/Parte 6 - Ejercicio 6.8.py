'''
Ejercicio 6.8 — Completa el código
Completa la función recursiva que calcula la potencia de un número:
'''

def potencia_recursiva(base, exponente):
    # Caso base: cualquier número elevado a 0 es 1
    if exponente == 0:
        return 1
    
    # Paso recursivo: base * base^(exponente - 1)
    return base * potencia_recursiva(base, exponente - 1)

# Pruebas
print(potencia_recursiva(2, 10))   # 1024
print(potencia_recursiva(3, 4))    # 81
print(potencia_recursiva(5, 0))    # 1
