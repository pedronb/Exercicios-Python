# Exercício Python 18: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

import datetime
date = datetime.date.today()
# print(date.year)
year = int(date.strftime('%Y'))
# forma de importar o ano atual em python

ano_nasc = int(input('Insira o ano de nascimento: '))
idade = year - ano_nasc

if idade < 18:
    print(f'Você tem {idade} anos. Ainda vai se alistar.')
    print(f'Faltam {18 - idade} anos para o alistamento.')
elif idade == 18:
    print(f'Você tem {idade} anos. É hora de se alistar.')
elif idade > 18:
    print(f'Você tem {idade} anos . Já passou do tempo de se alistar.')
    print(f'Passaram-se {idade - 18} anos do alistamento.')