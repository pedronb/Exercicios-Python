# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax² + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
#a - Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve pedir os demais valores, sendo encerrado;
#b - Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#c - Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#d - Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

a = int(input('Insira um valor: '))
b = int(input('Insira um valor: '))
c = int(input('Insira um valor: '))
delta = b**2 - (4 * a * c)
x1 = (-b + (delta)**(1/2)) / 2*a
x2 = (-b - (delta)**(1/2)) / 2*a

if a == 0:
  print('\nA equação não é do 2ºGrau.')

elif delta < 0:
  print('\nA equação não tem raízes reais.')

elif delta == 0:
  print(f'\nRaízes reais iguais.\nRAÍZES: {x1}')

elif delta > 0:
  print(f'\nA equação possui duas raízes reais.\nRAÍZES: {x1} e {x2}')