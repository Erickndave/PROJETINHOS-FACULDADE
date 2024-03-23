'''
O IMC – Índice de Massa Corporal é um critério da Organização Mundial de Saúde para dar uma indicação sobre a condição de peso de uma pessoa adulta. 
A fórmula é IMC = peso / altura2 . Implemente um programa que leia o peso e a altura de um adulto e mostre sua condição de acordo com a tabela abaixo.
IMC em adultos Condição
• Abaixo de 18,5 – Abaixo do peso
• Entre 18,5 e 25 – Peso normal
• Entre 25 e 30 – Acima do peso
• Acima de 30 – Obeso
'''

peso = float(input('Digite o seu peso: '))
alt = float(input('Digite a sua altura: '))
imc = peso / (alt * alt)

if imc < 18.5:
    print(f'O seu imc é {imc:.2f} e você está abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print(f'O seu imc é {imc:.2f} e você está com o peso normal')
elif imc >= 25 and imc < 30:
    print(f'O seu imc é {imc:.2f} e você está acima do peso')
elif imc > 30:
    print(f'O seu imc é {imc:.2f} e você está obeso')
else:
    print('Algum dado está incorreto, por favor tente novamente')