'''
Criar um programa que solicita ao usuário 10 números, contando
quantos são pares e quantos são ímpares. Informar ao final estas
informações.
'''
cont_par = 0
cont_imp = 0
for i in range(10):
    num = int(input('Digite o '+ str(i + 1) +'° número: '))
    if num % 2 == 0:
        cont_par += 1
    elif num % 2 ==1:
        cont_imp += 1
print(f'{cont_par} são pares e {cont_imp} são ímpares')