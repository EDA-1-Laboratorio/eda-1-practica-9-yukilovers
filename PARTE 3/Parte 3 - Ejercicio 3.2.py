'''
Ejercicio 3.2 — Replica el ejemplo
Escribe y ejecuta el siguiente código sobre operadores de asignación compuesta:
'''

# Operadores de asignación compuesta (igual que en C, excepto ++ y --)
x = 10
print("Valor inicial:", x)  # 10

x += 5     # x = x + 5
print("x += 5 →", x)       # 15

x -= 3     # x = x - 3
print("x -= 3 →", x)       # 12

x *= 2     # x = x * 2
print("x *= 2 →", x)       # 24

x //= 5   # x = x // 5
print("x //= 5 →", x)      # 4

x **= 3   # x = x ** 3
print("x **= 3 →", x)      # 64

x %= 10   # x = x % 10
print("x %= 10 →", x)       # 4

# ¡CUIDADO! NO existe ++ ni -- en Python
# i++   → Error de sintaxis
# i--   → Error de sintaxis
# Usa:  i += 1  o  i -= 1

'''
SALIDA:
Valor inicial: 10
x += 5 → 15
x -= 3 → 12
x *= 2 → 24
x //= 5 → 4
x **= 3 → 64
x %= 10 → 4
'''
