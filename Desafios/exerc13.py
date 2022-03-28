# Exercício Python 13: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

dist = float(input('Insira a distância da viagem em km: '))

if dist <= 200.00:
    print(f'O preço da passagem será: R$ {dist * 0.50:.2f}')
else:
    print(f'O preço da passagem será: R$ {dist * 0.45:.2f}')