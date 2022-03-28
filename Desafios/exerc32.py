# Exercício Python 32: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

somaidade = 0
idade_maisvelho = 0
nome_maisvelho = ''
mulher_menor = 0

for i in range(1, 5):
    print(f'\033[1;32mDADOS {i}º PESSOA:\033[m')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo (M/F): ').lower()

    somaidade += idade
    media = somaidade/4

    if sexo == 'm' and idade > idade_maisvelho:
        idade_maisvelho = idade
        nome_maisvelho = nome
    
    if sexo == 'f' and idade < 20:
        mulher_menor += 1

print(f'\nA média das idades é: \033[1m{media}\033[m anos.')
print(f'O homem mais velho é \033[1m{nome_maisvelho}033\[m e tem \033[1m{idade_maisvelho}\033[m anos.')
print(f'\033[1m{mulher_menor}\033[m mulhe(res) possuem menos de 20 anos.')