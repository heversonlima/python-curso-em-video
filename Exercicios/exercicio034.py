salario = float(input('Informe seu salario: '))

if salario > 1250.0:
    novo_sal = salario * 1.10 # salario mais 10%
    print(f'Seu salario ajustado: R${novo_sal:.2f}')
elif salario < 1250.0 & salario > 0:
    novo_sal = salario * 1.15 #salario mais 15%
    print(f'Seu novo salario: {novo_sal:.2f}')