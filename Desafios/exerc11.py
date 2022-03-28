# Exercício Python 11: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

vel = float(input('Insira a velocidade em km/h: '))
limite = 80.0

if vel > limite:
    print(f'Você foi MULTADO! valor da multa: R$ {(vel - limite) * 7.0:.2f}')