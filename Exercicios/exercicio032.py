ano = int(input('Informe o ano: '))

"""
    Um ano bissesto precisa ter o resto da div por 4 igual a 0
    ou o resto da div por 100 for diderente de 0. Caso contrario,
    O ano não é bissesto. 
    
"""

if ano % 4 != 0:
    if ano % 400 != 0:
        print(f'{ano} não é um ano bissesto.')
elif ano % 100 != 0: 
    print(f'{ano} é um ano bissesto.')