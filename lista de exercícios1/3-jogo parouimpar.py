'''
 Criar um jogo de par ou ímpar, onde dois jogadores entram com seu palpite (par ou
ímpar) e seus valores de 1 a 5. Tomar por base os nomes: Jogador 1 e Jogador 2. Caso
um dos valores esteja fora dos parâmetros informados, mostrar uma mensagem
informando que esta rodada não valeu. Caso contrário, informa qual jogador ganhou esta
rodada.
'''
valores = [1, 2, 3, 4, 5]
num1 = int(input('Jogador 1 digite um número de 1 a 5: '))
palpite_1 = str(input('Jogador 1 digite seu palpite (par/ímpar)'))
num2 = int(input('Jogador 2 digite um número de 1 a 5: '))
palpite_2 = str(input('Jogador 2 digite seu palpite (par/ímpar)'))


if num1 not in valores or num2 not in valores:
    print(f'Algum dado está inválido, tente novamente')

soma = num1 + num2    
pontuação = 'par' if soma % 2 == 0 else 'ímpar'

if pontuação == palpite_1 and pontuação == palpite_2:
    print(f'A soma dos números foi {soma}')
    print(f'Empate!')
elif pontuação == palpite_1:
    print(f'A soma dos números foi {soma}')
    print(f'O Jogador 1 venceu!!!!!!')
elif pontuação == palpite_2:
    print(f'A soma dos números foi {soma}')
    print(f'O Jogador 2 venceu!!!!!!')
