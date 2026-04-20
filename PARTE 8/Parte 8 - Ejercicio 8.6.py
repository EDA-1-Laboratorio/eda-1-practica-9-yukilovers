'''
Completa el programa que genera la secuencia de Fibonacci 
hasta un límite:
'''



def fibonacci(limite):
    secuencia = []
    a, b = 0, 1
    while a < limite:
        secuencia.append(a)
        a, b = b,a+b
    return secuencia

# Pruebas
print(fibonacci(50))
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

print(fibonacci(100))
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

