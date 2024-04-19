'''
Criar um programa que pede ao usuário 5 números, e informa
qual é o menor e qual é o maior deles.
'''
menor = 0
maior = 0
for i in range (5):
    num = input(f'Digite o {i + 1}° numero:')
    if menor == None:
        maior = num
        menor = num
    if num < menor:
        menor = num
    if num > maior:
        maior = num
print(f'O maior valor foi {maior} e o menor foi {menor}')