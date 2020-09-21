"""
Objetivo: Haz un programa que pida al usuario una cantidad de euros, una tasa de interés
y un número de años. Muestra por pantalla en cuánto se habrá convertido el capital inicial
transcurridos esos años si cada año se aplica la tasa de interés introducida.
Recuerda que un capital de C euros a un interés del x por cien durante n años se convierten
en C · (1 + x/100)n euros. (Prueba tu programa sabiendo que una cantidad de 10,000 ¤ al 4.5 %
de interés anual se convierte en 24,117.14 ¤ al cabo de 20 años).
"""
print('Programa que calcula el capital final trans invertir un capital inicial a una tasa de interes\n por n años')

capital_inicial = float(input('Ingrese el capital inicial: '))
tasa_interes = float(input('Ingres la tasa de interes: '))
numero_anios = int(input('Ingrese el numero de anios: '))

capital_final = capital_inicial * (1 + tasa_interes/100) ** numero_anios

print('El capital final es: {0:.2f}'.format(capital_final))