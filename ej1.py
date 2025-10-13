n1 = int(input('Introduzca un numero '))
n2 = int(input('Introduzca otro numero '))
n3 = int(input('Introduzca un numero mas '))

if n1>n2 and n1>n3:
    print(f'El numero mas grande es {n1}')
elif n2>n3:
    print(f'El numero mas grande es {n2}')
else:
    print(f'El numero mas grande es {n3}')

