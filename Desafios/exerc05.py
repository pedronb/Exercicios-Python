#Exercício Python 05: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

x = float(input('Insira um ângulo qualquer: '))

print(f'O cosseno de {x}º é {math.cos(x):.3f}, o seno é {math.sin(x):.3f} e a tangente é {math.tan(x):.3f}.')