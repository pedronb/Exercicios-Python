# Exercício Python 19: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#Média abaixo de 5.0: REPROVADO
#Média entre 5.0 e 6.9: RECUPERAÇÃO
#Média 7.0 ou superior: APROVADO

n1 = float(input('Insira sua nota 1: '))
n2 = float(input('Insira sua nota 2: '))
media = (n1+n2)/2

print(f'\nMédia do Aluno: {media}')
if media < 5.0:
    print('\033[1;31mREPROVADO\033[m\n')
elif media >= 5.0 or media <= 6.9:
    print('\033[1;34mRECUPERAÇÃO\033[m\n')
elif media >= 7.0:
    print('\033[1;32APROVADO\033[m\n')