try:
    idade = int(input('Digite sua idade: '))

    if idade > 18 and idade <= 45:
        print(f'Você passou {idade-18} ano(s) do periodo ideal para o alistamento. Aliste-se já') 
    elif idade > 45:
        print(f'Com {idade} anos, voce não pode mais se alistar')
    elif idade < 18:
        print(f'Voce ainda não pode se alistar, pois ainda é menor de idade')
        print(f'Faltam {18-idade} ano(s) para o seu periodo de alistamento')
    else:
        print(f'Se você tem {idade} anos, você está no periodo ideal par ao alistamento militar')
except:
    print('Digite um valor inteiro para informar sua idade\n')