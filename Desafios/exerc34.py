# Exercício Python 34: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
operacao = int(input('Informe a operação que deseja de acordo com o menu mostrado abaixo:\n[1] Somar\t[4] Novos números\n[2] Multiplicar\t[5] Sair do programa\n[3] Maior\n '))

while operacao == 4:
    n1 = float(input('Digite um número: '))
    n2 = float(input('Digite outro número: '))
    operacao = int(input('Informe a operação que deseja de acordo com o menu mostrado abaixo:\n[1] Somar\t[4] Novos números\n[2] Multiplicar\t[5] Sair do programa\n[3] Maior\n '))

if operacao == 1:
        print(f'A soma de {n1} e {n2} é igual a: {n1 + n2}')
elif operacao == 2:
        print(f'A multiplicação de {n1} e {n2} é igual a: {n1 * n2}')
elif operacao == 3:
    if n1 > n2:
            print(f'O maior número é: {n1}')
    else:
            print(f'O maior número é: {n2}')
elif operacao == 5:
    print('Programa encerrado!')