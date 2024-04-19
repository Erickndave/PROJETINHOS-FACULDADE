'''
Criar um programa que pede dois números ao usuário. O
primeiro será o numerador, e o segundo será o expoente. A saída
do programa deve ser o resultado da operação numerador
elevado a expoente. Obs.: não usar função interna que calcula
automaticamente potência.
'''
base = int(input('Digite a base: '))
exp = int(input('Digite o expoente: '))

resultado = 1
for i in range(1, (exp + 1)):
    resultado *= base

print(f'O resultado é {resultado}')