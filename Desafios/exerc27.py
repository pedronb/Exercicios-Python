# Exercício Python 27: Mostre a tabuada de um número que o usuário escolher, utilizando um laço de repetição.

n = int(input('Insira um número inteiro: '))

for i in range(0, 11):
    print(f'{n} x {i} = {n*i}')