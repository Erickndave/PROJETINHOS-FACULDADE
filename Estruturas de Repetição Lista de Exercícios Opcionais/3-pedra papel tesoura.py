'''
Criar um jogo de pedra, papel, tesoura entre dois jogadores. Antes de começar o jogo,
porém, deve ser escolhido a quantidade de pontos a serem feitos para vencer.
'''
rodadas = int(input('Digite a quantidade de pontos necessários para vencer a partida: '))
player1 = 0
player2 = 0
while True:
    if player1 == rodadas:
            print('Parabéns, o JOGADOR 1 venceu!')
            break
    elif player2 == rodadas:
            print('Parabéns, o JOGADOR 2 venceu!')
            break
    jogada_p1 = input("JOGADOR 1 Digite a sua jogada (pedra, papel, tesoura): ").lower().strip()
    jogada_p2 = input("JOGADOR 2 Digite a sua jogada (pedra, papel, tesoura): ").lower().strip()
    if jogada_p1 == jogada_p2:
        print('EMPATE')
        continue
    else:   
        if jogada_p1 == 'papel' and jogada_p2 == 'pedra':
            print('O Jogador 1 pontuou')
            player1 += 1
        elif jogada_p1 == 'tesoura' and jogada_p2 == 'papel':
            print('O Jogador 1 pontuou')
            player1 += 1
        elif jogada_p1 == 'pedra' and jogada_p2 == 'tesoura':
            print('O Jogador 1 pontuou')
            player1 += 1
        elif jogada_p2 == 'papel' and jogada_p1 == 'pedra':
            print('O Jogador 2 pontuou')
            player2 += 1
        elif jogada_p2 == 'tesoura' and jogada_p1 == 'papel':
            print('O Jogador 2 pontuou')
            player2 += 1
        elif jogada_p2 == 'pedra' and jogada_p1 == 'tesoura':
            print('O Jogador 2 pontuou')
            player2 += 1
        else:
             print("Erro gramatical, por favor tente novamente")