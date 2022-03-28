# Implemente um programa que possa receber do usuário a temperatura em graus Celsius ou Fahrenheit. Antes de receber a temperatura, pergunte ao usuário se ele deseja inserir em Celsius ou em Fahrenheit. Se a entrada for em graus Celsius, o programa deverá retornar a temperatura em Fahrenheit. Se a entrada for em Fahrenheit, o programa deverá retornar a temperatura em Celsius.

def conversao_temp(grau, temp):
  if grau == 'Celsius' or grau == 'celsius':
    n = (temp*1.8) + 32
    print(f'Temperatura convertida: {n}ºF')
  
  elif grau == 'Fahrenheit' or grau == 'fahrenheit':
    n = (temp-23)/1.8
    print(f'Temperatura convertida: {n}ºC')


grau = input('Deseja inserir em Celsius ou Fahrenheit? ')
temp = float(input('Insira a temperatura: '))

conversao_temp(grau, temp)