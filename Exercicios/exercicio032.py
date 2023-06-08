from datetime import date

ano_atual = date.today().year # ano atual 

ano = int(input('Informe o ano: '))


"""
    Um ano bissesto precisa ter o resto da div por 4 igual a 0
    ou o resto da div por 100 for diderente de 0. Caso contrario,
    O ano não é bissesto. 
    
"""

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'{ano} é um ano bissesto.')
else: 
    print(f'{ano} não é um ano bissesto')