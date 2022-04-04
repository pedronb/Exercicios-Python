# Exercício Python 36: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

n = int(input('Digite um número inteiro [digite "0" para sair]: '))
cont = 0
lista = [n]

while n != 0:
    cont += 1
    n = int(input('Digite um número inteiro [digite "0" para sair]: '))
    lista.append(n)
    if n == 0:
        del(lista[-1])

print(f'O maior valor: {max(lista)}')
print(f'O menor valor: {min(lista)}')
print(f'Média: {sum(lista)/cont}')