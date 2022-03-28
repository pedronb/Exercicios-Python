# Exercício Python 30: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. 

frase = input('Digite uma frase: ')
frase1 = frase.replace(' ', '')

frase_inver = frase1[::-1]

if frase1 == frase_inver:
    print('A frase é um palíndromo.')
else:
    print('A frase não é um palíndromo.')