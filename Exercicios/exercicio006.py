import math
menu = 'Dobro, Triplo e Raiz Quadrada'
print(f'{menu:=^20}')
numb = int(input('Informe um numero: '))


print(f'O dobro de {numb} é {numb + numb}\n{numb} ao quadrado é {numb*numb}\nA raiz quadrada de {numb} é {math.sqrt(numb)}')