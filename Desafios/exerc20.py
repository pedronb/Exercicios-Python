# Exercício Python 20: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade.

import datetime

date = datetime.date.today()
year = int(date.strftime('%Y'))

ano_nasc = int(input('Insira o ano de nascimento do atleta: '))
idade = year - ano_nasc

if idade <= 9:
    print('Categoria do Atleta: MIRIM.')
elif 9 < idade <= 14:
    print('Categoria do Atleta: INFANTIL.')
elif 14 < idade <= 19:
    print('Categoria do Atleta: JUNIOR.')
elif 19 < idade <= 20:
    print('Categoria do Atleta: SENIOR.')
else:
    print('Categoria do Atleta: MASTER.')