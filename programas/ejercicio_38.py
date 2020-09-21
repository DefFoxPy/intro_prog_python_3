"""
Diseña un programa que pida el valor de los tres lados de un triángulo y calcule
el valor de su área y perímetro. Recuerda que el área A de un triángulo puede calcularse a
partir de sus tres lados, a, b y c, así: A = s(s − a)(s − b)(s − c), donde s = (a + b + c)/2.
(Prueba que tu programa funciona correctamente con este ejemplo: si los lados miden 3, 5 y 7,
el perímetro será 15.0 y el área 6.49519052838).
"""
from math import sqrt

lado_1 = float(input('Dame el lado 1 del triangulo: '))
lado_2 = float(input('Dame el lado 2 del triangulo:'))
lado_3 = float(input('Dame el lado 3 del triangulo: '))

perimetro = lado_1 + lado_2 + lado_3

# calculo del area
s = (lado_1 + lado_2 + lado_3) / 2
area = sqrt(s * (s - lado_1) * (s - lado_2) * (s - lado_3))

print("Perimetro:", perimetro)
print("Area:", area)