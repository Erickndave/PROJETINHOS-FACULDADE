'''
Criar um programa que pede para o usuário inserir um login e uma
senha. Caso os valores sejam iguais, informar que os dados são
inválidos e pedir novamente as informações. Caso contrário, exibir a
mensagem "Bem-vindo ao sistema!!!".
'''
while True:
    login = input('Digite seu login: ')
    senha = input('Digite sua senha: ')
    if senha == login:
        print('Dados inválidos')
    else:
        print('Bem-vindo ao sistema')
        break