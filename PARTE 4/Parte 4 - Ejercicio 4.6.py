'''
Completa el código que usa list comprehension para filtrar y transformar datos:
'''

temperaturas_f = [32, 50, 68, 86, 104, 212]

# Convertir todas a Celsius: C = (F - 32) * 5/9
temperaturas_c = [(f-32)*5/9 for f in temperaturas_f]
print("En Celsius:", temperaturas_c)

# Filtrar solo las temperaturas menores a 50°C
frias = [c for c in temperaturas_c if c<50]
print("Menores a 50°C:", frias)

En Celsius: [0.0, 10.0, 20.0, 30.0, 40.0, 100.0]
Menores a 50°C: [0.0, 10.0, 20.0, 30.0, 40.0]
