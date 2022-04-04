# Exercício Python 40: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

n = int(input('Insira o valor a ser sacado: '))
a = b = c = d = e = 0

if n % 50 == 0:
    print(f'{n // 50} cédulas de R$50.')
elif n % 50 != 0:
    a = n // 50
    b = n % 50
    if b % 20 == 0:
        print(f'{a} cédulas de R$50 e {b // n} cédulas de R$20.')
    elif b % 20 != 0:
        c = b // 20
        d = b % 20
        if d % 10 == 0:
            print(f'{a} cédulas de R$50, {c} cédulas de R$20 e {d // 10} cédulas de R$10.')
        elif d % 10 != 0:
            e = d % 10
            f = d // 10
            print(f'{a} cédulas de R$50, {c} cédulas de R$20, {f} cédulas de R$10 e {e // 1} cédulas de R$1.')