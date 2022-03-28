# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido.

s = float(input('Quanto você ganha por hora de trabalho? '))
h = int(input('Quantas horas de trabalho no mês? '))
salario_bruto = s * h
IR = 0.11*salario_bruto
INSS = 0.08*salario_bruto
sindicato = 0.05*salario_bruto
salario_liquido = salario_bruto - IR - INSS - sindicato

print(f'\nSalário Bruto: R$ {salario_bruto:.2f}')
print(f'Desconto INSS: R$ {INSS:.2f}')
print(f'Desconto Sindicato: R$ {sindicato:.2f}')
print(f'Salário Líquido: R$ {salario_liquido:.2f}')