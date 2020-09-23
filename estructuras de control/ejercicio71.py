"""
Diseña un programa Python que lea un carácter cualquiera desde el teclado, y muestre
el mensaje « » cuando el carácter sea una letra mayúscula y el mensaje «
» cuando sea una minúscula. En cualquier otro caso, no mostrará mensaje alguno.
(Considera únicamente letras del alfabeto inglés). Pista: aunque parezca una obviedad, recuerda
que una letra es minúscula si está entre la y la , y mayúscula si está entre la y la
"""

def main():
    letra = input('Ingrese una letra: ')

    if 'a' <= letra and 'z' >= letra:
        print('La letra es minúscula')

    elif 'A' <= letra and 'Z' >= letra:
        print('La letra es Mayúscula.')

    else:
        print('No es una letra')


if __name__ == '__main__':
    print('Programa que determina si una letra es mayuscula o minuscula')
    main()
