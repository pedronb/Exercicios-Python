# Ler nome, sexo e idade. Se sexo for feminino e idade menor que 25, imprime o nome da pessoa e a palavra “ACEITA”, caso contrario imprimir “NÃO ACEITA”.

nome = input('Digite seu nome: ')
sexo = input('Insira o sexo (Masculino ou Feminino): ')
idade = int(input('Insira sua idade: '))

if (sexo == 'Feminino' or sexo == 'feminino') and idade < 25:
  print(f'{nome}, ACEITA.')
else:
  print('NÃO ACEITA.') 