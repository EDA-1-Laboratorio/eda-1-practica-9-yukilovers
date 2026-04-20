'''
Completa el programa que usa math para calcular la distancia entre dos puntos en el plano y el área de un triángulo 
usando la fórmula de Herón:
'''

import math

def distancia(x1, y1, x2, y2):
    # Usamos math.sqrt para la raíz cuadrada y completamos la diferencia de y
    return math.sqrt( (x2 - x1)**2 + (y2 - y1)**2 )

def area_triangulo(x1, y1, x2, y2, x3, y3):
    # Calcular los tres lados reutilizando la función anterior
    a = distancia(x1, y1, x2, y2)
    b = distancia(x2, y2, x3, y3)
    c = distancia(x3, y3, x1, y1)

    # Fórmula de Herón: s = semiperímetro (suma de lados entre 2)
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

# Pruebas
print(f"Distancia (0,0)→(3,4): {distancia(0, 0, 3, 4)}")  # 5.0
print(f"Área del triángulo: {area_triangulo(0, 0, 4, 0, 0, 3):.2f}")  # 6.00
