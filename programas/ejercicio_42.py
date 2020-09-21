"""
Diseña un programa legible que solicite el radio de una circunferencia y muestre su
área y perímetro con solo 2 decimales.
"""
from math import pi

print('Programa que calcula área y perímetro de una circuferencia conociendo el radio')

# Petición de los datos
radio = float(input('Ingrese el radio de la circunferencia: '))

# Cálculo del área y perímetro 
perimetro = 2 * pi * radio
area = pi * radio ** 2

# Impresión de resultados por pantalla
print('Area de la circunferencia: {0:.2f}'.format(area))
print('Perímetro de la circunferencia: {0:.2f}'.format(perimetro))
