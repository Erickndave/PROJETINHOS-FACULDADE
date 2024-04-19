'''
Progrqama que soma10 números usando laços
'''
soma = 0
for contador in range(0, 10): #range(0, 10) range(10) range(0, 10, 1)
    num = int(input('Digite umnúmero: '))
    soma += num
print(f'A soma dos números é {soma}')