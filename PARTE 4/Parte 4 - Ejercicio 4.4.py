'''
Ejercicio 4.4 — Completa el código
Dada la siguiente lista, completa el código para obtener la salida indicada:
'''
calificaciones = [8.5, 9.0, 7.5, 10.0, 6.0, 8.0]

# 1. Imprime la cantidad de calificaciones
print("Total:", len(calificaciones))

# 2. Imprime la calificación más alta
print("Máxima:", max(calificaciones))

# 3. Imprime la calificación más baja
print("Mínima:", min(calificaciones))

# 4. Imprime el promedio
print("Promedio:", (sum(calificaciones))/(len(calificaciones)))

# 5. Imprime las calificaciones ordenadas de menor a mayor
#    Pista: usa sorted()
print("Ordenadas:", sorted(calificaciones))
'''
Salida esperada:
Total: 6
Máxima: 10.0
Mínima: 6.0
Promedio: 8.166666666666666
Ordenadas: [6.0, 7.5, 8.0, 8.5, 9.0, 10.0]
'''
