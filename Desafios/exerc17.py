# Exercício Python 17: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#O primeiro valor é maior
#O segundo valor é maior
#Não existe valor maior, os dois são iguais

n1 = int(input('Insira um número inteiro: '))
n2 = int(input('Insira outro número inteiro: '))
maior = 0
menor = 0

if n1 > n2:
    maior = n1
    menor = n2
    print(f'O valor {maior} é maior.')
elif n1 < n2:
    maior = n2
    menor = n1
    print(f'O valor {maior} é o maior.')
elif n1 == n2:
    print('Não existe valor maior, os dois são iguais.')