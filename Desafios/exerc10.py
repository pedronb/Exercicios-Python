# Exercício Python 10: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
# Condições.

import random

n = [0, 1, 2, 3, 4, 5]
escolha = random.choice(n)

num = int(input('Advinhe o número escolhido de 0 a 5: '))

if num == escolha:
    print('ACERTOU!!')
else:
    print('ERROU!!')