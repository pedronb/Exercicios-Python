# Exercício Python 28: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0

for i in range(0,6):
    num = int(input('Insira um número inteiro: '))

    if num % 2 == 0:
        soma += num

print(soma)