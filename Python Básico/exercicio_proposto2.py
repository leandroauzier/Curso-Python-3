"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada.
Ex: Bom dia 0-11, Boa tarde 12-17 e Boa Noite 18-23.
"""
horario = input('olá, Que horas são agora?: ')
if horario.isdigit():
    if int(horario) >= 0 and int(horario) <= 11:
        print('Bom dia')
    elif int(horario) >= 12 and int(horario) <= 17:
        print('Boa tarde')
    elif int(horario) >= 18 and int(horario) <= 23:
        print('Boa noite')
    else:
        print('Engraçado mas digite apenas horas entre 0 - 23 hrs')
else:
    print('Por favor digite Somente a hora sem Minutos!')