'''
Criar um Programa que simule um caixa eletrônico. O programa
deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas. A saber:
a. Notas disponíveis: 1, 5, 10, 50 e 100 reais;
b. Valor mínimo de saque: R$ 10,00 reais;
c. Valor máximo de saque: R$ 600,00 reais.
'''
#Variáveis para as notas
n100 = 0
n50 = 0
n10 = 0
n5 = 0
n1 = 0
#Laço de filtro de respostas
while True:
    saque = int(input('Digite o valor entre R$10,00 e R$600,00 para ser sacado: R$'))
    if saque < 10:
         print('Erro, O saque mínimo é de R$10,00')
    elif saque > 600:
         print('Erro, o saque mínimo é de R$600,00')
    elif saque == '':
         print('Por favor digite algum valor')
    else:
         break
#Laço infinito para fazer o cálculo de quais notas usar    
while True:
    if saque >= 100 and saque <= 600:
            n100 += 1
            saque -= 100
    elif saque >= 50 and saque < 100:
        n50 += 1 
        saque -=50
    elif saque >= 10 and saque < 50:
        n10 += 1 
        saque -= 10
    elif saque >= 5 and saque < 10:
        n5 += 1
        saque -= 5
    elif saque >= 1 and saque <5:
        n1 += 1 
        saque -= 1
    elif saque == 0:
        print(f'Foram sacadas:\n{n100} notas de 100 reais,\n{n50} notas de 50 reais, \n{n10} notas de 10 reias, \n{n5} notas de 5 reais,\n{n1} notas de 1 real')    
        break
