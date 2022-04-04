# Exercício Python 37: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

import random

print('---------JOGO DO PAR OU ÍMPAR----------')
escolha = int(input('Escolha [0]par ou [1]ímpar? '))
jogador = int(input('Escolha um número (0 a 10): '))
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
escolha_pc = random.choice(lista) 
cont = 0

while True:
    if escolha == 0 and (jogador + escolha_pc) % 2 == 0:
        cont += 1
        print('Você GANHOU!!!')
        print(f'Você escolheu {jogador} e a máquina escolheu {escolha_pc}. Soma = {jogador + escolha_pc} -> PAR')
    elif escolha == 1 and (jogador + escolha_pc) % 2 != 0:
        cont += 1
        print('Você GANHOU!!!')
        print(f'Você escolheu {jogador} e a máquina escolheu {escolha_pc}. Soma = {jogador + escolha_pc} -> ÍMPAR')
    else:
        print('Você PERDEU!!!')
        if (jogador + escolha_pc) % 2 == 0:
            print(f'Você escolheu {jogador} e a máquina escolheu {escolha_pc}. Soma = {jogador + escolha_pc} -> PAR')
        else:
            print(f'Você escolheu {jogador} e a máquina escolheu {escolha_pc}. Soma = {jogador + escolha_pc} -> ÍMPAR')
        break
    escolha = int(input('Escolha [0]par ou [1]ímpar? '))
    jogador = int(input('Escolha um número (0 a 10): '))
    escolha_pc = random.choice(lista)