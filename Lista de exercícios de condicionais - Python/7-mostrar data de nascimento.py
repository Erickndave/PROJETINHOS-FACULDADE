'''
Implemente um programa que solicite o dia, mês e ano (com 4 dígitos) de nascimento
de uma pessoa, e pergunte em qual formato deve exibir a data, como segue:
Código de Exibição de Data
• 1 – Data simples. Ex.: 10/08/1990;
• 2 – Data abreviada. Ex.: 10/ago/1990;
• 3 – Data completa. Ex.: 10 de agosto de 1990.
'''
dia = int(input('Digite o dia do seu nascimento (DOIS DÍGITOS): '))
mes = int(input('Digite o mês do seu nascimento (DOIS DÍGITOS): '))
ano = int(input('Digite o ano do seu nascimento (QUATRO DÍGITOS): '))

print('''Escolha a opção que você deseja ver sua data de nascimento:
[1] Data simples. Ex.: 10/08/1990
[2] Data abreviada. Ex.: 10/ago/1990     
[3] Data completa. Ex.: 10 de agosto de 1990 ''')
opcao = int(input('Digite a opção escolhida: '))
if opcao == 1:
    print(f'{dia}/{mes}/{ano}')
elif opcao == 2:
    if mes == 01:
        print(f'{dia}/jan/{ano}')
    elif mes == 02:
        print(f'{dia}/fev/{ano}')

