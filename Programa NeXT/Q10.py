# Crie um programa que tenha uma função que receba uma lista de números inteiros e exiba todos os valores multiplicados por um valor inserido pelo usuário.

def multip_lista(lista, multip):
  for i in lista:
    print(i*multip)

lista = []

num = input('Informe os valores da lista, separados por vírgula: ').split(',')

for n in num:
  lista.append(int(n))

multip = int(input('Informe o multiplicador: '))

multip_lista(lista, multip)