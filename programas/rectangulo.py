# Programa: rectangulo.py
# Propósito: Cálcula el perímetro y el área de un rectángulo a partir de su altura y anchura.
# Autor: Juan Miguel
# Fecha: 30/03/20

# Petición de los datos (en metros)
altura = float(input('Dame la altura (en metros): '))
anchura = float(input('Dame la anchura (en metros): '))

# Cálculo del área y del perímetro
area = altura * anchura
perimetro = 2 * altura + 2 * anchura

# Impresión de resultados en pantalla
print('El perímetro es de {0:6.2f} metros'.format(perimetro)) # solo dos decimales
print('El área es de {0:6.2f} metros cuadrados'.format(area))
