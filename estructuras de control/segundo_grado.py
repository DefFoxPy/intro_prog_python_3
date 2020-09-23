from math import sqrt

print('Programa para la resolución de la ecuación a x * x + b x + c = 0')

a = float(input('Valor de a: '))
b = float(input('Valor de b: '))
c = float(input('Valor de c: '))

x1 = (-b + sqrt(b**2 - 4*a*c)) / (2 * a)
x2 = (-b - sqrt(b**2 - 4*a*c)) / (2 * a)

print('Soluciones x1={0:.3f} y x2={1:.3f}'.format(x1, x2))