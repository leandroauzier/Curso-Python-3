"""
Faça um programa que peça para o usuário para digitar um número inteiro, informe se este numero é par ou impar.
Caso o usuário não digite um número inteiro, informe ao usuário.
"""
num = input('Informe um número: ')
if num.isdigit():
    if int(num) % 2 == 0:
        print('Seu número é Par')
    else:
        print('Seu número é impar')
else:
    print('Desculpe, só aceito números!')
