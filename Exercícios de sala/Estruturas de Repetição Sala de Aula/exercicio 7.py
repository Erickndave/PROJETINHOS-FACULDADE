'''
Criar um programa que solicite ao usuário vários números e, ao
digitar 0, calcula a média destes números informados
'''
soma = 0
div = 0
sair = False
while not sair:
   try:
        num = int(input('Digite um número (0 faz a média): '))
        if num == 0:
            sair = True
        else:
            soma += num 
            div += 1
   except ValueError:
      print('Valor inválido') 
print(f'A média é {soma/div}')


