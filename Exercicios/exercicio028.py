import random

ram = random.randint(1, 5)

print(ram)

numero = int(input('Tente advinhar o numero aleatorio entre 1 a 5: '))

if (ram == numero):

    print('Parabens, voce acertou o numero')
    print(f'numero gerado: {ram}\n Seu numero: {numero}')

else:
    print('Voce não acertou, tente novamente')
    print(f'Numero gerado: {ram}\nSeu numero: {numero}')

