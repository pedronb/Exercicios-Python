# Exercício Python 31: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

import datetime

date = datetime.date.today()
year = int(date.strftime('%Y'))

ano_nasc = []
idades = []
maiores = 0
menores = 0

for i in range(7):
    ano_nasc.append(int(f'{(input("Digite o ano de nascimento: "))}'))

for i in ano_nasc:
    idades.append(year - i)

for i in idades:
    if i >= 18:
        maiores += 1
    else:
        menores += 1

print(f'{maiores} pessoas é(são) maior(es) de idade e {menores} é(são) meno(res) de idade.')