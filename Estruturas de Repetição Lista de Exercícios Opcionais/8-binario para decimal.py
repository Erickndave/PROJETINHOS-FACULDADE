'''
Elaborar um programa que receba um número em binário, e mostre o seu valor em
decimal.
'''
numB = input('Digite um número binário: ')
base = 2
numLoop = len(numB)
#SOMA(Símbolo x Base^Posição)
for posição in range(numLoop, 0, -1):
    