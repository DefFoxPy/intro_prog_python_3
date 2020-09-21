"""
Diseña un programa que pida el valor de los dos lados de un rectángulo y muestre
el valor de su perímetro y el de su área. (Prueba que tu programa funciona correctamente con
este ejemplo: si un lado mide 1 y el otro 5, el perímetro será 12.0, y el área 5.0).
"""
lado_1 = float(input('Dame el lado 1 del rectangulo: '))
lado_2 = float(input('Dale el lado 2 del rectangulo: '))

perimetro = lado_1 * 2 + lado_2 * 2
area = lado_1 * lado_2

print("Perimetro:", perimetro)
print("Area %.2f" % area)