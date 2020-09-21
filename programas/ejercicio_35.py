"""
Diseña un programa que pida el valor del lado de un cuadrado y muestre el valor de
su perímetro y el de su área. (Prueba que tu programa funciona correctamente con este ejemplo:
si el lado vale 1.1, el perímetro será 4.4, y el área 1.21).
"""
lado_cuadrado = float(input('Dame el valor del lado del cuadrado: '))

perimetro = lado_cuadrado * 4
area = lado_cuadrado ** 2

print(f"Perimetro: {perimetro}")
print("Area: {0}".format(area))