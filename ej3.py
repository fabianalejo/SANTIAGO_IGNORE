n = int(input('Ingrese otro numero'))

if n < 4:
    print(f'Su nota {n} es muy deficiente')
elif n < 6:
    print(f'Su nota {n} es insuficiente')
elif n < 8:
    print(f'Su nota es suficiente')