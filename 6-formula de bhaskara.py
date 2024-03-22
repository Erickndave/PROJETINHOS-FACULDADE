'''
Implemente um programa para calcular as raízes de uma equação do 2º grau, sendo que
os valores dos coeficientes A, B, e C devem ser fornecidos pelo usuário, e os valores das
raízes devem ser calculadas pela fórmula de Bhaskara, como segue:
'''
import math

a = float(input('Digite o núemro para a variável A: '))
b = float(input('Digite o núemro para a variável B: '))
c = float(input('Digite o núemro para a variável C: '))
delta = (b * b) / 4 * a * c
if delta < 0:
    print('Não possuí raizes reais')
elif delta == 0:
    x = -b / (2*a)
    print(f'Possí apenas uma raiz real que é {x:.2f}')
else:
    x1 = (-b) + (math.sqrt(delta)) / 2 * (a)
    x2 = (-b) - (math.sqrt(delta)) / 2 * (a)
    print(f'Possuí duas raizes reais que são {x1:.2f} e {x2:.2f} ')