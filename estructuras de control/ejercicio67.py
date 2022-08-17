"""
Realiza un programa que calcule el desglose mínimo en billetes y monedas de una
cantidad exacta de euros. Hay billetes de 500, 200, 100, 50, 20, 10 y 5 ¤ y monedas de 2 y 1 ¤.
Por ejemplo, si deseamos conocer el desglose de 434 ¤, el programa mostrará por pantalla
el siguiente resultado:
(¿Que cómo se efectúa el desglose mínimo? Muy fácil. Empieza por calcular la división entera
entre la cantidad y 500 (el valor de la mayor moneda): 434 entre 500 da 0, así que no hay billetes
de 500 ¤ en el desglose; divide a continuación la cantidad 434 entre 200, cabe a 2 y sobran 34,
así que en el desglose hay 2 billetes de 200 ¤; dividimos a continuación 34 entre 100 y vemos
que no hay ningún billete de 100 ¤
"""
DINERO = (500, 200, 100, 50, 20, 10, 5, 2, 1)

monto = int(input('Ingrese la cantidad de dinero a desglozar: '))

for cantidad in DINERO:
	cantidad_billetes = 0

	while monto >= cantidad:
		cantidad_billetes = monto // cantidad
		monto = monto % cantidad
	
	if cantidad_billetes != 0:
		print(f'{cantidad_billetes} de {cantidad} euros.')