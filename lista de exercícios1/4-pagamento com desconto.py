'''Implemente um programa que calcule o que deve ser pago por um produto,
considerando o preço normal de etiqueta e a escolha da condição de pagamento. Utilize
os códigos da tabela a seguir para ler qual a condição de pagamento escolhida e efetuar o
cálculo adequado.
Código Condição de pagamento
• 1 – À vista em dinheiro ou cheque, recebe 10% de desconto
• 2 – À vista no cartão de crédito, recebe 15% de desconto
• 3 – Em duas vezes, preço normal de etiqueta sem juros
• 4 – Em duas vezes, preço normal de etiqueta mais juros de 10%
'''

produto = float(input('Digite o valor do produto: R$'))

print("1 - À vista em dinheiro ou cheque, recebe 10% de desconto")
print('2 - À vista no cartão de crédito, recebe 15% de desconto')
print('3 - Em duas vezes, preço normal de etiqueta sem juros')
print("4 - Em duas vezes, preço normal de etiqueta mais juros de 10%")

pag = int(input('Qual método de pagamento você vai usar? (1, 2, 3, 4): '))

if pag == 1:
    print(f'O valor final da compra será de R$ {produto * 0.9:.2f}')
elif pag == 2:
    print(f'O valor final da compra será de R$ {produto * 0.85:.2f}')
elif pag == 3:
    print(f'O valor final da compra será de duas parcelas de R$ {produto / 2:.2f}')
elif pag == 4:
    print(f'O valor final da compra será de duas parcelas, sendo uma R$ {produto / 2 :.2f} e a segunda de R$ {(produto / 2) * 1.1}')
else: 
    print('Dado inválido, tente novamente')