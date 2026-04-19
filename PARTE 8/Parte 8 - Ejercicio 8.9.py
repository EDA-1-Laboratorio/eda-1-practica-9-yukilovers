'''
Ejercicio 8.9 — Completa el código
Completa el código que convierte un número decimal a binario usando un ciclo:
'''

def decimal_a_binario(n):
    if n == 0:
        return "0"
    binario = ""
    while n > 0:
        residuo = n % 2
        binario = str(residuo) + binario
        n = n // 2
    return binario

# Pruebas
print(decimal_a_binario(0))    # 0
print(decimal_a_binario(10))   # 1010
print(decimal_a_binario(255))  # 11111111
print(decimal_a_binario(42))   # 101010

