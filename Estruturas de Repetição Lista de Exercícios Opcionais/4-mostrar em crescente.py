'''
Peça 5 números ao usuário. Fazendo uso de laços, organize e mostre eles em ordem
crescente
'''
n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))
n3 = int(input('Digite o 3° número: '))
n4 = int(input('Digite o 4° número: '))
n5 = int(input('Digite o 5° número: '))          
for _ in range(4):
    if n1 > n2:
        aux = n1
        n1 = n2
        n2 = aux
    if n2 > n3:
        aux = n2
        n2 = n3
        n3 = aux    
    if n3 > n4:
        aux = n3
        n3 = n4
        n4 = aux
    if n4 > n5:
        aux = n4
        n4 = n5
        n5 = aux
print(f'Números em ordem crescente: {n1}, {n2}, {n3}, {n4}, {n5}')