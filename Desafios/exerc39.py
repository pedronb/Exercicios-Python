# Exercício Python 39: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.

print('~'*30)
print('LISTA DE COMPRAS')
print('~'*30)

prod = input('Insira o nome do produto: ')
preco = float(input('Insira o preço: '))
mais_mil = soma = 0
mais_barato = preco
prod_mais_barato = prod

while True:
    soma += preco
    if preco > 1000:
        mais_mil += 1
    if preco < mais_barato:
        mais_barato = preco
        prod_mais_barato = prod
    x = input('Continuar cadastrando [S/N]: ').upper()
    if x == 'S':
        prod = input('Insira o nome do produto: ')