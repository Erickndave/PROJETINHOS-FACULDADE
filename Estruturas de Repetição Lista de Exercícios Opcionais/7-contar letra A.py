'''
Elaborar um programa que solicita várias palavras ao usuário, sendo que o critério de
parada é digitar uma palavra vazia. Contar e exibir quantas letras A existem neste
conjunto de palavras
'''
palavras = []
while True:
    palavra = input('Digite uma palavra: ')
    if palavra == '':
        break
    palavras.append(palavra)
letras_A = 0
for palavra in palavras:
   letras_A += palavra.lower().count('a')
print(f"Total de letras A: {letras_A}")