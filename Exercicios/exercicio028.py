import random
from time import sleep # sleep para esperar um pouco
ram = random.randint(1, 5)

print(ram)

numero = int(input('Tente advinhar o numero aleatorio entre 1 a 5: '))

print('PROCESSANDO...')
sleep(3)

if (ram == numero):

    print('Parabens, voce acertou o numero')
    print(f'numero gerado: {ram}\n Seu numero: {numero}')

else:
    print('Voce não acertou, tente novamente')
    print(f'Numero gerado: {ram}\nSeu numero: {numero}')

