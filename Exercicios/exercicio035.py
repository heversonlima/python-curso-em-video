"""
    soma dos menores precisam ser maior que a reta maior
"""

r1 = float(input(f'Digite o compriminto da primeira reta: '))
r2 = float(input(f'Digite o compriminto da segunda reta: '))
r3 = float(input(f'Digite o compriminto da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r2 and r3 < r2 + r1:
    print(f'Com as retas {r1:.0f}, {r2:.0f}, {r3:.0f}\nÉ possivel fazer um triangulo')
else:
    print(f'Com as retas {r1:.0f}, {r2:.0f}, {r3:.0f}\nNão é possivel fazer um triangulo')

"""if r1 < r2 and r1 < r3:
    menor1 = r1
    if r2 < r3:
        menor2 = r2
    else:
        menor2 = r3
elif r2 < r1 and r2 < r3:
    menor1 = r2
    if r1 < r3:
        menor2 = r1
    else:
        menor2 = r3
elif r3 < r1 and r3 < r2:
    menor1 = r3
    if r1 < r2:
        menor2 = r1
    else:
        menor2 = r2"""
