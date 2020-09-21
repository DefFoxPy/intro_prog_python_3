"""
El área A de un triángulo se puede calcular a partir del valor de dos de sus lados, a y
b, y del ángulo θ que estos forman entre sí con la fórmula A = 1
2ab sin(θ). Diseña un programa
que pida al usuario el valor de los dos lados (en metros), el ángulo que estos forman (en grados),
y muestre el valor del área.

(Ten en cuenta que la función sin de Python trabaja en radianes, así que el ángulo que leas en
grados deberás pasarlo a radianes sabiendo que π radianes son 180 grados. Prueba que has
hecho bien el programa introduciendo los siguientes datos: a = 1, b = 2, θ = 30; el resultado
es 0.5).
"""
from math import pi, sin

print('Este programa calcula el area de un triangulo.')

a = float(input('Ingrese el valor del lado 1(metros): '))
b = float(input('Ingrese el valor del lado 2(metros): '))
angulo = float(input('Ingrese el angulo de separación(grados): '))

angulo = (angulo * pi) / 180 # Conversión de grados a raidanes

area = 1 / 2 * a * b * sin(angulo)

print('Area del triangulo {0:.2f} metros cuadrados'.format(area))
