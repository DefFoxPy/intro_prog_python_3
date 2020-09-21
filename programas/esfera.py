from math import pi

print('Programa para el cálculo del volumen de una esfera')

radio = float(input('Dame el radio (en metros): '))

volumen = 4 / 3 * pi * radio ** 3

print('Volumen: {0:.2f} metros cúbicos.'.format(volumen), end='')
print('Gracias por usar el programa. Adiós')