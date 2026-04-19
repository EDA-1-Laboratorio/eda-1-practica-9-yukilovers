'''
Ejercicio 1.2 — Replica el ejemplo
Escribe y ejecuta el siguiente código que muestra la conversión entre tipos:
'''

# Conversión de tipos (casting)
entero = 7
flotante = float(entero)#Este numero entero lo convierte a decimal, cambiando de int a float.
print(flotante, type(flotante))   # Por eso imprime 7.0 <class 'float'>

cadena_num = "42"
numero = int(cadena_num)# int() lo convierte en numero real
print(numero, type(numero))       # 42 <class 'int'>

pi = 3.14159
entero_pi = int(pi)
print(entero_pi, type(entero_pi)) # int() no redondea solo corta los decimales, por lo tanto solo pone el 3,3 <class 'int'>

# bool también es numérico
print(True + True)    # 2
print(False + 10)     # 10
print(int(True))      # 1
print(int(False))     # 0
