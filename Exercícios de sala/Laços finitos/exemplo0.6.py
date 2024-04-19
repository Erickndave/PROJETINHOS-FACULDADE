'''
Solicitar um número de 1 a 5 e dizer se este número é par ou ímpar
'''
while True:
    try:
        num = int(input('Digite um número de 1 a 5: '))
        if num >= 1 and num <= 5:  
            break
    except:
        print('Entrada inválida')
if num % 2 == 0:
    print('O número digitado é par')
else:
    print('O número digitado é ímpar')