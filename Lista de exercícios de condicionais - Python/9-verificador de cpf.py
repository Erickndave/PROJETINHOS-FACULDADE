#Implementar um programa que valide um CPF. Para tanto, solicitar em separado cadacum dos 11 dígitos do CPF
#Pedindo os digitos do CPF para o úsuario
d1 = int(input('Digite o primeiro digito: '))
d2 = int(input('Digite o segundo digito: '))
d3 = int(input('Digite o terceiro digito: '))
d4 = int(input('Digite o quarto digito: '))
d5 = int(input('Digite o quinto digito: '))
d6 = int(input('Digite o sexto digito: '))
d7 = int(input('Digite o sétimo digito: '))
d8 = int(input('Digite o oitavo digito: '))
d9 = int(input('Digite o nono digito: '))
#Cálculo 1
calculo1 = (d1  * 10) + (d2 * 9) + (d3 * 8) + (d4 * 7) + (d5 * 6) + (d6 * 5) + (d7 * 4) + (d8 * 3) + (d9 * 2)
mult1 = calculo1 * 10
#Resto para ter o primeiro dígito
verificador1 = mult1 % 11
if verificador1 == 10:
    verificador1 = 0
#validação do segundo dígito
calculo2 = (d1  * 11) + (d2 * 10) + (d3 * 9) + (d4 * 8) + (d5 * 7) + (d6 * 6) + (d7 * 5) + (d8 * 4) + (d9 * 3) + (verificador1 * 2)
mult2 = calculo2 * 10
verificador2 = mult2 % 11
print(f'O seu cpf é {d1}{d2}{d3}{d4}{d5}{d6}{d7}{d8}{d9}-{verificador1}{verificador2}')
