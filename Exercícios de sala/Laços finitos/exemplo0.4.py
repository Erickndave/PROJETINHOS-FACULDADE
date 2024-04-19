'''
pedir infinitos números para o usuário e somá-los
'''
soma = 0
sair = False
while not(sair):
    num = int(input('Digite um número para somar: '))
    if num == 0:
        sair = True
    else:
        soma += num
print(f'A soma dos número é {soma}')