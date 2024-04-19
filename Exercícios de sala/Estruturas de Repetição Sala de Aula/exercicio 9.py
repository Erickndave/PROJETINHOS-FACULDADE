'''
Criar um programa que simula um carrinho de compras, onde
solicita o nome do produto (não pode ser vazio), o valor deste
produto (valor com vírgula, positivo) e a quantidade deste
produto a ser comprada (valor inteiro, positivo). Ao incluir um
produto, deve perguntar se o usuário deseja fechar o pedido ou
incluir mais produtos. Todos os dados devem ser validados. Ao
final da compra, deve ser informado o valor total do pedido.
'''
carrinho = []
while True:
     try:
        #Adicionar novo produto ou encerrar
        option = int(input("Digite uma das opções:\n[1] - Adicionar novo produto ao carrinho\n[2] - Concluir carrinho\n"))    
        #Solicitar informações ao usuário 
        if option == 1:
            produto = input('Digite o nome do produto: ')
            quant = int(input('Digite a quantidade desse produto: '))
            valor = float(input('Digite o valor do produto: '))
            #Filtrando algumas respostas inválidas
            if produto == '':
                print('Por favor insira um nome para o seu produto.')
                continue
            if quant < 0:
                print('Por favor digite um número inteiro e positivo para a quantidade.')
                continue
            if valor < 0:
                print('Por favor digite um valor decimal com "." e positivo para o valor.')
                continue
            #Salvar os produtos dentro de uma lista
            carrinho.append((quant, valor))
        if option == 2:
            total = sum(valor * quantidade for valor, quantidade in carrinho) 
            print(f'O valor total da sua compra ficou R${total:.2f}')
            break
     except ValueError:
         print('Algum dado está errado, tente novamente')
         continue