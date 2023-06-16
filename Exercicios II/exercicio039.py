from datetime import date

try:
    anoNasc = int(input('Digite o ano de nascimento: '))
    genero  = int(input('Informe seu genero: \n1 - Masculinon\n2 - Femenino : '))
    anoAtual = date.today().year
    idade = anoAtual - anoNasc
    anoAlistamento = anoAtual - (idade - 18)
    anoAlistamentoFuturo = anoAtual + (idade - 18)

    if genero == 1:
        if idade > 18 and idade <= 45:
            print(f'Você passou {idade - 18} ano(s) do periodo ideal para o alistamento. Aliste-se já')
            print(f'Voce deveria ter se alistar em {anoAtual - (idade - 18)}') 
        elif idade < 18:
            print(f'Voce ainda não pode se alistar, pois ainda é menor de idade')
            print(f'Faltam {18-idade} ano(s) para o seu periodo de alistamento')
            print(f'Voce podera se alisatar em: {anoAtual + (18 - idade)}')
        elif idade > 45:
            print(f'Com {idade} anos, voce não pode mais se alistar')
        else:
            print(f'Se você tem {idade} anos, você está no periodo ideal par ao alistamento militar')
    else:
        print('Se voce é do genero femenino, não precisa fazer o alistamento militar')
except:
    print('Digite um valor inteiro para informar sua idade ou genero\n')