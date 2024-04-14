'''
Elaborar um programa que receba o nome completo do usuário, e imprima apenas o
primeiro e último nome.
'''
name = input("Digite seu nome completo: ")
name_part = name.split()
firts_nome = name_part[0]
last_nome = name_part[-1]
print("Primeiro nome:", firts_nome)
print("Último nome:", last_nome)
