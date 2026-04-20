
'''
Escribe y ejecuta el siguiente código sobre break, continue y else en ciclos:
'''

# break: salir del ciclo prematuramente
print("=== break ===")
for i in range(10):
    if i == 5:
        print("¡Llegué a 5, me detengo!")
        break
    print(i, end=" ")
print()

# continue: saltar a la siguiente iteración
print("\n=== continue ===")
for i in range(10):
    if i % 2 == 0:
        continue    # Salta los pares
    print(i, end=" ")
print()
# Imprime: 1 3 5 7 9

# else en ciclo for (¡no existe en C!)
# El bloque else se ejecuta si el ciclo terminó SIN break
print("\n=== for-else ===")
numeros = [2, 4, 6, 8]
for n in numeros:
    if n % 2 != 0:
        print(f"Encontré un impar: {n}")
        break
else:
    print("Todos los números son pares")
# Imprime: Todos los números son pares


'''
Ejecución del código en python:

=== break ===
0 1 2 3 4 ¡Llegué a 5, me detengo!


=== continue ===
1 3 5 7 9 

=== for-else ===
Todos los números son pares
'''
