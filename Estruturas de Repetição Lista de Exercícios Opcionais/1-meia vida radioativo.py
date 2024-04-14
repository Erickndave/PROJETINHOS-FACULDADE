'''
Um determinado material radioativo perde metade de sua massa a cada 50 segundos.
Dada a massa inicial, em gramas, fazer um algoritmo que determine o tempo necessário
para que a massa se torne menor do que 0,5 grama. Imprima como dado de saída a massa
final e o tempo calculado em segundos
'''
tempo = 0
massa = float(input('Digite a massa do material (em grama): '))
while True:
    if massa >= 0.5:
        massa /= 2
        tempo += 50
    elif massa < 0.5:
        print(f'Ao final, a massa é {massa:.2f}g e o tempo foi de {tempo} segundos.')
        break

