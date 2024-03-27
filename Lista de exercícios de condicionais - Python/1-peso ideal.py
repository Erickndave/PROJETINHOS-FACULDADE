"""
. Tendo como dados de entrada a altura e o sexo de uma pessoa, implemente um
programa que calcule seu peso ideal, utilizando as seguintes fórmulas:
• para homens: (72.7 * h) - 58;
• para mulheres: (62.1 * h) - 44.7.
"""

alt = float(input('Digite aqui a sua altura (EM METROS): '))
sex = input('Digite aqui o seu sexo (M/F):  ').upper()

if sex == 'M':
    ideal = (72.7 * alt) - 58
    print(f'seu peso ideal é {ideal}:')
elif sex == 'F':
   ideal =  (62.1 * alt) - 44.7
   print(f'seu peso ideal é {ideal}:')
else:
    print("Algum comando está errado, por favor tente novamente")    