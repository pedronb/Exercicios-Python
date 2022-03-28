# Tendo como dado de entrada a altura ( h ) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens:  (72.7×h)−58 
# Para mulheres:  (62.1×h)−44.7

print('Qual seu gênero: \n\n(m) Masculino \t(f) Feminino\n')
g = input()
h = float(input('Insira sua altura: '))

if g == 'm':  
  print(f'Seu peso ideal é: {(72.7 * h) - 58:.2f}')
elif g == 'f':
  print(f'Seu peso ideal é: {(62.1 * h) - 44.7:.2f}')
else:
  print('Gênero inválido!')