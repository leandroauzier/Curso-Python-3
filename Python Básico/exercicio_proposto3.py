"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto";
se tiver entre 5 e 6 letras, escreva "Seu nome é normal; Maior que 6 escreva "Seu nome é muito grande".
"""
nome = input('Olá, digite seu primeiro nome: ')
if nome.isalpha():
    if len(nome) <= 4:
        print(f'Seu nome é pequeno, possui apenas {len(nome)} letras')
    elif len(nome) >=5 and len(nome) <= 6:
        print(f'Seu nome é de tamanho normal, pois possui {len(nome)} letras')
    elif len(nome) > 6:
        print(f'Seu nome é de tamanho grande, pois possui {len(nome)} letras')
else:
    print('Por favor apenas letras, afinal é seu nome!')