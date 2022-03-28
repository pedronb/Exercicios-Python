# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#a. par ou ímpar;
#b. positivo ou negativo;
#c. inteiro ou decimal.

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
opera = input('Qual operação deseja realizar? ').lower()

if opera == 'soma' or opera == 'somar':
  resul = n1 + n2
  print(f'\nResultado: {resul}')
  if resul % 2 == 0:
    print('O número é PAR.')
  else:
    print('O número é ÍMPAR.')
  
  if resul > 0:
    print('O número é POSITIVO.')
  else:
    print('O número é NEGATIVO.')
  
  if resul // 1 == resul:
    print('O número é INTEIRO.')
  else:
    print('O número é DECIMAL.')

elif opera == 'subtração' or opera == 'subtrair':
  resul = n1 - n2
  print(f'\nResultado: {resul}')
  if resul % 2 == 0:
    print('O número é PAR.')
  else:
    print('O número é ÍMPAR.')
  
  if resul > 0:
    print('O número é POSITIVO.')
  else:
    print('O número é NEGATIVO.')
  
  if resul // 1 == resul:
    print('O número é INTEIRO.')
  else:
    print('O número é DECIMAL.')

elif opera == 'multiplicação' or opera == 'multiplicar':
  resul = n1 * n2
  print(f'\nResultado: {resul}')
  if resul % 2 == 0:
    print('O número é PAR.')
  else:
    print('O número é ÍMPAR.')
  
  if resul > 0:
    print('O número é POSITIVO.')
  else:
    print('O número é NEGATIVO.')
  
  if resul // 1 == resul:
    print('O número é INTEIRO.')
  else:
    print('O número é DECIMAL.')

elif opera == 'divisão' or opera == 'dividir':
  resul = n1 / n2
  print(f'\nResultado: {resul}')
  if resul % 2 == 0:
    print('O número é PAR.')
  else:
    print('O número é ÍMPAR.')
  
  if resul > 0:
    print('O número é POSITIVO.')
  else:
    print('O número é NEGATIVO.')
  
  if resul // 1 == resul:
    print('O número é INTEIRO.')
  else:
    print('O número é DECIMAL.')