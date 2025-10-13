n = int(input('Ingrese un numero '))

if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
    print('Su numero es divisible por 2, 3, 5 o 7')
else:
    print('Su numero no es divisible por 2, 3, 5 o 7')