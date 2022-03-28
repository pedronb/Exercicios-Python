# Exercício Python 25: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, 
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.
# Estrutura de Repetição.

import time # comando para o terminal esperar algum tempo antes do próximo print.

for cont in range(10, -1, -1):
    print(cont)
    time.sleep(1) # comando para o terminal esperar algum tempo antes do próximo print.
print('BOOM!  BOOM!  ACABOU!')