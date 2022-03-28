# Exercício Python 29: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

a1 = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digite a razão dessa P.A: '))
a11 = a1 + (11-1)*r

for i in range(a1, a11, r):
    print(i)