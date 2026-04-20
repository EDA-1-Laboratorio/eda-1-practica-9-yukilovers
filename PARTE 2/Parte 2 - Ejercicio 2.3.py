'''
Ejercicio 2.3 — Replica el ejemplo
Escribe y ejecuta este código sobre slicing (rebanado) de cadenas:
'''

texto = "Python es genial"

# Slicing: texto[inicio:fin]  (fin NO se incluye)
print(texto[0:6])    # Python
print(texto[7:9])    # es
print(texto[10:])    # genial  (desde índice 10 hasta el final)
print(texto[:6])     # Python  (desde el inicio hasta índice 5)

# Índices negativos (cuenta desde el final)
print(texto[-6:])    # genial
print(texto[-6:-1])  # genia

# Slicing con paso: texto[inicio:fin:paso]
print(texto[::2])    # Pto sgna  (cada 2 caracteres)

# Invertir una cadena (¡muy útil!)
print(texto[::-1])   # laineg se nohtyP

# Repetir cadenas con *
print("ja" * 3)      # jajaja
print("-" * 30)      # ------------------------------

'''
SALIDA:
Python
es
genial
Python
genial
genia
Pto sgna
laineg se nohtyP
jajaja
'''
