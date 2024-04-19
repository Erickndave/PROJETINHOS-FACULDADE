'''
Elaborar um programa que calcula o fatorial de um número
'''
fat = 1
num = int(input('Digite o núemro: '))
for i in range(num, 1, -1):
    fat *= i
print(f'O fatoreial de {num} é {fat}')