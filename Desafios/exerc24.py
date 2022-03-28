# Exercício Python 24: Crie um programa que faça o computador jogar Jokenpô com você.

import random

game = ['PEDRA', 'PAPEL', 'TESOURA']

jogador = input('Qual a sua jogada (Pedra, papel ou tesoura)? ').upper()

jogador_pc = random.choice(game)

if (jogador == 'PEDRA' and jogador_pc == 'TESOURA') or (jogador == 'PAPEL' and jogador_pc == 'PEDRA') or (jogador == 'TESOURA' and jogador_pc == 'PAPEL'):
    print('\033[1;32mPARABÉNS!! Você ganhou!\033[m')

elif jogador == jogador_pc:
    print('\033[;35mEMPATE!!\033[m')

else:
    print('\033[1;31mPERDEU!! Tente outra vez\033[m')

print(f'\nGabarito do PC: {jogador_pc}\n')