"""
Formatando Valores com moficadores

:s - Texto (Strings)
:d - inteiros (Int)
:f - Numeros de ponto flutuante (Float)
:.(Número)f - Quantidade de casas decimais (Float)
:(Caractere) (> ou < ou ^) (QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""
num1 = 10
num2 = 3
divisao = num1/num2
print(f'O resultado da divisão é {divisao:.2f}')

# Usando Números
num3 = 1
print(f'Formatando numero em Float na chave: {num3:.2f}')
print(f'Colocando Zeros a esquerda em 10 casas: {num3:0>10}')
print(f'Colocando Zeros a Direita em 10 casas: {num3:0<10}')
print(f'Mantendo o {num3} no centro envolto de Zeros em 10 casas: {num3:0^10}')
print('\n')

# Usando String
nome = 'Leandro Auzier'
# Põe # em 50 espaços sendo eles subtraidos pelo tamanho do nome, ao redor do proprio nome
print(f'{nome:#^50}')
