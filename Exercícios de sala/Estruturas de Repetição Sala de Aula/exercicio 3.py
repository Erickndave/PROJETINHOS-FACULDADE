'''
Criar um programa que recebe um texto digitado pelo usuário e
o imprime apenas com consoantes, removendo as vogais. Obs.:
desconsiderar letras maiúsculas e acentos.
'''
txt = input('Digite o texto: ')
texto_sem_vogais = ""
for i in txt:
    if i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u':
        texto_sem_vogais += i
print(f'O texto sem vogaias é {texto_sem_vogais}')
