# Exercício Python 22: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status.

peso = float(input('Qual seu peso: '))
altura = float(input('Qual sua altura: '))
imc = peso/(altura**2)

print(f'Seu IMC: {imc:.2f}')

if imc < 18.5:
    print('Situação: ABAIXO DO PESO.')
elif 18.5 <= imc < 25:
    print('Situação: PESO IDEAL.')
elif 25 <= imc < 30:
    print('Situação: SOBREPESO.')
elif 30 <= imc < 40:
    print('Situação: OBESIDADE.')
else:
    print('Situação: OBESIDADE MORBIDA.')