# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:


r1 = float(input(f'Digite o compriminto da primeira reta: '))
r2 = float(input(f'Digite o compriminto da segunda reta: '))
r3 = float(input(f'Digite o compriminto da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r2 and r3 < r2 + r1:
    print(f'Com as retas {r1:.0f}, {r2:.0f}, {r3:.0f}\nÉ possivel fazer um triangulo')
    if r1 == r2 == r3:
        print('Com estas retas formamos um triangulo equilatero..')
    elif r1 != r2 != r3 != r1:
        print('Escaleno')
    else:
        print('Isoles')
else:
    print(f'Com as retas {r1:.0f}, {r2:.0f}, {r3:.0f}\nNão é possivel fazer um triangulo')