# Exercício Python 14: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

import math

r1 = int(input('Digite o comprimento da reta 1: '))
r2 = int(input('Digite o comprimento da reta 2: '))
r3 = int(input('Digite o comprimento da reta 3: '))

if math.fabs(r2 - r3) < r1 < math.fabs(r2 + r3) and math.fabs(r1 - r3) < r2 < math.fabs(r1 + r3) and math.fabs(r1 - r2) < r3 < math.fabs(r1 + r2):
    print(f'Um triângulo pode ser formado com os valores {r1}, {r2} e {r3}.')
else:
    print(f'Não podemos formar um triângulo com esses valores.')