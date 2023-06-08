velocidade = float(input("Em quantos km/h seu carro esta correndo? "))


if velocidade > 80.0:

    km_ajustado = velocidade - 80.0
    multa = km_ajustado * 7.0

    print(f'Você ultrapassou o limite de velociade e foi multado\nMulta: R${multa}')
else:
    print('Você está dentro do limite de velocidade e não recebeu nenhuma multa')