# sorteador de numeros para alunos

import random

nome1 = input('Digite um nome: ')
nome2 = input('Digite um nome: ')
nome3 = input('Digite um nome: ')
nome4 = input('Digite um nome: ')

lista = [nome1, nome2, nome3, nome4]

# usando a função choice para sortear um nome
sorteador = random.choice(lista)

print(f'O escolhido foi {sorteador}')