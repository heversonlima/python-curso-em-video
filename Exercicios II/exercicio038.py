try:
    n1 = float(input('Digite um valor: '))
    n2 = float(input('Digite outro valor: '))

    if n1 > n2:
        print(f'Opa {n1} é maior que {n2}')
    elif n2 > n1:
        print(f'Opa {n2} é maior que {n1}')
    elif n1 == n2:
        print(f'Opa parece que os numeros são iguais e equivalentes')
    else:
        print('Algo deu errado, tente novamente')
except:
    print('Algo deu errado, tente com numeros inteiros ou fracionarios')

