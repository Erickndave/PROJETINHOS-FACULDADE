'''
Dado um país A, com 5000000 de habitantes e uma taxa de natalidade de 3% ao ano,
e um país B com 7000000 de habitantes e uma taxa de natalidade de 2% ao ano, escrever
um programa em Python que seja capaz de calcular e iterativamente e no fim imprimir o
tempo necessário para que a população do país A ultrapasse a população do país B.
'''
countryA = 5000000
taxA = 1.03
countryB = 7000000
taxB = 1.02
anos = 0
while True:
    if countryA > countryB:
        print(f'A população do País A ultrapassou a do País B sendo respectivamente {countryA:.2f} e {countryB:.2f} ')
        break
    else:
        anos += 1
        countryA *= taxA
        print(f'A população do país A após {anos} é {countryA:.2f} ')
        countryB *= taxB
        print(f'A população do país B após {anos} é {countryB:.2f} ')
