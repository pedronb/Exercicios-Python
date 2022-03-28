# Crie um programa que registra as notas de uma pessoa na escola (como o boletim) em um arquivo. Em seguida, leia todos os valores para imprimir o menor valor, o maior e a média.

with open('notas.txt', 'w') as notas:
  for i in range(4):
    notas.write(f'{input("Digite sua nota: ")}\n')

with open('notas.txt') as notas:
  lista_notas = []
  for i in notas:
    lista_notas.append(float(i))
  media = sum(lista_notas)/4
  
  print(f'A menor nota: {min(lista_notas)}')
  print(f'A maior nota: {max(lista_notas)}')
  print(f'Média: {media:.2f}')