# Exercício Python 23: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço formal 
# 3x ou mais no cartão: 20% de juros

valor_prod = float(input('Preço do produto (R$): '))
modo = input('Modo de pagamento, à vista ou a prazo? ')

if modo == 'a vista' or modo == 'vista' or modo == 'à vista':
    pagamento = input('Qual a condição de pagamento: Dinheiro/Cheque ou Cartão? ').lower()

    if pagamento == 'dinheiro' or pagamento == 'cheque':
        print(f'Valor a pagar com desconto de 10%: R$ {valor_prod*0.9:.2f}')
    elif pagamento == 'cartão' or pagamento == 'cartao':
        print(f'Valor a pagar com desconto de 5%: R$ {valor_prod*0.95:.2f}')

elif modo == 'a prazo' or modo == 'prazo':
    parcela = int(input('Em quantas parcelas: '))

    if parcela <= 2:
        print(f'Valor a pagar: R$ {valor_prod}')
        print(f'Valor da parcela: {parcela}x R${valor_prod/parcela:.2f}')        
    elif parcela >= 3:
        print(f'Valor a pagar com juros de 20%: {valor_prod*1.2:.2f}')
        print(f'Valor da parcela: {parcela}x R${(valor_prod*1.2)/parcela:.2f}') 