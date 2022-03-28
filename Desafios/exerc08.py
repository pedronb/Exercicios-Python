# Exercício Python 08: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).upper().strip()

print(f'A letra "A" apareceu {frase.count("A")} vezes.')
print(f'O primeiro "A" apareceu na posição {frase.find("A")+1}.')
print(f'O último "A" apareceu na posição {frase.rfind("A")}.') 