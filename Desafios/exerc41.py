import os
from time import sleep

nomes = list()
idades = list()

if not os.path.exists('cadastrados.txt'):
    with open('cadastrados.txt', 'w') as arquivo:       
        arquivo.write(f'{"-"*40}\n')
        arquivo.write(f'{"PESSOAS CADASTRADAS".center(40)}\n')
        arquivo.write(f'{"NOME": <20}\t{"IDADE": >10}\n')
        arquivo.write(f'{"-"*40}\n')
else:
    while True:
        try:     
            print('-'*40)
            print(f'{"MENU PRINCIPAL".center(40)}')
            print('-'*40)
            print('1 - Ver pessoas cadastradas\n2 - Cadastrar nova pessoa\n3 - Sair do sistema')
            print('-'*40)

            n = int(input('Qual sua opção: '))

            if n == 2:
                print('-'*40)
                print(f'{"OPÇÃO 2".center(40)}')
                print('-'*40)
                with open('cadastrados.txt', 'a') as arquivo:
                    nomes.append(input('Nome: '))
                    idades.append(int(input('Idade: ')))
                    arquivo.write(f'{nomes[-1]: <20}\t{idades[-1]: >10}\n')
                sleep(1)
                print('Cadastrado com sucesso!')
                sleep(2)
                continue
            
            elif n == 1:
                print('-'*40)
                print(f'{"OPÇÃO 1".center(40)}')
                print('-'*40)
                with open('cadastrados.txt') as arquivo:
                    for linha in arquivo:
                        print(linha)
                break
            elif n == 3:
                print('Sistema finalizado! Até logo!')
                break
            else:
                print('Digite uma opção válida!')
                sleep(2)
                continue
            
        except (ValueError, TypeError):
            print('ERRO: por favor, insira uma opção!')
            sleep(2)
            continue