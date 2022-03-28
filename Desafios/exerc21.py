# Exercício Python 21: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado.

import math

r1 = int(input('Digite o comprimento da reta 1: '))
r2 = int(input('Digite o comprimento da reta 2: '))
r3 = int(input('Digite o comprimento da reta 3: '))

if math.fabs(r2 - r3) < r1 < math.fabs(r2 + r3) and math.fabs(r1 - r3) < r2 < math.fabs(r1 + r3) and math.fabs(r1 - r2) < r3 < math.fabs(r1 + r2):
    print(f'Um triângulo pode ser formado com os valores {r1}, {r2} e {r3}.')
    if r1 == r2 == r3:
        print('Triângulo formado: Equilátero.')
    elif (r1 == r2) or (r1 == r3) or (r3 == r2):
        print('Triângulo formado: Isóceles.')
    else:
        print('Triângulo formado: Escaleno.')
else:
    print(f'Não podemos formar um triângulo com esses valores.')