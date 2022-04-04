#Exercício Python 33: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = input('Informe o sexo [M/F]: ').upper()[0] 

while sexo != 'M' and sexo != 'F':  
    print('Sexo incorreto!')
    sexo = input('Informe novamente o sexo [M/F]: ').upper()[0]
print('Concluído!')