'''
Criar um programa que solicita um número ao usuário e exibe a
tabuada deste número de 1 a 10, no formato:
'''
num = int(input('Digite o número: '))

for i in range(1, 11):
    print(f'{num} * {i} = {num * i}')
    