#Crie um programa para um circo, no qual dada a idade de uma pessoa, seja indicado o valor do ingresso segundo as regras:
#a) A entrada para qualquer pessoa com menos de 4 anos ou maior que 60 é gratuita;
#b) a entrada para qualquer pessoa com idade entre 4 e 18 custa 20 reais;
#c) a entrada para qualquer pessoa com 18 ou mais custa 30 reais;
#d) estudantes e professores pagam meia-entrada.

idade = int(input('Digite a idade da pessoa: '))

ocup = input('Meia entrada: Estudante ou Professor?\n(s) Sim\t(n) Não\n').lower()

if idade < 4 or idade > 60:
  print('Valor da entrada: GRATUITO!')

elif 4 <= idade < 18:
  if ocup == 's' or ocup == 'sim':
    print('Valor da entrada: R$ 10,00')
  else:
    print('Valor da entrada: R$ 20,00')

elif idade >= 18:
  if ocup == 's' or ocup == 'sim':
    print('Valor da entrada: R$ 15,00')
  else:
    print('Valor da entrada: R$ 30,00')