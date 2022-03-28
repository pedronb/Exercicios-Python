# Faça um programa que leia 5 números e informe o maior número.

numeros = []

for i in range(1, 6):
  x = int(input('Digite um número: '))
  numeros.append(x)

print(max(numeros))