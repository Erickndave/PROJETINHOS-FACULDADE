'''
Criar um programa que gera a série de Fibonacci até enquanto o
valor for menor que um valor informado pelo usuário. Obs.: Série de
Fibonacci = 0, 1, 1, 2, 3, 5, 8 ,13, 21, 34, 55,... é formada por 0, 1 e
partir deste ponto sempre será a soma dos dois valores anteriores.
'''
'''
limite = int(input('Digite o valor limite para o número de Febonacci: '))
a, b = 0, 1
while True:
   print(a, end=", ")
   a,b = b, a + b
   if a > limite:
     break
'''

limite = int(input('Digite o valor limite para o número de Febonacci: '))
n1 = 0
n2 = 1
fib = ""
if limite == 1:
    fib = f"{n1}"
elif limite == 2:
    fib = f'{n1} {n2}'
else:
    fib = f'{n1} {n2}'
    for i in range(limite, 2):
        n = n1 + n2
        fib += f'{n}'
        n1 = n2
        n2 = n
print(f'{fib}')