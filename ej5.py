listadivisa = {
    'euro':'€',
    'dollar':'$',
    'yen':'¥'
}

moneda = input('Introduzca una divisa ')

print(listadivisa[(moneda.lower())])
