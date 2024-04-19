'''
Calcular o fatorial de um número usando laço infinito
'''
num = int(input('Digite o núemro: '))
fat = 1
cont = 0
while True:
    cont += 1
    if cont > num:
        break
    else:
        fat *= cont
print(f"O fatorial de {num} é {fat}")