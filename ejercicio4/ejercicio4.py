# Escribe un programa que sea capaz de mostrar los números del 1 al 100 en orden inverso.

print('Numeros del 100 al 1')
numero = 100
while numero >= 1:
    if numero > 1:
        print(numero, end=', ')
    else:
        print(numero)
    numero = numero - 1
