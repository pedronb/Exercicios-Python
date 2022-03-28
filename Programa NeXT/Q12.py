# Crie um programa que receba do usuário 5 números inteiros e os exiba na tela na ordem contrária a que foi inserido. A leitura dos números deve ser feita em uma função e a exibição dos valores em ordem contrária deve ocorrer em outra função.

def inteiro(n):
  l = []
  for i in n:
    l.append(int(i))
  print(l)

def inteiro_inverso(n):
  l = []
  for i in n:
    l.append(int(i))
  print(l[::-1])

num = input('Insira 5 números inteiros, separados por vírgula: ').split(',')
inteiros = []

inteiro(num)
inteiro_inverso(num)