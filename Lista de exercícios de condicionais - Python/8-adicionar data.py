'''
Implemente um programa que solicite uma data com hora, pedindo em separado: dia,
mês, ano, hora, minuto e segundo. Pergunte ao usuário que informação ele deseja
acrescentar, e em qual quantidade. Informar a nova data de acordo com o solicitado pelo
usuário.
Ex.: Informada a data 31/12/2001 23:59:59, se o usuário pedir para acrescentar um
segundo a data deve ser exibida como 01/01/2002 00:00:00.
Para determinar se um ano é bissexto, execute estas etapas:
1. Se o ano for uniformemente divisível por 4, vá para a etapa 2. Caso contrário, vá
para a etapa 5.
2. Se o ano for uniformemente divisível por 100, vá para a etapa 3. Caso contrário,
vá para a etapa 4.
3. Se o ano for uniformemente divisível por 400, vá para a etapa 4. Caso contrário,
vá para a etapa 5.
4. O ano é bissexto (tem 366 dias).
5. O ano não é um ano bissexto (tem 365 dias).
'''
#Solicitação de dados para o usuário
dia = int(input("Digite o dia:"))
mes = int(input("Digite o mês (SEM ZEROS À ESQUERDA):"))
ano = int(input("Digite o ano:"))
hor = int(input("Digite a hora:"))
min = int(input("Digite o minuto:"))
seg = int(input("Digite o segundo:")) 
#verificar se o ano é bissexto:
ano_bissexto =(ano % 4 == 0  and ano % 100 != 0) or (ano % 400 == 0)
#imprimir data inserida
print(f'Sua data inserida é {dia}/{mes}/{ano} às {hor}:{min}:{seg}')
#Solicitar qual informação o usuário quer adicionar e a quantidade
print('''Opções:
[1] - Segundo(s)
[2] - Minuto(s)
[3] - Hora(s)
[4] - Dia(s)
[5] - Mes(es)
[6] - Ano(s)
''')
info = int(input('Digite a opção que será adicionada: '))   
add = int(input("Digite a quantidade a ser adicionada: "))
if info == 1:
        seg =+ add
        if seg > 59:
              seg -= 59
              min += 1 
elif info == 2:
        min += add
        if min > 59:
              min -= 59
              hor += 1
elif info == 3:
        hor += add
        if hor > 24:
                hor = 0
                dia += 1
elif info == 4:
        dia += add
        if mes in [1,3, 5, 7, 8, 10]:
               if dia > 31:
                 dia -= 31
                 mes += 1
        elif mes in [4, 6, 9, 11]:
              if dia > 30:
                    dia -= 30
                    mes += 1
        elif mes == 2:
              if ano_bissexto and dia > 29:
                    dia -= 29
                    mes += 1
              elif not ano_bissexto and dia > 28:
                    dia -= 28
                    mes += 1
        if mes == 12:
              if dia > 31:
                    dia -= 31
                    mes = 1
                    ano += 1
elif info == 5:
    mes += add
    if mes > 12:
        mes -= 11
        ano += 1          
elif info == 6:   
        novo_ano = ano + add
#Verificar se o novo ano é bissexto
bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
print(f'Sua nova data é {dia}/{mes}/{ano} às {hor}:{min}:{seg}')
#verificar novamente a data 
if not bissexto and mes == 2 and dia == 29:
      dia = 28
#Printar a nova data
print(f'Sua nova data é {dia}/{mes}/{ano} às {hor}:{min}:{seg}') 