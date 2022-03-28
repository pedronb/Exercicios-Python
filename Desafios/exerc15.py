# Exercício Python 15: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

print('\033[1;32m*'*35)
print('\033[1;97mSIMULADOR DE EMPRÉSTIMO RESIDENCIAL\033[m')
print('\033[1;32m*\033[m'*35)

valor_casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário? '))
pagar_anos = int(input('Quantos anos para pagar? '))
prest_mensal = (valor_casa) / (pagar_anos * 12)
print(f'\nPrestação mensal = R$ {prest_mensal:.2f}')

if prest_mensal > 0.30 * salario:
    print('\033[1;33mEMPÉSTIMO NEGADO!\033[m')
else:
    print('\033[1;32mEMPRÉSTIMO APROVADO!\033[m\n')