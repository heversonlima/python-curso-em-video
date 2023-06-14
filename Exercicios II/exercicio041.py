

anoNascimento = int(input('Digite o ano do seu nascimento: '))

idade = 2023 - anoNascimento

if idade > 0 and idade <= 9:
    print(f'Com {idade} anos, voce entra na categoria Mirim.')
elif idade > 9 and idade <= 14:
    print(f'Com {idade} anos, voce entra na categoria Infantil.')
elif idade > 14 and idade <= 19:
    print(f'Com {idade} anos, voce entra na categoria Junior.')
elif idade == 20:
    print(f'Com {idade} anos, voce entra na categoria Senior.')
elif idade > 20:
    print(f'Com {idade} anos, voce entra na categoria Master.')
else:
    print('Erro. Tente novamente..')