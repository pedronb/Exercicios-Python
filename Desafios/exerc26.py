# Exercício Python 26: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0

for i in range(1, 501):
    if i % 2 != 0 and i % 3 == 0:
        soma += i

print(soma)