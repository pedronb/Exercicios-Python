# Faça um programa que crie uma pasta no diretorio atual do notebook e crie dentro dele um arquivo chamado, lista_de_chamada.txt, na qual devera ter 5 nomes informados pelo usuario.

import os

os.mkdir('Listas') 

# os.mkdir() vai criar um novo diretorio(pasta), para remover a pasta utilizamos o comando os.rmdir()
# obs: para remover uma pasta é necessário remover tbm todos os arquivos que há dentro dele.

with open('Listas/lista_de_chamada.txt', 'w') as lista:
  for i in range(5):
    lista.write(f'{input("Nome do aluno: ")}\n')