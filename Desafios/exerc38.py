# Exercício Python 38: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.

print('CADASTRE UM USUÁRIO:')
idade = int(input('Insira a idade: '))
sexo = input('Insira o sexo [Homem/Mulher]: ').lower()
cont_idade = homem = mulher_20 = 0

while True:
    if idade > 18:
        cont_idade += 1
    if sexo == 'homem':
        homem += 1
    if idade < 20 and sexo == 'mulher':
        mulher_20 += 1
    n = int(input('Digite [1] para Cadastrar mais pessoas e [0] para Sair: '))
    if n == 1:
        idade = int(input('Insira a idade: '))
        sexo = input('Insira o sexo [Homem/Mulher]: ').lower()
    elif n == 0:
        print('\nSISTEMA FINALIZADO.')
        break

print(f'a- Pessoas maiores de 18 anos: {cont_idade}')
print(f'b- Homens cadastrados: {homem}')
print(f'c- Mulheres com menos de 20 anos: {mulher_20}')