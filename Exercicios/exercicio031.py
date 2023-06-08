qtdKmViagem = float(input('Informe a distancia em Km/h de sua viagem'))

if qtdKmViagem > 200.0:
    print(f'Ok, o preço de sua passagem vai sair por: {qtdKmViagem * 0.45}')
else:
    print(f'Ok, o preço de sua passagem vai sair por: {qtdKmViagem * 0.50}')
